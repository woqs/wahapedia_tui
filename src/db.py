from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
import models

connection_string = "postgresql://wahapedia:wahapedia@db:5432/wahapedia" 
engine = create_engine(connection_string)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def get_faction_list() -> list[models.Factions]:
    return session.query(models.Factions).all()

def get_datasheets_for_faction(factionId: str) -> list[models.Datasheets]:
    return session.query(
        models.Datasheets
    ).where(
        models.Datasheets.faction_id == factionId
    )

def get_models_enriched_sheet(sheet: models.Datasheet) -> models.Datasheets:
    stmt = select(
        models.Datasheets
    ).join(
        models.Datasheets.models
    ).join(
        models.Datasheets.models_cost
    ).where(
        models.Datasheets.id == sheet.id
    )
    result = session.execute(stmt)
    return result.fetchone()[0]
