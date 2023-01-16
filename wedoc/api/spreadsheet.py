from wedoc.api.base import WedocApiBase


class Spreadsheet(WedocApiBase):
    def get_sheet_properties(self, docid: str) -> dict:
        """
        获取表格行列信息

        :param docid:
        :return:

        使用示例

        >>> from wedoc import WedocClient
        >>> client = WedocClient("corpid", "corpsecret")
        >>> client.wb.get_sheet_properties("docid")
        """

        api = "/wedoc/spreadsheet/get_sheet_properties"
        pyload = {"docid": docid}
        res = self.request("post", api, pyload=pyload)
        return res

    def get_sheet_range_data(self, docid, sheet_id, range):
        """
        获取表格行列信息
        :param docid:
        :param sheet_id:
        :param range:
        :return:

        使用示例

        >>> from wedoc import WedocClient
        >>> client = WedocClient("corpid", "corpsecret")
        >>> client.wb.get_sheet_range_data("docid", "range")
        """
        api = "/wedoc/spreadsheet/get_sheet_range_data"
        pyload = {"docid": docid, "sheet_id": sheet_id, "range": range}
        res = self.request("post", api, pyload=pyload)
        return res

    def batch_update(self, docid):
        """
        编辑表格内容
        :param docid:
        :return:

        使用示例

        >>> from wedoc import WedocClient
        >>> client = WedocClient("corpid", "corpsecret")
        >>> client.wb.batch_update("docid")
        """

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
        res = self.request("post", api, pyload=pyload)
        return res
