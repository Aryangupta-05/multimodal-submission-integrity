"""Deterministic source text + reproducible containers; TTS voice bytes vary by OS.

All text was written with Codex assistance for this assessment and is synthetic.
Independent means independently composed subject matter, never human authorship.
Only generation/evaluation reads the manifest, never runtime scoring.
"""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import wave

ROOT = Path(__file__).resolve().parents[1]

PROMPT = """Riverton University invites teams to design a practical improvement for a small community institution. The institution has limited money, uncertain demand, and a responsibility to serve residents fairly. Your proposal should identify one operational problem, explain why existing practices are inadequate, and recommend an intervention that can be tested within one academic term. State the assumptions behind your analysis and explain which observations would cause you to change your recommendation. Include a way to measure progress without collecting unnecessary personal information. Discuss an implementation risk, a possible unintended consequence, and a low cost method for gathering feedback. The evaluation panel values clear reasoning over ambitious technology. Teams may use simple schedules, physical tools, or public information where appropriate. Do not assume that additional staff, permanent subsidies, or expensive equipment will become available. Conclude by explaining how the institution could decide whether to continue, adapt, or stop the proposed pilot after review."""

HARBOR_SPEECH = """The harbor cooperative should repair its cold storage before buying another delivery truck. Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates would protect the catch. We would measure discarded kilograms each morning and pause expansion until spoilage falls for four consecutive weeks."""

HARBOR = [
    """A coastal fish cooperative is losing income because its storage rooms warm overnight. The members have proposed purchasing another delivery truck, yet dispatch records show that vehicles spend their mornings waiting beside unreliable refrigeration equipment. Expanding transport before stabilizing storage would increase idle capacity rather than preserve more fish. The first investment should therefore address the temperature failure at the landing site. This is a synthetic business case; the quantities below are illustrative rather than observations from a real cooperative.

The pilot would assign two members to inspect seals and clean condenser coils every evening. A paper log would record room temperature at closing and opening. Repairs would be funded from a ring fenced maintenance reserve instead of an additional vehicle loan. Members would compare spoilage during similar landing volumes, since a small catch can make a weak process appear successful. If repair parts cannot arrive promptly, insulated crates provide a temporary buffer without committing the group to a new vehicle.""",
    HARBOR_SPEECH
    + "\n\n"
    + """The decision rule should use the fraction of landed fish discarded, not revenue alone, because auction prices change with weather and seasonal supply. Every participating vessel would receive the same access to crates during the trial. A rotating committee would publish aggregate totals without disclosing individual earnings. A four week reduction in waste would justify extending the maintenance arrangement, while unstable temperatures would trigger a specialist inspection. The cooperative should stop the pilot if contamination incidents increase, even if transport margins improve. These checks distinguish the operational claim from a generic recommendation to expand distribution.""",
]

CLINIC = [
    """A rural clinic should reserve its first morning appointments for patients travelling on the only village bus. That bus arrives before the normal booking desk opens, so visitors currently wait through the busiest part of the day. Keeping a small protected block would reduce wasted journeys without expanding the medical staff. The clinic should compare missed appointments for bus passengers with missed appointments for nearby residents over six weeks. The experiment must not displace emergencies or create a preference for people who own phones.""",
    """Reception staff can issue paper appointment cards through the village shop each Thursday. A numbered card holds the visit time without recording a diagnosis. Unused reserved slots should become available to everyone fifteen minutes before the consultation begins. Nurses should record whether a delayed bus caused a missed visit, rather than assuming the patient ignored the booking. If travel related absences remain unchanged, the clinic should alter its timetable instead of sending more reminder messages. This intervention targets transport timing rather than patient motivation.""",
]

PARAPHRASE = [
    """For a countryside health centre, the earliest consultations ought to be set aside for people arriving on the single local bus. Public transport reaches the building before reception starts taking bookings, leaving those visitors stuck in the daily rush. A modest allocation of protected slots could prevent fruitless trips without hiring additional clinicians. During a six week trial, compare the nonattendance rate of public transport users against that of neighbours living close by. Urgent cases must retain priority, and access cannot depend on having a mobile telephone.""",
    """Each Thursday the community store could distribute numbered paper cards specifying consultation times, with no medical condition written down. Any protected booking that remains unused should be released to other patients a quarter hour before the clinician is ready. Staff need to distinguish bus delays from deliberate nonattendance when recording an absence. Should transport linked missed visits persist, revise the opening schedule rather than increasing reminder notifications. The proposal fixes a mismatch with the bus timetable, instead of blaming residents for insufficient commitment to treatment.""",
]

