"""Real additional parser edge cases used during the updated-specification audit."""

import sys

import fitz
from docx import Document
import pytest

from integrity.extractors import Extractor
from integrity.pipeline import load_config


def test_docx_heading_and_table_have_real_body_references(tmp_path):
    path = tmp_path / "section-table.docx"
    document = Document()
    document.add_heading("Operations", level=1)
    document.add_paragraph("The workshop records equipment faults before ordering spare parts.")
    table = document.add_table(rows=1, cols=2)
    table.cell(0, 0).text = "Cold storage"
    table.cell(0, 1).text = "Inspect seals every evening"
    document.save(path)
    result = Extractor(load_config()).extract(path)
    assert result.status == "ok"
    assert [unit.location["paragraph"] for unit in result.units] == [1, 2, 3, 4]
    assert all(unit.location["section"] == "Operations" for unit in result.units)
    assert result.units[3].location["table_column"] == 2
    assert result.units[3].text == "Inspect seals every evening"
    assert all("page" not in unit.location for unit in result.units)


def test_password_protected_pdf_does_not_stop_subsequent_extraction(tmp_path):
    path = tmp_path / "encrypted.pdf"
    with fitz.open() as document:
        document.new_page().insert_text((72, 72), "Synthetic encrypted extraction fixture")
        document.save(
            path,
            encryption=fitz.PDF_ENCRYPT_AES_128,
            owner_pw="fixture-owner",
            user_pw="fixture-reader",
        )
    extractor = Extractor(load_config())
    result = extractor.extract(path)
    assert result.status == "error"
    assert any("Password-protected" in warning for warning in result.warnings)
    assert extractor.extract(tmp_path / "missing.pdf").status == "error"


@pytest.mark.skipif(sys.platform != "win32", reason="Tests a real Windows exclusive read lock")
def test_unreadable_file_is_reported_without_mocking_open(tmp_path):
    import ctypes
    from ctypes import wintypes

    path = tmp_path / "locked.pdf"
    path.write_bytes(b"%PDF synthetic locked fixture")
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel32.CreateFileW.argtypes = [
        wintypes.LPCWSTR,
        wintypes.DWORD,
        wintypes.DWORD,
        wintypes.LPVOID,
        wintypes.DWORD,
        wintypes.DWORD,
        wintypes.HANDLE,
    ]
    kernel32.CreateFileW.restype = wintypes.HANDLE
    kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
    handle = kernel32.CreateFileW(str(path), 0x80000000, 0, None, 3, 0x80, None)
    assert handle != ctypes.c_void_p(-1).value, ctypes.get_last_error()
    try:
        result = Extractor(load_config()).extract(path)
        assert result.status == "error"
        assert not result.units
        assert any("PermissionError" in warning for warning in result.warnings)
    finally:
        kernel32.CloseHandle(handle)
