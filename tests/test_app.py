import os

from dotenv import load_dotenv
from wedoc import WedocClient


if __name__ == "__main__":

    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_path = os.path.join(ROOT_PATH, ".env")
    load_dotenv(env_path)
    corpid = os.environ.get("corpid")
    corpsecret = os.environ.get("corpsecret")