ANSWERS = {
    "05_prompt_water.pdf": """I would begin with the school's drinking water taps. A caretaker can place identical marked buckets under three taps for one minute before pupils arrive. Recording the collected volume twice a week would reveal whether sediment is restricting one branch of the pipe. Cleaning a removable filter is a smaller commitment than replacing the full plumbing network. The trial needs no pupil names or electronic sensors.

The principal risk is confusing a fall in municipal pressure with a blocked filter. The caretaker should therefore measure a nearby outdoor tap at the same time. If every tap slows together, local maintenance is unlikely to help. A labelled notice should tell pupils when a tap is closed, with another drinking point kept available. At the end of six weeks, consistent recovery at the cleaned tap would support extending the routine. Persistent brown water would end the experiment and require an appropriate water quality inspection before reuse.""",
    "06_prompt_library.pdf": """My library proposal concerns lost shelf locations rather than late returns. Volunteers currently move donated books whenever a shelf fills, leaving the catalogue physically inaccurate. A set of removable coloured shelf cards would identify temporary overflow locations. A reader could find a moved title by consulting a single board beside the entrance. Each week a volunteer would sample twelve catalogue entries and count titles that can be found without asking for help.

The board could become another stale source of information. To prevent this, each shelf move should require moving its card before the books themselves. A second volunteer should check the board during opening preparations. Reader comments can be collected on anonymous slips, then discarded after tallying recurring problems. If retrieval time does not improve after two rotation cycles, the library should simplify its classification rules instead of purchasing more shelving. Large print labels would keep the physical system accessible to older visitors.""",
    "07_prompt_bakery.docx": """The community bakery discards unsold bread at closing, but baking less every day could leave weekend customers empty handed. I propose a two colour chalkboard tally of early and late sales. The baker can record loaves by product without linking purchases to individual customers. After a fortnight, dough batches for slow weekday afternoons can be reduced while weekend production remains unchanged.

Weather and a neighbouring school holiday could distort the short trial, so the tally should include those circumstances in a margin note. Donating edible leftovers must remain an option while production is adjusted. A reduction in waste accompanied by repeated stockouts would count as failure, because discarded weight alone rewards underproduction. The baker should compare both leftovers and unfilled requests before continuing. Feedback can come from a small basket of paper comments near the counter. The proposed intervention is a production scheduling change that uses equipment already present in the shop.""",
    "08_prompt_museum.docx": """The local history museum has fragile handwritten letters in a room with strong afternoon sunlight. My proposal moves those letters into a shaded cabinet and displays facsimiles during the brightest hours. A volunteer can use a paper rotation calendar to keep handling predictable. The pilot would record the number of cabinet openings and visible changes in the display mounts rather than asking visitors for demographic information.

Replicas may disappoint visitors who expect original objects. A small label should explain the conservation reason, while a supervised viewing hour can preserve access to originals. The main implementation risk is damage during repeated transfers, so a single trained custodian should move the letters in supportive folders. If relocation increases handling incidents, the museum should stop rotating originals and retain the shaded display permanently. Anonymous visitor questions can show whether the explanation is understandable. The decision rests on conservation and access rather than attendance growth.""",
    "09_prompt_garden_llm.docx": """The neighbourhood garden should test a shared seed exchange drawer before opening additional planting beds. Unused packets currently remain in separate sheds, and new gardeners buy duplicate varieties. A wooden organiser with broad labels can make surplus seeds visible without collecting anyone's address. Volunteers should note the number of packets added, taken, and returned at the end of each weekend.

Furthermore, packet age needs to be visible because poor germination could discourage participation. Gardeners can write the harvest year and perform a small germination check using a damp cloth. Moreover, the trial must keep invasive species out of the exchange, using a short approved list prepared from local guidance. Additionally, anonymous comments can identify confusing labels or missing varieties. In conclusion, the garden should continue only if shared packets are actually planted and participants report useful choices. Drawer activity alone does not establish success when seeds are discarded rather than grown.""",
}

EXTERNAL = """A queue works best when arrivals can see how service order is decided. Numbered tickets separate a visitor's place in line from the place where that visitor stands. This lets people sit, read, or wait in shade without losing their turn. The organiser should announce exceptions openly and keep an accessible route to the service desk. A ticket system does not create more service capacity; it only makes the existing waiting process easier to understand."""

EXTERNAL_SPEECH = """Numbered tickets separate a visitor's place in line from the place where that visitor stands. This lets people sit, read, or wait in shade without losing their turn. The organiser should announce exceptions openly and keep an accessible route to the service desk."""

INDEPENDENT_SPEECH = """Our astronomy club will map the moon with hand drawn sketches rather than buy a larger telescope. Members will observe the same crater at different phases, marking shadows with pencils. Comparing those sketches will teach how sunlight changes the visible relief. We will keep the drawings in a shared notebook."""


