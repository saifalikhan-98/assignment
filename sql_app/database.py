from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sql_app.postgres_conf import PostgresConfiguration

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Saif@329@postgresserver/db"
db=PostgresConfiguration()
engine = create_engine(
    db.postgres_db_path,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()