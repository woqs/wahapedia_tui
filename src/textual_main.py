from textual import on
from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Select, ListView, Input
from widgets import DatasheetLabel
from panel_datasheet import DatasheetPanel
import re
import db
import models


class LeftPanel(Widget):
    DEFAULT_CSS = """
LeftPanel {
    height: 1fr;
    width: 0.2fr;
}
"""

    datasheetListView = ListView()
    searchInput = Input(placeholder="Search unit", type="text")
    sheetList = ()

    def compose(self):
        factions = db.get_faction_list()
        yield Select((f.name, f.id) for f in factions)
        yield self.searchInput
        yield self.datasheetListView

    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        self.sheetList = db.get_datasheets_for_faction(str(event.value))
        self.datasheetListView.clear()
        for sheet in self.sheetList:
            self.datasheetListView.append(
                DatasheetLabel(sheet)
            )

    @on(Input.Changed)
    def on_input_change(self, event: Input.Changed) -> None:
        self.datasheetListView.clear()
        for sheet in filter(lambda s: bool(re.match('.*'+event.value+'.*', s.name)), self.sheetList):
            self.datasheetListView.append(
                DatasheetLabel(sheet)
            )


class MainPanel(Widget):
    DEFAULT_CSS = """
MainPanel {
    layout: horizontal;
    height: 1fr;
    width: 1fr;
}
"""
    leftPanel = LeftPanel()
    rightPanel = DatasheetPanel()

    def compose(self):
        yield self.leftPanel
        yield self.rightPanel
    
    @on(ListView.Selected)
    def on_list_view_selected(self, event: ListView.Selected) -> None:
        self.rightPanel.sheet = event.item.sheet


class WahapediaTUI(App):

    def on_mount(self) -> None:
        self.screen.styles.background = "darkblue"

    def compose(self) -> ComposeResult:
        yield MainPanel()
