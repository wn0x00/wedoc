import os
from dotenv import load_dotenv

from wedoc import WedocClient


ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(ROOT_PATH, ".env")
load_dotenv(env_path)
corpid = os.environ.get("corpid")
corpsecret = os.environ.get("corpsecret")
docid = os.environ.get("docid")
client = WedocClient(corpid=corpid, corpsecret=corpsecret)

wb = client.workbook(docid)

res = wb.get_row(1)
print(res)
