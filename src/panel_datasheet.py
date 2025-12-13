from textual import on
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Static, ListView, Label, ListItem, Placeholder
import models

class Header(Widget):
    DEFAULT_CSS = """
Header {
    height: 3;
    dock: top;
    width: 100%;
}
"""

    text = Static("Wahapedia TUI")
    def compose(self):
        yield self.text


class DatasheetPanel(Widget):
    DEFAULT_CSS = """
DatasheetPanel {
    height: 1fr;
    width: 0.8fr;
}
"""
    sheet: reactive[models.Datasheets | None] = reactive(None)
    header = Header()

    def compose(self):
        yield self.header

    def watch_sheet(self, sheet: models.Datasheets | None) -> None :
        if sheet is not None:
            self.header.text.content = sheet.name
