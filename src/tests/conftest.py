import pytest
from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig
from envparse import env as environment
from sqlalchemy import create_engine
from sqlalchemy.engine.url import make_url
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists, drop_database


@pytest.fixture(scope="session", autouse=True)
def env():
    environment.read_envfile()

    return environment


@pytest.fixture(scope="session", autouse=True)
def engine(env):
    db_url = make_url(env("SQLALCHEMY_DATABASE_URI"))
    db_url = db_url.set(database=f"{db_url.database}_test")

    engine = create_engine(db_url)
    if not database_exists(engine.url):
        create_database(engine.url)

    yield engine

    drop_database(engine.url)


@pytest.fixture(scope="session", autouse=True)
def connection(engine):
    connection = engine.connect()

    alembic_config = AlembicConfig("alembic.ini")
    alembic_config.attributes["connection"] = connection
    alembic_upgrade(alembic_config, "head")

    yield connection

    connection.close()


@pytest.fixture
def session(mocker, connection):
    transaction = connection.begin()
    session = sessionmaker()(bind=connection)

    mocker.patch("sqlalchemy.orm.session.sessionmaker.__call__", return_value=session)

    yield session

    session.close()
    transaction.rollback()
