from textual.containers import Horizontal
from textual.widgets import Static
import models
from components.attribute import Attribute

class Model(Horizontal):
    DEFAULT_CSS = """
Model {
    width: 100%;
    height: auto;
}
Model > Static {
    max-width: 20;
}
"""
    model: models.DatasheetsModels
    moveAttribute: Attribute
    tAttribute: Attribute
    svAttribute: Attribute
    isvAttribute: Attribute
    wAttribute: Attribute
    ldAttribute: Attribute
    ocAttribute: Attribute

    def __init__(self, model: models.DatasheetsModels):
        super().__init__()
        self.model = model
        self.moveAttribute = Attribute("M", model.M)
        self.tAttribute = Attribute("T", model.T)
        self.svAttribute = Attribute("Sv", model.Sv)
        self.isvAttribute = Attribute("ISv", model.inv_sv)
        self.wAttribute = Attribute("W", model.W)
        self.ldAttribute = Attribute("Ld", model.Ld)
        self.ocAttribute = Attribute("Oc", model.OC)

    def compose(self):
        yield Static(self.model.name)
        yield self.moveAttribute
        yield self.tAttribute
        yield self.svAttribute
        yield self.isvAttribute
        yield self.wAttribute
        yield self.ldAttribute
        yield self.ocAttribute
