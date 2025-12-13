from textual.app import ComposeResult
from textual.widgets import Label, ListItem
import models

class DatasheetLabel(ListItem):
    sheet: models.Datasheets

    def __init__(self, sheet: models.Datasheet) -> None:
        super().__init__()
        self.label = sheet.name
        self.sheet = sheet

    def compose( self ) -> ComposeResult:
        yield Label(self.label)
