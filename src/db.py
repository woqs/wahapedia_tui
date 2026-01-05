from sqlalchemy import create_engine
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

def get_models_from_sheet(sheet: models.Datasheet) -> list[models.DatasheetsModels]:
    return session.query(
        models.DatasheetsModels
    ).where(
        models.DatasheetsModels.datasheet_id == sheet.id
    ).all()
