from textual.containers import VerticalScroll, Horizontal, Vertical
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Static, ListView, Label, ListItem
import models
from db import get_models_enriched_sheet
from components.model import Model


class Header(Static):
    DEFAULT_CSS = """
Header {
    height: 3;
    dock: top;
    width: 100%;
    content-align: center middle;
    color: white;
    border: double white;
}
"""

class DatasheetPanel(Widget):
    DEFAULT_CSS = """
DatasheetPanel {
    height: 1fr;
    width: 0.8fr;
    background: blue;
}
"""
    sheet: reactive[models.Datasheets | None] = reactive(None)
    header: Header
    modelList: Vertical

    def __init__(self):
        super().__init__()
        self.header = Header("Wahapedia TUI")
        self.modelList = Vertical()

    def compose(self):
        yield self.header
        yield self.modelList

    async def watch_sheet(self, sheet: models.Datasheets | None) -> None :
        if sheet is not None:
#            self.styles.background = "white"
            self.header.update(sheet.name)
            await self.modelList.remove_children()

            sheet = get_models_enriched_sheet(sheet)
            await self.modelList.mount(
                *[Model(model) for model in sheet.models]
            )
