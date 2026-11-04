"""Allow integration checks to inspect a newly generated report directory."""

from pathlib import Path

import pytest

from integrity.pipeline import ROOT


def pytest_addoption(parser):
    parser.addoption("--reports-dir", default="reports", help="Main batch reports to validate")
    parser.addoption(
        "--challenge-reports-dir", default="challenge_reports", help="Challenge reports to validate"
    )


@pytest.fixture(scope="session")
def report_dir(request):
    return (ROOT / Path(request.config.getoption("--reports-dir"))).resolve()


@pytest.fixture(scope="session")
def challenge_report_dir(request):
    return (ROOT / Path(request.config.getoption("--challenge-reports-dir"))).resolve()
