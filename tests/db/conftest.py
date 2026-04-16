import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@pytest.fixture
def db_connection():
    db = create_engine("sqlite:///1_db.sqlite3")  # postgresql://username:password@localhost:5432/dbname
    connection = db.connect()

    yield connection

    connection.close()
    db.dispose()



@pytest.fixture
def db_session():

    db = create_engine("sqlite:///1_db.sqlite3")
    Session = sessionmaker(bind=db)
    session = Session()

    yield session

    session.close()
    db.dispose()