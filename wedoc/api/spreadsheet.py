class Spreadsheet:
    def __init__(self) -> None:
        pass

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
