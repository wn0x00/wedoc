import os
import json
import requests
import tempfile


from .exception import WeworkError


class Application:
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


class Document:
    def __init__(self) -> None:
        self.app = Application()

    def create_doc(self):
        """创建文档"""
        api = "/wedoc/create_doc"
        pyload = {
            "spaceid": "SPACEID",
            "fatherid": "FATHERID",
            "doc_type": "DOC_TYPE",
            "doc_name": "DOC_NAME",
            "admin_users": ["USERID1", "USERID2", "USERID3"],
        }

        res = self.app.request("post", api, pyload)
        return res

    def rename_doc(self, docid, new_name):
        """重命名文档"""
        api = "/wedoc/rename_doc"
        pyload = {"docid": docid, "new_name": new_name}
        res = self.app.request("post", api, pyload)
        return res

    def del_doc(self, docid):
        """删除文档"""
        api = "/wedoc/del_doc"
        pyload = {"docid": docid}
        res = self.app.request("post", api, pyload)
        return res

    def get_doc_base_info(self, docid):
        """获取文档基础信息"""
        api = "/wedoc/get_doc_base_info"
        pyload = {"docid": docid}
        res = self.app.request("post", api, pyload)
        return res


class Spreadsheet:
    def __init__(self) -> None:
        self.app = Application()

    def get_sheet_properties(self, docid):
        """获取表格行列信息"""
        api = "/wedoc/spreadsheet/get_sheet_properties"
        pyload = {"docid": docid}
        res = self.app.request("post", api, pyload)
        return res

    def get_sheet_range_data(self, docid, sheet_id, range):
        """获取表格数据"""
        api = "/wedoc/spreadsheet/get_sheet_range_data"
        pyload = {"docid": docid, "sheet_id": sheet_id, "range": range}
        res = self.app.request("post", api, pyload)
        return res

    def batch_update(self, docid):
        """编辑表格内容"""
        api = "/wedoc/spreadsheet/get_sheet_range_data"
        pyload = {
            "docid": docid,
            "requests": [
                {"add_sheet_request": {...}},
                {"update_range_request": {...}},
                {"delete_dimension_request": {...}},
                {"delete_sheet_request": {...}},
            ],
        }
        res = self.app.request("post", api, pyload)
        return res


if __name__ == "__main__":
    pass
