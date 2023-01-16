import os
import json
import requests
import tempfile
import inspect

from wedoc.api.base import WedocApiBase


def _is_api_endpoint(obj):
    return isinstance(obj, WedocApiBase)


class WedocClientBase:
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        api_endpoints = inspect.getmembers(self, _is_api_endpoint)
        for name, api in api_endpoints:
            api_cls = type(api)
            api = api_cls(client=self)
            setattr(self, name, api)
        return self

    def __init__(self, corpid, corpsecret) -> None:
        self.base_url = "https://qyapi.weixin.qq.com/cgi-bin"
        self.corpid = corpid
        self.corpsecret = corpsecret
        self.access_token = self.get_local_session()

    def get_local_session(self):
        """创建企业微信应用 access_token 缓存"""
        tmp_path = tempfile.gettempdir()
        wework_app_token_path = os.path.join(tmp_path, "wework_app_token")

        if not os.path.exists(wework_app_token_path):
            access_token = self.get_access_token().get("access_token")
            token_dict = {"access_token": access_token}
            with open(wework_app_token_path, "w") as f:
                json.dump(token_dict, f)
        with open(wework_app_token_path) as f:
            token_dict = json.load(f)
            if token_dict.get("access_token"):
                return token_dict.get("access_token")

    def get_access_token(self):
        """获取企业微信应用的 access_token"""
        url = f"{self.base_url}/gettoken?corpid={self.corpid}&corpsecret={self.corpsecret}"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()

    def request(self, method, api, params="", pyload={}):
        """发送请求"""
        url = f"{self.base_url}{api}?access_token={self.access_token}"
        headers = {"Content-Type": "application/json"}
        res = requests.request(
            method, url, params=params, data=json.dumps(pyload), headers=headers
        )
        return res.json()


if __name__ == "__main__":
    pass