def pdf(path, pages):
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

    styles = getSampleStyleSheet()
    styles["BodyText"].fontName = "Helvetica"
    styles["BodyText"].fontSize = 11
    styles["BodyText"].leading = 16
    flow = []
    for i, page in enumerate(pages):
        if i:
            flow.append(PageBreak())
        for text in page.split("\n\n"):
            flow += [Paragraph(text.replace("&", "&amp;"), styles["BodyText"]), Spacer(1, 12)]

    def margins(canvas, document):
        canvas.setFont("Helvetica", 9)
        canvas.drawString(54, 812, "Riverton synthetic case collection")
        canvas.drawString(54, 30, f"Case collection | Page {document.page}")

    SimpleDocTemplate(
        str(path),
        pagesize=(595, 842),
        leftMargin=54,
        rightMargin=54,
        topMargin=60,
        bottomMargin=54,
        invariant=1,
    ).build(flow, onFirstPage=margins, onLaterPages=margins)


def docx(path, paragraphs):
    from docx import Document
    from docx.shared import Inches, Pt, RGBColor

    d = Document()
    sec = d.sections[0]
    sec.top_margin = sec.bottom_margin = Inches(0.75)
    sec.left_margin = sec.right_margin = Inches(0.8)
    style = d.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)
    style.font.color.rgb = RGBColor(0, 0, 0)
    style.paragraph_format.space_after = Pt(10)
    for paragraph in paragraphs:
        d.add_paragraph(paragraph)
    d.core_properties.author = "Synthetic assessment corpus with Codex assistance"
    d.save(path)


def speech_wav(text, path):
    # SAPI is local Windows TTS. On Linux, install espeak-ng and use its CLI.
    if sys.platform == "win32":
        import pyttsx3

        engine = pyttsx3.init()
        engine.setProperty("rate", 145)
        engine.save_to_file(text, str(path))
        engine.runAndWait()
        engine.stop()
    else:
        executable = shutil.which("espeak-ng") or shutil.which("espeak")
        if not executable:
            raise RuntimeError("Dataset regeneration requires espeak-ng on Linux or Windows SAPI.")
        subprocess.run([executable, "-s", "145", "-w", str(path), text], check=True)


