"""Real file/report integration checks. No ingestion/ASR/embedding mocks."""

from hashlib import sha256
import json

import av
import jsonschema
import numpy as np
import pytest

from integrity.extractors import Extractor
from integrity.index import Embedder
from integrity.matching import coverage
from integrity.pipeline import ROOT, load_config
from integrity.text import normalize, make_windows, passage, exclude_repeated_prefixes
from integrity.types import Document, Unit


@pytest.fixture(scope="session")
def reports():
    return {
        p.name.removesuffix(".json"): json.loads(p.read_text(encoding="utf-8"))
        for p in (ROOT / "reports/individual").glob("*.json")
    }


@pytest.fixture(scope="session")
def raw():
    return json.loads((ROOT / "reports/extracted_documents.json").read_text(encoding="utf-8"))


@pytest.fixture(scope="session")
def challenge():
    return {
        p.name.removesuffix(".json"): json.loads(p.read_text(encoding="utf-8"))
        for p in (ROOT / "challenge_reports/individual").glob("*.json")
    }


def test_dataset_inventory_and_hashes():
    manifest = json.loads((ROOT / "sample_submissions/dataset_manifest.json").read_text())
    files = manifest["files"]
    assert len(files) == 15
    assert sum(f["file"].endswith(".pdf") and f["bytes"] > 0 for f in files) == 5
    assert sum(f["file"].endswith(".docx") for f in files) == 5
    assert sum(f["file"].endswith(".mp4") for f in files) == 4
    for f in files:
        assert (
            sha256((ROOT / "sample_submissions" / f["file"]).read_bytes()).hexdigest()
            == f["sha256"]
        )
    assert (ROOT / "sample_submissions/01_harbor.pdf").read_bytes() == (
        ROOT / "sample_submissions/02_harbor_copy.pdf"
    ).read_bytes()


@pytest.mark.parametrize(
    "name", ["11_harbor_pitch.mp4", "12_external_pitch.mp4", "13_independent_pitch.mp4"]
)
def test_playable_spoken_videos(name):
    with av.open(str(ROOT / "sample_submissions" / name)) as container:
        assert container.streams.video and container.streams.audio
        assert 10 <= container.duration / av.time_base <= 30
        frames = list(container.decode(audio=0))
        assert frames and any(np.max(np.abs(f.to_ndarray())) > 0.01 for f in frames)


def test_reports_and_schema(reports):
    assert len(reports) == 15
    schema = json.loads((ROOT / "report_schema.json").read_text())
    for name, r in reports.items():
        jsonschema.validate(r, schema)
        assert (ROOT / "reports/individual" / (name + ".md")).stat().st_size > 0


def test_every_passage_is_exact_and_location_valid(reports, raw):
    count = 0
    for name, r in reports.items():
        for match in r["peer_matches"] + r["external_matches"]:
            for side, doc_id, key in [
                ("query", name, "query_passage"),
                ("matched", match["matched_file"], "matched_passage"),
            ]:
                doc = raw[doc_id]
                pieces = []
                for span in match["location"][side + "_spans"]:
                    unit = doc["units"][span["unit_index"]]
                    a, b = span["char_start"], span["char_end"]
                    assert 0 <= a < b <= len(unit["text"])
                    assert unit["text"][a:b] == span["text"]
                    for field, value in unit["location"].items():
                        assert span[field] == value
                    pieces.append(span["text"])
                assert "\n".join(pieces) == match[key]
                count += 1
    assert count > 20


def test_saved_raw_extraction_matches_fresh_original_parsers(raw):
    extractor = Extractor(load_config())
    for name in raw:
        if name.endswith((".pdf", ".docx")) and raw[name]["status"] == "ok":
            fresh = extractor.extract(ROOT / "sample_submissions" / name)
            assert [u.text for u in fresh.units] == [u["text"] for u in raw[name]["units"]]
            assert [u.location for u in fresh.units] == [u["location"] for u in raw[name]["units"]]


