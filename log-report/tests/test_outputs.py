import json
from pathlib import Path

REPORT = Path("/app/report.json")


def test_report_exists():
    """Verifies success criterion 2."""
    assert REPORT.exists(), "report.json not found"


def test_report_is_valid_json():
    """Verifies success criterion 3."""
    json.loads(REPORT.read_text())


def test_report_fields():
    """Verifies success criterion 4."""
    data = json.loads(REPORT.read_text())
    assert set(data.keys()) == {
        "total_requests",
        "unique_ips",
        "top_path",
    }, "report.json contains incorrect fields"


def test_report_values():
    """Verifies success criterion 5."""
    data = json.loads(REPORT.read_text())

    expected = {
        "total_requests": 6,
        "unique_ips": 3,
        "top_path": "/index.html",
    }

    assert data == expected, "report values do not match the expected summary"