from core.db import Session, engine


def test_engine_configured(env):
    assert str(engine.url) == env("SQLALCHEMY_DATABASE_URI")


def test_session_configured(env):
    session = Session()

    assert str(session.bind.engine.url) == env("SQLALCHEMY_DATABASE_URI")