def test_self_excluded_duplicate_identity_retained(reports):
    for name, r in reports.items():
        assert all(m["matched_file"] != name for m in r["peer_matches"])
    assert any(
        m["matched_file"] == "02_harbor_copy.pdf" and m["similarity_score"] > 0.999
        for m in reports["01_harbor.pdf"]["peer_matches"]
    )


def test_crossmodal_page_two_and_real_timestamp(reports, raw):
    matches = [
        m
        for m in reports["11_harbor_pitch.mp4"]["multimodal_matches"]
        if m["matched_file"] == "01_harbor.pdf"
    ]
    assert matches
    assert any(2 in m["location"]["matched_pages"] for m in matches)
    duration = raw["11_harbor_pitch.mp4"]["metadata"]["duration_seconds"]
    for m in matches:
        assert (
            0
            <= m["location"]["query_start_seconds"]
            < m["location"]["query_end_seconds"]
            <= duration + 0.1
        )
        assert "query_page" not in m["location"]


def test_paraphrase_is_semantic_with_honest_docx_refs(reports):
    matches = [
        m
        for m in reports["03_clinic.docx"]["peer_matches"]
        if m["matched_file"] == "04_clinic_paraphrase.docx"
    ]
    assert any(m["similarity_score"] > 0.8 and m["lexical_jaccard"] < 0.4 for m in matches)
    for m in matches:
        assert "query_page" not in m["location"]
        assert m["location"]["query_paragraphs"] and m["location"]["matched_paragraphs"]


def test_boilerplate_discounted_but_copied_answers_visible(reports, challenge):
    names = [
        "05_prompt_water.pdf",
        "06_prompt_library.pdf",
        "07_prompt_bakery.docx",
        "08_prompt_museum.docx",
        "09_prompt_garden_llm.docx",
    ]
    for name in names:
        assert reports[name]["extraction"]["excluded_word_count"] == 151
        assert reports[name]["scores"]["peer_similarity_percentage"] == 0
        assert reports[name]["extraction"]["eligible_word_count"] > 100
    assert any(
        m["matched_file"] == "prompt_copy_b.docx"
        for m in challenge["prompt_copy_a.docx"]["peer_matches"]
    )
    assert challenge["prompt_copy_a.docx"]["scores"]["peer_similarity_percentage"] == 100


def test_coverage_union_and_no_cosine_percent(reports):
    for r in reports.values():
        if not r["extraction"]["assessable"]:
            continue
        assert r["scores"]["peer_similarity_percentage"] == coverage(
            r["peer_matches"], r["extraction"]["eligible_word_count"]
        )
        assert r["scores"]["external_similarity_percentage"] == coverage(
            r["external_matches"], r["extraction"]["eligible_word_count"]
        )
        assert r["scores"]["peer_similarity_percentage"] <= 100
    match = {"query_token_ids": [1, 2, 3]}
    assert coverage([match, match], 6) == 50
    assert coverage([], 0) is None


def test_external_is_separate_and_provenanced(reports):
    for name in ["10_external.pdf", "12_external_pitch.mp4"]:
        r = reports[name]
        assert r["scores"]["external_similarity_percentage"] >= 50
        assert all(m["matched_file"].startswith("reference:") for m in r["external_matches"])
        assert all(not m["matched_file"].startswith("reference:") for m in r["peer_matches"])
        assert all(
            m["provenance"]["source_url"].startswith("https://github.com/")
            for m in r["external_matches"]
        )


@pytest.mark.parametrize("name,status", [("15_empty.pdf", "empty"), ("14_silent.mp4", "no_audio")])
def test_unavailable_is_null_not_zero(reports, name, status):
    r = reports[name]
    assert r["extraction"]["status"] == status
    assert r["total_integrity_risk"] == "UNABLE_TO_ASSESS"
    assert all(value is None for value in r["scores"].values())


def test_edge_statuses_and_partial_assessment(challenge):
    expected = json.loads((ROOT / "evaluation/challenge_ground_truth.json").read_text())["statuses"]
    for name, status in expected.items():
        r = challenge[name]
        assert r["extraction"]["status"] == status
        if status != "partial":
            assert not r["extraction"]["assessable"]
            assert r["scores"]["peer_similarity_percentage"] is None
        assert r["warnings"]
    assert challenge["partial.pdf"]["extraction"]["assessable"]


