import os
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")


# Define the MySQL engine using MySQL Connector/Python
engine_setup_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

print(engine_setup_string)

engine = sqlalchemy.create_engine(
    engine_setup_string,
    echo=True
)

# Define and create the table
Base = declarative_base()

Base.metadata.create_all(engine)

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()
