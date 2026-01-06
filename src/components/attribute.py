from textual.containers import Vertical
from textual.widgets import Static

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
