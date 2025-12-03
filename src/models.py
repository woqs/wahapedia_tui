"""SQLAlchemy models for Wahapedia export data specification."""
from datetime import datetime
from typing import List
from sqlalchemy import ( Boolean, Column, String, Text, Date, DateTime, ForeignKey, Integer,)
from sqlalchemy.orm import declarative_base, relationship
Base = declarative_base()

class Factions(Base):
 __tablename__ = "factions"
 id = Column(String, primary_key=True, comment="Faction identifier")
 name = Column(String, nullable=False, comment="Faction name")
 link = Column(String,comment="Link to the faction page on the Wahapedia website",)
 # Relationships
 datasheets = relationship("Datasheets", back_populates="faction")
 stratagems = relationship("Stratagems", back_populates="faction")
 abilities = relationship("Abilities", back_populates="faction")
 enhancements = relationship("Enhancements", back_populates="faction")
 detachment_abilities = relationship( "DetachmentAbilities", back_populates="faction", )
 detachments = relationship("Detachments", back_populates="faction")

class Source(Base):
 __tablename__ = "sources"
 id = Column(String, primary_key=True, comment="Add-on identifier")
 name = Column(String, nullable=False, comment="Add-on name")
 type = Column(String, comment='Add-on type ("Index", "Supplement", etc.)')
 edition = Column(String, comment="Edition number")
 version = Column(String, comment="Errata version number")
 errata_date = Column(Date, comment="Date of the latest errata or announcement/release", )
 errata_link = Column(String, comment="Link to errata/source on GW website")
 # Relationships
 datasheets = relationship("Datasheets", back_populates="source")

class Datasheets(Base):
 __tablename__ = "datasheets"
 id = Column(String, primary_key=True, comment="Datasheet identifier")
 name = Column(String, nullable=False, comment="Datasheet name")
 faction_id = Column( String, ForeignKey("factions.id"), nullable=False, index=True, )
 source_id = Column(String, ForeignKey("sources.id"), nullable=False, index=True)
 legend = Column(Text, comment="Datasheet's background")
 role = Column(String, comment="Datasheet's Battlefield Role")
 loadout = Column(Text, comment="Datasheet loadout")
 transport = Column(Text, comment="Transport capacity (if it is a TRANSPORT)")
 virtual = Column( Boolean, comment="Virtual datasheets not present in army list", )
 leader_head = Column(Text, comment="Leader section header commentary")
 leader_footer = Column(Text, comment="Leader section footer commentary")
 damaged_w = Column(String, comment="Remaining Wounds count")
 damaged_description = Column(Text, comment="Remaining Wounds description")
 link = Column(String, comment="Link to datasheet on the Wahapedia website")
 # Relationships
 faction = relationship("Factions", back_populates="datasheets")
 source = relationship("Source", back_populates="datasheets")
 abilities = relationship("DatasheetsAbilities", back_populates="datasheet")
 keywords = relationship("DatasheetsKeywords", back_populates="datasheet")
 models = relationship("DatasheetsModels", back_populates="datasheet")
 options = relationship("DatasheetsOptions", back_populates="datasheet")
 wargear = relationship("DatasheetsWargear", back_populates="datasheet")
 unit_composition = relationship("DatasheetsUnitComposition", back_populates="datasheet", )
 models_cost = relationship("DatasheetsModelsCost", back_populates="datasheet")
 stratagems = relationship( "DatasheetsStratagems", back_populates="datasheet", )
 enhancements = relationship( "DatasheetsEnhancements", back_populates="datasheet", )
 detachment_abilities = relationship( "DatasheetsDetachmentAbilities", back_populates="datasheet", )
 leaders = relationship( "DatasheetsLeader", back_populates="datasheet", foreign_keys="DatasheetsLeader.datasheet_id", )
 attached_to = relationship( "DatasheetsLeader", back_populates="attached_datasheet", foreign_keys="DatasheetsLeader.attached_datasheet_id", )

class DatasheetsAbilities(Base):
 __tablename__ = "datasheets_abilities"
 datasheet_id = Column( String, ForeignKey("datasheets.id"), primary_key=True, index=True, )
 line = Column(String, primary_key=True, comment="Line number in the table")
 ability_id = Column( String, ForeignKey("abilities.id"), nullable=True, index=True, comment="Ability ID (link to Abilities table)", )
 model = Column( String, comment="Belonging of this ability to a specific model", )
 name = Column(String, comment="Ability name")
 description = Column(Text, comment="Ability description")
 type = Column(String, comment="Ability type")
 parameter = Column(String, comment="Ability parameter")
 # Relationships
 datasheet = relationship("Datasheets", back_populates="abilities")
 ability = relationship("Abilities")

