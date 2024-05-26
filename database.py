from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Параметры БД
url_object = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password="tyu456jhg",
    host="localhost",
    database="test_base",
)

# Подключение к PostgreSQL
engine = create_engine(url_object)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()

def get_database():
    database = session_local()
    try:
        yield database
    finally:
        database.close()