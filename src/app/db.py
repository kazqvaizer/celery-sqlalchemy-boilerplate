from contextlib import contextmanager

from envparse import env
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

env.read_envfile()

engine = create_engine(env("SQLALCHEMY_DATABASE_URI"), pool_recycle=1800)

Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