class DatasheetsKeywords(Base):
 __tablename__ = "datasheets_keywords"
 datasheet_id = Column( String, ForeignKey("datasheets.id"), primary_key=True, index=True, )
 keyword = Column(String, primary_key=True, comment="Datasheet keyword")
 model = Column( String, comment="Belonging of this keyword to a specific model", )
 is_faction_keyword = Column( Boolean, comment="This is a Faction Keyword", )
 # Relationships
 datasheet = relationship("Datasheets", back_populates="keywords")

class DatasheetsModels(Base):
 __tablename__ = "datasheets_models"
 datasheet_id = Column( String, ForeignKey("datasheets.id"), primary_key=True, index=True, )
 line = Column(String, primary_key=True, comment="Line number in the table")
 name = Column(String, nullable=False, comment="Model name")
 M = Column(String, comment="Move characteristic")
 T = Column(String, comment="Toughness characteristic")
 Sv = Column(String, comment="Save characteristic")
 inv_sv = Column(String, comment="Invulnerable Save characteristic")
 inv_sv_descr = Column(Text, comment="Invulnerable Save commentary")
 W = Column(String, comment="Wounds characteristic")
 Ld = Column(String, comment="Leadership characteristic")
 OC = Column(String, comment="Objective Control characteristic")
 base_size = Column(String, comment="Model base size")
 base_size_descr = Column(Text, comment="Model base size commentary")
 # Relationships
 datasheet = relationship("Datasheets", back_populates="models")

class DatasheetsOptions(Base):
 __tablename__ = "datasheets_options"
 datasheet_id = Column( String, ForeignKey("datasheets.id"), primary_key=True, index=True, )
 line = Column(String, primary_key=True, comment="Line number in the table")
 button = Column(String, comment="Decorative symbol at the beginning")
 description = Column(Text, comment="Wargear option description")
 # Relationships
 datasheet = relationship("Datasheets", back_populates="options")

class DatasheetsWargear(Base):
 __tablename__ = "datasheets_wargear"
 datasheet_id = Column( String, ForeignKey("datasheets.id"), primary_key=True, index=True, )
 line = Column(String, primary_key=True, comment="Line number in the table")
 line_in_wargear = Column( String, comment="Line number in Wargear table for sorting", )
 dice = Column(String, comment="Dice result required (see Bubblechukka)")
 name = Column(String, comment="Wargear name")
 description = Column(Text, comment="Wargear rules")
 range = Column(String, comment="Range characteristic")
 type = Column(String, comment='Type characteristic ("Melee", "Range")')
 A = Column(String, comment="Attacks characteristic")
 BS_WS = Column(String, comment="Ballistic/Weapon Skill characteristic")
 S = Column(String, comment="Strength characteristic")
 AP = Column(String, comment="Armour Penetration characteristic")
 D = Column(String, comment="Damage characteristic")
 # Relationships
 datasheet = relationship("Datasheets", back_populates="wargear")

class DatasheetsUnitComposition(Base):
 __tablename__ = "datasheets_unit_composition"
 datasheet_id = Column( String, ForeignKey("datasheets.id"), primary_key=True, index=True, )
 line = Column(String, primary_key=True, comment="Line number in the table")
 description = Column(Text, comment="Unit composition")
 # Relationships
 datasheet = relationship("Datasheets", back_populates="unit_composition")

class DatasheetsModelsCost(Base):
 __tablename__ = "datasheets_models_cost"
 datasheet_id = Column( String, ForeignKey("datasheets.id"), primary_key=True, index=True, )
 line = Column(String, primary_key=True, comment="Line number in the table")
 description = Column(Text, comment="Model description")
 cost = Column(String, comment="Model cost")
 # Relationships
 datasheet = relationship("Datasheets", back_populates="models_cost")

class DatasheetsStratagems(Base):
 __tablename__ = "datasheets_stratagems"
 datasheet_id = Column( String, ForeignKey("datasheets.id"), primary_key=True, index=True, )
 stratagem_id = Column( String, ForeignKey("stratagems.id"), primary_key=True, index=True, )
 # Relationships
 datasheet = relationship("Datasheets", back_populates="stratagems")
 stratagem = relationship("Stratagems")

class DatasheetsEnhancements(Base):
 __tablename__ = "datasheets_enhancements"
 datasheet_id = Column( String, ForeignKey("datasheets.id"), primary_key=True, index=True, )
 enhancement_id = Column( String, ForeignKey("enhancements.id"), primary_key=True, index=True, )
 # Relationships
 datasheet = relationship("Datasheets", back_populates="enhancements")
 enhancement = relationship("Enhancements")

