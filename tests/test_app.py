import os
import unittest

from dotenv import load_dotenv
from wedoc import WedocClient


class WedocClientBase(unittest.TestCase):
    def test_init_wndocclient(self):
        ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        env_path = os.path.join(ROOT_PATH, ".env")
        load_dotenv(env_path)
        corpid = os.environ.get("corpid")
        corpsecret = os.environ.get("corpsecret")
        client = WedocClient(corpid=corpid, corpsecret=corpsecret)
        res = client.get_crop_access_token()
        print(res)
