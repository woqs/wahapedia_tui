from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models

connection_string = "postgresql://wahapedia:wahapedia@db:5432/wahapedia" 
engine = create_engine(connection_string, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def get_faction_list() -> list[models.Factions]:
    return session.query(models.Factions).all()