class DatasheetsDetachmentAbilities(Base):
 __tablename__ = "datasheets_detachment_abilities"
 datasheet_id = Column( String, ForeignKey("datasheets.id"), primary_key=True, index=True, )
 detachment_ability_id = Column( String, ForeignKey("detachment_abilities.id"), primary_key=True, index=True, )
 # Relationships
 datasheet = relationship("Datasheets", back_populates="detachment_abilities")
 detachment_ability = relationship("DetachmentAbilities")

class DatasheetsLeader(Base):
 __tablename__ = "datasheets_leader"
 datasheet_id = Column( String, ForeignKey("datasheets.id"), primary_key=True, index=True, comment="Datasheet identifier", )
 attached_datasheet_id = Column( String, ForeignKey("datasheets.id"), primary_key=True, index=True, comment="Attached datasheet identifier", )
 # Relationships
 datasheet = relationship("Datasheets", back_populates="leaders", foreign_keys=[datasheet_id], )
 attached_datasheet = relationship("Datasheets", back_populates="attached_to", foreign_keys=[attached_datasheet_id], )

class Stratagems(Base):
 __tablename__ = "stratagems"
 id = Column(String, primary_key=True, comment="Stratagem identifier")
 faction_id = Column( String, ForeignKey("factions.id"), nullable=False, index=True, )
 name = Column(String, nullable=False, comment="Stratagem name")
 type = Column( String, comment="Stratagem type (eg Shield Host – Strategic Ploy Stratagem)", )
 cp_cost = Column(String, comment="Stratagem command point cost")
 legend = Column(Text, comment="Stratagem background")
 turn = Column(String, comment="Stratagem turn")
 phase = Column(String, comment="Stratagem phase")
 description = Column(Text, comment="Stratagem description")
 detachment = Column(String, comment="Detachment name")
 detachment_id = Column( String, ForeignKey("detachments.id"), nullable=True, index=True, )
 # Relationships
 faction = relationship("Factions", back_populates="stratagems")
 detachment = relationship("Detachments")

class Abilities(Base):
 __tablename__ = "abilities"
 id = Column(String, primary_key=True, comment="Abilities identifier")
 name = Column(String, nullable=False, comment="Ability name")
 legend = Column(Text, comment="Ability background")
 faction_id = Column( String, ForeignKey("factions.id"), nullable=False, index=True, )
 description = Column(Text, comment="Ability description")
 # Relationships
 faction = relationship("Factions", back_populates="abilities")

class Enhancements(Base):
 __tablename__ = "enhancements"
 id = Column(String, primary_key=True, comment="Enhancements identifier")
 faction_id = Column( String, ForeignKey("factions.id"), nullable=False, index=True, )
 name = Column(String, nullable=False, comment="Enhancement name")
 legend = Column(Text, comment="Enhancement legend")
 description = Column(Text, comment="Enhancement description")
 cost = Column(String, comment="Enhancement points cost")
 detachment = Column(String, comment="Detachment name")
 detachment_id = Column( String, ForeignKey("detachments.id"), nullable=True, index=True, )
 # Relationships
 faction = relationship("Factions", back_populates="enhancements")
 detachment = relationship("Detachments")

class DetachmentAbilities(Base):
 __tablename__ = "detachment_abilities"
 id = Column( String, primary_key=True, comment="Detachment abilities identifier", )
 faction_id = Column( String, ForeignKey("factions.id"), nullable=False, index=True, )
 name = Column(String, nullable=False, comment="Detachment ability name")
 legend = Column(Text, comment="Detachment ability legend")
 description = Column(Text, comment="Detachment ability description")
 detachment = Column(String, comment="Detachment name")
 detachment_id = Column( String, ForeignKey("detachments.id"), nullable=True, index=True, )
 # Relationships
 faction = relationship("Factions", back_populates="detachment_abilities")
 detachment = relationship("Detachments")

class Detachments(Base):
 __tablename__ = "detachments"
 id = Column(String, primary_key=True, comment="Detachment identifier")
 faction_id = Column( String, ForeignKey("factions.id"), nullable=False, index=True, )
 name = Column(String, nullable=False, comment="Detachment name")
 legend = Column(Text, comment="Detachment legend")
 type = Column(String, comment='Detachment type (e.g. "Boarding Action")')
 # Relationships
 faction = relationship("Factions", back_populates="detachments")

class LastUpdate(Base):
 __tablename__ = "last_update"
 id = Column( Integer, primary_key=True, comment="Single row table, always id=1", )
 last_update = Column( DateTime, nullable=False, comment="Date-time of last export data update (GMT+3)", )
