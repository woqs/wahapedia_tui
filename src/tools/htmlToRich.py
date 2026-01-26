from bs4 import BeautifulSoup, NavigableString, Tag
from rich.text import Text


def html_to_rich(html: str) -> Text:
    soup = BeautifulSoup(html, "html.parser")
    rich_text = Text()

    def walk(node):
        if isinstance(node, NavigableString):
            rich_text.append(str(node))
        elif isinstance(node, Tag):
            if node.name == "a" and node.get("href"):
                start = len(rich_text)
                rich_text.append(node.get_text())
                rich_text.stylize(
                    f"link {node['href']}",
                    start,
                    len(rich_text),
                )
            else:
                for child in node.children:
                    walk(child)

    for child in soup.contents:
        walk(child)

    return rich_text