def video(path, text=None):
    import imageio_ffmpeg

    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    with tempfile.TemporaryDirectory() as tmp:
        audio = Path(tmp) / "voice.wav"
        if text:
            speech_wav(text, audio)
            with wave.open(str(audio)) as wav:
                duration = wav.getnframes() / wav.getframerate()
            if not 10 <= duration <= 30:
                raise ValueError(f"Speech duration {duration:.2f}s outside target 10-30s")
            command = [
                ffmpeg,
                "-nostdin",
                "-y",
                "-v",
                "error",
                "-f",
                "lavfi",
                "-i",
                "color=c=0x17324d:s=640x360:r=15",
                "-i",
                str(audio),
                "-c:v",
                "libx264",
                "-pix_fmt",
                "yuv420p",
                "-c:a",
                "aac",
                "-b:a",
                "96k",
                "-shortest",
                str(path),
            ]
        else:
            duration = 12
            command = [
                ffmpeg,
                "-nostdin",
                "-y",
                "-v",
                "error",
                "-f",
                "lavfi",
                "-i",
                "color=c=0x17324d:s=640x360:r=15",
                "-t",
                "12",
                "-an",
                "-c:v",
                "libx264",
                "-pix_fmt",
                "yuv420p",
                str(path),
            ]
        subprocess.run(command, check=True, timeout=120)
    return round(duration, 3)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--documents-only", action="store_true")
    parser.add_argument("--videos-only", action="store_true")
    args = parser.parse_args()
    target = ROOT / "sample_submissions"
    target.mkdir(exist_ok=True)
    (ROOT / "config").mkdir(exist_ok=True)
    (ROOT / "config/common_prompt.txt").write_text(PROMPT, encoding="utf-8")
    if not args.videos_only:
        pdf(target / "01_harbor.pdf", HARBOR)
        shutil.copyfile(target / "01_harbor.pdf", target / "02_harbor_copy.pdf")
        docx(target / "03_clinic.docx", CLINIC)
        docx(target / "04_clinic_paraphrase.docx", PARAPHRASE)
        for name, answer in ANSWERS.items():
            if name.endswith(".pdf"):
                pdf(target / name, [PROMPT + "\n\n" + answer])
            else:
                docx(target / name, [PROMPT] + answer.split("\n\n"))
        pdf(target / "10_external.pdf", [EXTERNAL])
        (target / "15_empty.pdf").write_bytes(b"")
        references = ROOT / "reference_corpus"
        references.mkdir(exist_ok=True)
        data = {
            "title": "Transparent queue design",
            "text": EXTERNAL,
            "source_url": "https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json",
            "provenance_type": "synthetic_local_reference",
            "author": "Codex-assisted synthetic corpus",
            "license": "CC0-1.0",
            "retrieval_note": "Authored locally, not scraped. Source URL is the committed source location in the private repository.",
            "sha256": hashlib.sha256(EXTERNAL.encode()).hexdigest(),
        }
        (references / "queue_design.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
    durations = {}
    if not args.documents_only:
        for name, text in [
            ("11_harbor_pitch.mp4", HARBOR_SPEECH),
            ("12_external_pitch.mp4", EXTERNAL_SPEECH),
            ("13_independent_pitch.mp4", INDEPENDENT_SPEECH),
            ("14_silent.mp4", None),
        ]:
            durations[name] = video(target / name, text)
            print(name, durations[name], flush=True)
    else:
        previous = target / "dataset_manifest.json"
        if previous.exists():
            durations = {
                f["file"]: f["duration_seconds"]
                for f in json.loads(previous.read_text())["files"]
                if "duration_seconds" in f
            }
    entries = []
    for path in sorted(target.iterdir()):
        if path.suffix not in {".pdf", ".docx", ".mp4"}:
            continue
        entry = {
            "file": path.name,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "bytes": path.stat().st_size,
            "provenance": "Synthetic, Codex-assisted content; no private student data",
            "license": "CC0-1.0",
            "ai_authored": True,
            "valid": path.name != "15_empty.pdf",
            "assessable": path.name not in {"14_silent.mp4", "15_empty.pdf"},
        }
        if path.name in durations:
            entry["duration_seconds"] = durations[path.name]
        if path.name in ANSWERS:
            entry["shared_prompt_words"] = len(PROMPT.split())
            entry["independent_answer"] = True
        if path.name == "09_prompt_garden_llm.docx":
            entry["explicit_llm_example"] = True
        entries.append(entry)
    manifest = {
        "dataset_version": "1.0",
        "generation_command": "python scripts/generate_dataset.py",
        "text_origin": "All prose generated with OpenAI Codex assistance on 2026-11-04. Independent labels describe relationships, not human authorship.",
        "media_origin": "Local TTS: Windows SAPI default English voice at 145 words/min; FFmpeg H.264/AAC. Linux espeak-ng fallback changes audio and ASR outputs.",
        "reproducibility": "Source texts and relationships fixed; DOCX ZIP metadata/TTS bytes may vary across runtimes. Committed files + SHA256 are benchmark identity.",
        "runtime_isolation": "Only dataset generator and evaluation read these labels. Runtime excludes manifest metadata.",
        "files": entries,
        "positive_peer_pairs": [
            ["01_harbor.pdf", "02_harbor_copy.pdf"],
            ["01_harbor.pdf", "11_harbor_pitch.mp4"],
            ["02_harbor_copy.pdf", "11_harbor_pitch.mp4"],
            ["03_clinic.docx", "04_clinic_paraphrase.docx"],
            ["10_external.pdf", "12_external_pitch.mp4"],
        ],
        "relationships": [
            {"type": "exact_copy", "files": ["01_harbor.pdf", "02_harbor_copy.pdf"]},
            {
                "type": "semantic_paraphrase",
                "files": ["03_clinic.docx", "04_clinic_paraphrase.docx"],
            },
            {
                "type": "cross_modal",
                "files": ["01_harbor.pdf", "11_harbor_pitch.mp4"],
                "pdf_page": 2,
                "intended_speech": HARBOR_SPEECH,
            },
            {
                "type": "external_copy",
                "files": ["10_external.pdf", "12_external_pitch.mp4"],
                "reference": "reference:queue_design",
            },
        ],
        "external_positive_files": ["10_external.pdf", "12_external_pitch.mp4"],
        "shared_prompt_files": list(ANSWERS),
        "shared_prompt_word_count": len(PROMPT.split()),
        "independent_files": list(ANSWERS) + ["13_independent_pitch.mp4"],
        "intended_transcripts": {
            "11_harbor_pitch.mp4": HARBOR_SPEECH,
            "12_external_pitch.mp4": EXTERNAL_SPEECH,
            "13_independent_pitch.mp4": INDEPENDENT_SPEECH,
        },
        "label_policy": "Any substantive authored content copy/paraphrase is positive. Shared configured prompt is negative. Other assessable unordered pairs are negative. Invalid inputs excluded from pair classification and separately tested.",
    }
    (target / "dataset_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Saved manifest for {len(entries)} files; prompt {len(PROMPT.split())} words.")


if __name__ == "__main__":
    main()
