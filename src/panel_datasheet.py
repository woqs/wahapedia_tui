from textual import on
from textual.containers import VerticalScroll, Horizontal, Vertical
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Static, ListView, Label, ListItem
import models
from db import get_models_from_sheet
import logging


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

class Attribute(Vertical):
    DEFAULT_CSS = """
Attribute {
    height: auto;
    min-width: 5;
    max-width: 5;
    content-align: center middle;
    border: solid white;
}
"""

    title: Static
    valueStatic: Static

    def __init__(self, title, value):
        super().__init__()
        self.title = Static(title, expand = True)
        self.valueStatic = Static(str(value), expand = True)

    def compose(self):
        yield self.title
        yield self.valueStatic

class Model(Horizontal):
    DEFAULT_CSS = """
Model {
    width: 100%;
    height: auto;
    border: solid white;
}
Model > Static {
    max-width: 20;
}
"""
    model: models.DatasheetsModels
    moveAttribute: Attribute
    tAttribute: Attribute
    sv: Attribute

    def __init__(self, model: models.DatasheetsModels):
        super().__init__()
        self.model = model
        self.moveAttribute = Attribute("M", model.M)
        self.tAttribute = Attribute("T", model.T)
        self.sv = Attribute("Sv", model.Sv)

    def compose(self):
        yield Static(self.model.name)
        yield self.moveAttribute
        yield self.tAttribute
        yield self.sv

class DatasheetPanel(Widget):
    DEFAULT_CSS = """
DatasheetPanel {
    height: 1fr;
    width: 0.8fr;
    background: blue;
}
"""
    sheet: reactive[models.Datasheets | None] = reactive(None)
    text: Header
    modelList: VerticalScroll

    def __init__(self):
        super().__init__()
        self.text = Header("Wahapedia TUI")
        self.modelList = VerticalScroll()

    def compose(self):
        yield self.text
        yield self.modelList

    async def watch_sheet(self, sheet: models.Datasheets | None) -> None :
        if sheet is not None:
            logger = logging.getLogger()
            fh = logging.FileHandler('spam.log')
            fh.setLevel(logging.ERROR)
            logger.addHandler(fh)

            for model in get_models_from_sheet(sheet):
                logger.error(model.name)

#            self.styles.background = "white"
            self.text.update(sheet.name)
            await self.modelList.remove_children()

            await self.modelList.mount(
                *[Model(model) for model in get_models_from_sheet(sheet)]
            )
