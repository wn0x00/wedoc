import os
import tempfile
import unittest

from dotenv import load_dotenv
from wedoc import WedocClient


class WedocClientBase(unittest.TestCase):
    def setUp(self) -> None:
        ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        env_path = os.path.join(ROOT_PATH, ".env")
        load_dotenv(env_path)
        corpid = os.environ.get("corpid")
        corpsecret = os.environ.get("corpsecret")
        docid = os.environ.get("docid")
        client = WedocClient(corpid=corpid, corpsecret=corpsecret)
        self.client = client
        self.wb = client.workbook(docid)

    def tearDown(self):
        tmp_path = tempfile.gettempdir()
        wework_app_token_path = os.path.join(tmp_path, "wework_app_token")
        os.remove(wework_app_token_path)

    def test_init_wndocclient(self):
        pass

    def test_get_sheet_properties(self):
        pass

    def test_get_sheet_names(self):
        pass

    def test_set_cell(self):
        res = self.wb.set_cell(1, "A", "wn0x00")
        print(res)

    def test_set_row(self):
        res = self.wb.set_row(1, ["1", "2"], "A")
        print(res)

    def test_set_columns(self):
        res = self.wb.set_column("A", ["1", "2"], 1)
        print(res)

    def test_set_range(self):
        res = self.wb.set_range(1, "A", [["1", "2"], ["1", "2"]])
        print(res)

    def test_get_cell(self):
        res = self.wb.get_cell("1", "A")
        print(res)

    def test_get_row(self):
        res = self.wb.get_row(1)
        print(res)

    def test_get_column(self):
        res = self.wb.get_column("A")
        print(res)

    def test_get_range(self):
        res = self.wb.get_range("A1:B2")
        print(res)


if __name__ == "__main__":
    unittest.main()
