from textual.containers import VerticalScroll
from textual.widgets import Static
from tools.htmlToRich import html_to_rich


class ContentElement():
    name: str
    description: str
    def __init__(self, name, description):
        self.description = description
        self.name = name

class NameStatic(Static):
    DEFAULT_CSS = """
NameStatic {
    text-style: bold;
}
"""

class Abilities(VerticalScroll):
    DEFAULT_CSS = """
Abilities {
    height: 0.3fr;
}
Abilities > .title {
    text-style: bold underline;
}
"""

    title: Static
    content: list[ContentElement]

    def __init__(self, title: str, content: list[ContentElement]):
        super().__init__()
        self.title = Static(title, classes="title")
        self.content = content

    def compose(self):
        yield self.title
        for content in self.content:
            if content.name != "" and content.name is not None:
                yield NameStatic(content.name or "")
                yield Static(html_to_rich(content.description or ""))