def test_quotes_references_fully_excluded_and_prompt_only(challenge):
    assert not challenge["only_prompt.docx"]["extraction"]["assessable"]
    reasons = {e["reason"] for e in challenge["attributed.docx"]["exclusions"]}
    assert {"explicitly_attributed_quotation", "reference_list"} <= reasons
    assert not challenge["attributed.docx"]["extraction"]["assessable"]


def test_ai_signal_never_alone_proof(reports):
    r = reports["09_prompt_garden_llm.docx"]
    assert r["ai_indicator"]["calibrated"] is False
    assert r["total_integrity_risk"] == "LOW"
    assert r["scores"]["ai_generated_probability"] == r["ai_indicator"]["score"]
    assert reports["12_external_pitch.mp4"]["ai_indicator"]["status"] == "insufficient_text"


def test_normalization_keeps_unicode_offsets():
    text = "  The \ufb01sh\tand river\u2019s\n  edge. "
    d = normalize(
        Document("unicode.docx", "docx", units=[Unit(text, {"paragraph": 1, "section": "Body"})])
    )
    assert [t.value for t in d.tokens] == ["the", "fish", "and", "river's", "edge"]
    raw, spans = passage(d, list(range(len(d.tokens))))
    assert raw == text[2 : text.index("edge") + 4]
    assert spans[0]["char_start"] == 2


def test_actual_model_chunks_fit_context_and_overlap():
    config = load_config()
    e = Embedder(config)
    d = normalize(Extractor(config).extract(ROOT / "sample_submissions/01_harbor.pdf"))
    chunks = make_windows(d, e.tokenizer, target=220, overlap=35)
    assert len(chunks) >= 2
    assert all(len(e.tokenizer.encode(w.text)) <= 222 for w in chunks)
    assert all(200 <= w.model_tokens <= 220 for w in chunks[:-1])
    assert set(chunks[0].token_ids) & set(chunks[1].token_ids)
    vectors = e.encode(chunks)
    assert vectors.shape == (len(chunks), 384)
    assert np.allclose(np.linalg.norm(vectors, axis=1), 1, atol=1e-5)


def test_repeated_pdf_margins_removed(raw):
    d = raw["01_harbor.pdf"]
    assert len(d["metadata"]["removed_margins"]) == 4
    assert all("Riverton synthetic case collection" not in u["text"] for u in d["units"])


def test_matrix_unknown_and_self_entries():
    m = json.loads((ROOT / "reports/similarity_matrix.json").read_text())
    for name, row in m.items():
        assert row[name] is None
        assert row["14_silent.mp4"] is None
        assert row["15_empty.pdf"] is None


def test_runtime_has_no_ground_truth_dependency():
    for path in (ROOT / "integrity").glob("*.py"):
        text = path.read_text()
        assert "positive_peer_pairs" not in text
        assert "intended_transcripts" not in text
        assert "explicit_llm_example" not in text


def test_unknown_shared_opening_is_discovered_without_hiding_answers():
    prefix = " ".join(f"common{i}" for i in range(50))
    docs = [
        normalize(
            Document(
                f"case{i}.docx",
                "docx",
                units=[Unit(prefix + f" answer{i} a distinct continuation", {"paragraph": 1})],
            )
        )
        for i in range(5)
    ]
    exclude_repeated_prefixes(docs)
    for doc in docs:
        assert len(doc.excluded) == 50
        assert 50 not in doc.excluded
        assert set(doc.excluded.values()) == {"discovered_common_opening_prefix"}


def test_noncontiguous_raw_spans_do_not_reinsert_excluded_words():
    d = normalize(
        Document(
            "holes.docx",
            "docx",
            units=[Unit("Original answer quoted material original continuation", {"paragraph": 1})],
        )
    )
    text, spans = passage(d, [0, 1, 4, 5])
    assert text == "Original answer\noriginal continuation"
    assert len(spans) == 2
    assert all("quoted material" not in span["text"] for span in spans)
