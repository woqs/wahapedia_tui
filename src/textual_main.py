from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Select
import db
import models

from typing import Callable

map_factions: Callable[[models.Factions], str] = lambda f: f.id + " " + f.name

class WahapediaTUI(App):
    FACTION_COLORS = [
        {},
        {},
        {},
        {},
        {},
        {},
        {},
        {},
    ]

    def on_mount(self) -> None:
        self.screen.styles.background = "darkblue"

    def compose(self) -> ComposeResult:
        factions = db.get_faction_list()
        yield Select.from_values(map(map_factions, factions))

    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        self.title = str(event.value)
#        self.screen.styles.background = ""
