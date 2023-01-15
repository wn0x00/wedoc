from wedoc.api import Document
from wedoc.api import Spreadsheet
from wedoc.client import WedocClientBase


class WedocClient(WedocClientBase):
    doc = Document()
    wb = Spreadsheet()

    def __init__(self, corpid, corpsecret) -> None:
        super().__init__(corpid, corpsecret)
