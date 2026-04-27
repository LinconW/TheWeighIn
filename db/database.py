from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#Creates database at DATABASE_URL
DATABASE_URL = "sqlite:///./weights.db"

# Creates new database connections and holds onto connections for fast reuse
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()