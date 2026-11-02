import pytest

from src.database import _load_database_url


def test_database_url_environment_has_priority(monkeypatch, tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text(
        "DATABASE_URL=sqlite+pysqlite:///from-file.db\n", encoding="utf-8"
    )
    monkeypatch.setenv("DATABASE_URL", "sqlite+pysqlite:///from-process.db")

    assert (
        _load_database_url(env_file)
        == "sqlite+pysqlite:///from-process.db"
    )


def test_database_url_loads_from_dotenv(monkeypatch, tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text(
        "DATABASE_URL=sqlite+pysqlite:///from-file.db\n", encoding="utf-8"
    )
    monkeypatch.delenv("DATABASE_URL", raising=False)

    assert _load_database_url(env_file) == "sqlite+pysqlite:///from-file.db"


def test_database_url_is_required(monkeypatch, tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text("# no database configured\n", encoding="utf-8")
    monkeypatch.delenv("DATABASE_URL", raising=False)

    with pytest.raises(RuntimeError, match="DATABASE_URL is not configured"):
        _load_database_url(env_file)
