import urllib.request
import pandas
from sqlalchemy import create_engine
import src.models

if __name__ == "__main__":
    local_filenames = []

    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Factions.csv", "/tmp/Factions.csv")
    local_filenames.append(local_filename)
    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Source.csv", "/tmp/Source.csv")
    local_filenames.append(local_filename)
    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Datasheets.csv", "/tmp/Datasheets.csv")
    local_filenames.append(local_filename)
    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Datasheets_abilities.csv", "/tmp/Datasheets_abilities.csv")
    local_filenames.append(local_filename)
    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Datasheets_keywords.csv", "/tmp/Datasheets_keywords.csv")
    local_filenames.append(local_filename)
    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Datasheets_models.csv", "/tmp/Datasheets_models.csv")
    local_filenames.append(local_filename)
    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Datasheets_options.csv", "/tmp/Datasheets_options.csv")
    local_filenames.append(local_filename)
    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Datasheets_wargear.csv", "/tmp/Datasheets_wargear.csv")
    local_filenames.append(local_filename)
    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Datasheets_unit_composition.csv", "/tmp/Datasheets_unit_composition.csv")
    local_filenames.append(local_filename)
    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Datasheets_models_cost.csv", "/tmp/Datasheets_models_cost.csv")
    local_filenames.append(local_filename)
    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Datasheets_stratagems.csv", "/tmp/Datasheets_stratagems.csv")
    local_filenames.append(local_filename)
    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Datasheets_enhancements.csv", "/tmp/Datasheets_enhancements.csv")
    local_filenames.append(local_filename)
    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Datasheets_detachment_abilities.csv", "/tmp/Datasheets_detachment_abilities.csv")
    local_filenames.append(local_filename)
    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Datasheets_leader.csv", "/tmp/Datasheets_leader.csv")
    local_filenames.append(local_filename)
    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Stratagems.csv", "/tmp/Stratagems.csv")
    local_filenames.append(local_filename)
    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Abilities.csv", "/tmp/Abilities.csv")
    local_filenames.append(local_filename)
    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Enhancements.csv", "/tmp/Enhancements.csv")
    local_filenames.append(local_filename)
    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Detachment_abilities.csv", "/tmp/Detachment_abilities.csv")
    local_filenames.append(local_filename)
    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Detachments.csv", "/tmp/Detachments.csv")
    local_filenames.append(local_filename)
    local_filename, headers = urllib.request.urlretrieve("http://wahapedia.ru/wh40k10ed/Last_update.csv", "/tmp/Last_update.csv")
    local_filenames.append(local_filename)

    print("connection db")
    connection_string = "postgresql://wahapedia:wahapedia@db:5432/wahapedia" 
    engine = create_engine(connection_string)

    for local_filename in local_filenames:
        dbEntity = "".join(map(lambda s: s.capitalize(), local_filename.replace(".csv", "").replace("/tmp/", "").split("_")))
        class_ = getattr(src.models, dbEntity)
        entity = class_()
        csv = pandas.read_csv(local_filename, sep="|")
        csv.to_sql(
            entity.__tablename__,
            con=engine,
            if_exists='append',
            index=False
        )
