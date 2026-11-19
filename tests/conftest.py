# tests/conftest.py
from pathlib import Path

import pytest
from esbn_to_mqtt import statistics


@pytest.fixture(autouse=True)
def no_supervisor_token(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    # Keep every test hermetic: nothing may find a token or reach a real Home Assistant.
    monkeypatch.delenv("SUPERVISOR_TOKEN", raising=False)
    monkeypatch.delenv("HASSIO_TOKEN", raising=False)
    monkeypatch.setattr(statistics, "S6_TOKEN_FILE", tmp_path / "missing-s6-token")
    monkeypatch.setattr(statistics, "INIT_ENVIRON_FILE", tmp_path / "missing-environ")
