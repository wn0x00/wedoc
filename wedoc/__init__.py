from wedoc.api import Document
from wedoc.api import Spreadsheet
from wedoc.client import WedocClientBase


class WedocClient(WedocClientBase):
    doc: Document = Document()
    workbook: Spreadsheet = Spreadsheet()

    def __init__(self, corpid, corpsecret) -> None:
        """
        对企业微信自建应用初始化

        :param corpid: 企业 ID 标识
        :param corpsecret: 企业自建应用密钥

        使用示例::

        >>> from wedoc import WedocClient
        >>> client = WedocClient("corpid", "corpsecret")
        >>> client.doc.create_doc("doc_name", "doc_type")
        """
        super().__init__(corpid, corpsecret)
