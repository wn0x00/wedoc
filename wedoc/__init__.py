import os
import json
import requests
import tempfile


from .exception import WeworkError


class WedocClient:
    def __init__(self, corpid, corpsecret) -> None:
        self.base_url = "https://qyapi.weixin.qq.com/cgi-bin"
        self.access_token = ""
        self.corpid = corpid
        self.corpsecret = corpsecret

    def get_crop_access_token(self):
        """获取企业微信应用的 access_token"""
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.corpid}&corpsecret={self.corpsecret}"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()

    def cache():
        """创建企业微信应用 access_token 缓存"""
        tmp_path = tempfile.gettempdir()
        wework_app_token_path = os.path.join(tmp_path, "wework_app_token")

        if not os.path.exists(wework_app_token_path):
            token_dict = {"access_token": ""}
            with open(wework_app_token_path, "w") as f:
                json.dump(token_dict, f)
        with open(wework_app_token_path) as f:
            token_dict = json.load(f)
            if token_dict.get("access_token"):
                return token_dict.get("access_token")

    def request(self, method, api, params=None, pyload={}):
        """发送请求"""
        url = f"{self.base_url}{api}?access_token={self.access_token}"
        headers = {"Content-Type": "application/json"}
        res = requests.request(
            method, url, params=params, data=json.dumps(pyload), headers=headers
        )
        return res.json()


if __name__ == "__main__":
    pass
