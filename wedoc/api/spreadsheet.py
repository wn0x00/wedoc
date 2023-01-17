from wedoc.api.base import WedocApiBase
from wedoc.utils import column_index_from_string, get_column_letter


class Spreadsheet(WedocApiBase):
    def __init__(self, docid: str = None, client: object = None) -> None:
        super().__init__(client)
        self.docid = docid
        self.sheet_metadata = None

    def get_sheet_properties(self) -> dict:
        """
        获取表格行列信息

        使用示例

        >>> from wedoc import WedocClient
        >>> client = WedocClient("corpid", "corpsecret")
        >>> wb = client.workbook("docid")
        >>> wb.get_sheet_properties()
        """

        api = "/wedoc/spreadsheet/get_sheet_properties"
        pyload = {"docid": self.docid}
        res = self.request("post", api, pyload=pyload)
        return res.get("properties")

    def get_sheet_property(self, sheet_id: str, property: str):
        """
        通过 sheet_id 找到 sheet 页对应的属性

        :param sheet_id:
        :param property:
        :return:
        """
        for item in self.sheet_metadata:
            if item.get("sheet_id") == sheet_id:
                return item.get(property)
        else:
            raise ValueError("找不到 %s sheet_id 对应的 sheet 页" % property)

    def get_sheet_range_data(self, pyload):
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
        res = self.request("post", api, pyload=pyload)
        return res

    def batch_update(self, pyload):
        """
        编辑表格内容
        :param docid:
        :return:

        使用示例

        >>> from wedoc import WedocClient
        >>> client = WedocClient("corpid", "corpsecret")
        >>> client.wb.batch_update("docid")
        """

        api = "/wedoc/spreadsheet/batch_update"

        res = self.request("post", api, pyload=pyload)
        return res

    def get_sheet_names(self) -> list:
        """
        获取所有的 sheet 页数据
        :return:
        """
        res = self.get_sheet_properties()
        return [item.get("title") for item in res]

    def get_active_sheet(self) -> str:
        res = self.get_sheet_properties()
        return [item.get("title") for item in res][0]

    def get_sheet_id(self, sheet_name):
        for item in self.sheet_metadata:
            if item.get("title") == sheet_name:
                return item.get("sheet_id")
        else:
            raise ValueError("找不到 s% sheet 页" % sheet_name)

    def add_sheet(
        self, sheet_name: str, row_count: int = 10, column_count: int = 10
    ) -> dict:
        """
        添加 sheet 页
        :param docid: str,
        :param sheet_name: str,
        :param row_count: int = 10,
        :param column_count: int = 10,
        :return:

        """
        pyload = {
            "docid": self.docid,
            "requests": [
                {
                    "add_sheet_request": {
                        "title": sheet_name,
                        "row_count": row_count,
                        "column_count": column_count,
                    }
                },
            ],
        }
        res = self.batch_update(pyload=pyload)
        self.sheet_metadata = self.get_sheet_properties()
        return res

    def delete_sheet(self, sheet_name: str) -> dict:
        """
        删除 sheet 页
        :param sheet_id: str
        :retrun:
        """

        sheet_id = self.get_sheet_id(sheet_name=sheet_name)
        pyload = {
            "docid": self.docid,
            "requests": [
                {"delete_sheet_request": {"sheet_id": sheet_id}},
            ],
        }
        res = self.batch_update(pyload=pyload)
        self.sheet_metadata = self.get_sheet_properties()
        return res

    def rename_sheet(self):
        """
        重命名 sheet 页, 暂不支持
        """
        pass

    def get_row_count(self, sheet_name: str = None):
        """
        获取总行数
        :param sheet_name: str
        :return: int
        """
        sheet_name = sheet_name if sheet_name else self.get_active_sheet()
        sheet_id = self.get_sheet_id(sheet_name)

        for item in self.sheet_metadata:
            if item.get("sheet_id") == sheet_id:
                return item.get("row_count")

    def get_column_count(self, sheet_name=None):
        """
        获取总列数
        :param sheet_name: str
        :return: int
        """
        sheet_name = sheet_name if sheet_name else self.get_active_sheet()
        sheet_id = self.get_sheet_id(sheet_name)

        for item in self.sheet_metadata:
            if item.get("sheet_id") == sheet_id:
                return item.get("column_count")

    def get_cell(self, row, column, sheet_name=None):
        """
        读取单元格
        :param row:
        :param column:
        :param sheet_name:
        """
        sheet_name = sheet_name if sheet_name else self.get_active_sheet()
        sheet_id = self.get_sheet_id(sheet_name)
        pyload = {
            "docid": self.docid,
            "sheet_id": sheet_id,
            "range": f"{column}{row}:{column}{row}",
        }
        res = self.get_sheet_range_data(pyload=pyload)
        return res

    def set_cell(self, row, column, value, sheet_name=None):
        """
        设置单元格数据

        :param row:
        :param column:
        :param value:
        :param sheet_name:
        :return:

        """
        sheet_name = sheet_name if sheet_name else self.get_active_sheet()
        sheet_id = self.get_sheet_id(sheet_name)
        pyload = {
            "docid": self.docid,
            "requests": [
                {
                    "update_range_request": {
                        "sheet_id": sheet_id,
                        "grid_data": {
                            "start_row": int(row) - 1,
                            "start_column": column_index_from_string(column) - 1,
                            "rows": [{"values": [{"cell_value": {"text": value}}]}],
                        },
                    }
                },
            ],
        }
        res = self.batch_update(pyload)
        return res

    def get_range(self, des_range, sheet_name=None):
        """
        读取区域数据
        """
        sheet_name = sheet_name if sheet_name else self.get_active_sheet()
        sheet_id = self.get_sheet_id(sheet_name)
        pyload = {"docid": self.docid, "sheet_id": sheet_id, "range": des_range}
        res = self.get_sheet_range_data(pyload=pyload)
        return res

    def set_range(self, sheet_name=None):
        """
        读取区域数据
        """
        pass

    def set_row(self):
        pass

    def set_column(self):
        pass

    def get_row(self, row, sheet_name=None) -> list:
        """
        读取行内容
        """
        sheet_name = sheet_name if sheet_name else self.get_active_sheet()
        sheet_id = self.get_sheet_id(sheet_name)
        column_count = self.get_sheet_property(sheet_id, "column_count")

        if column_count == 0:
            return []

        pyload = {
            "docid": self.docid,
            "sheet_id": sheet_id,
            "range": f"A{row}:{get_column_letter(column_count)}{row}",
        }
        res = self.get_sheet_range_data(pyload=pyload)
        return res

    def get_column(self, column, sheet_name=None):
        sheet_name = sheet_name if sheet_name else self.get_active_sheet()
        sheet_id = self.get_sheet_id(sheet_name)
        row_count = self.get_sheet_property(sheet_id, "row_count")
        if row_count == 0:
            return []

        pyload = {
            "docid": self.docid,
            "sheet_id": sheet_id,
            "range": f"{column}1:{column}{row_count}",
        }
        res = self.get_sheet_range_data(pyload=pyload)
        return res

    def delete_row(self, start_index, end_index, sheet_name=None):
        """
        删除行
        """
        sheet_name = sheet_name if sheet_name else self.get_active_sheet()
        sheet_id = self.get_sheet_id(sheet_name)
        pyload = {
            "docid": self.docid,
            "requests": [
                {
                    "delete_dimension_request": {
                        "sheet_id": sheet_id,
                        "dimension": "ROW",
                        "start_index": start_index,
                        "end_index": end_index,
                    }
                },
            ],
        }
        res = self.batch_update(pyload)
        return res

    def delete_column(self, start_index, end_index, sheet_name=None):
        """删除列"""
        sheet_name = sheet_name if sheet_name else self.get_active_sheet()
        sheet_id = self.get_sheet_id(sheet_name)
        pyload = {
            "docid": self.docid,
            "requests": [
                {
                    "delete_dimension_request": {
                        "sheet_id": sheet_id,
                        "dimension": "COLUMN",
                        "start_index": start_index,
                        "end_index": end_index,
                    }
                },
            ],
        }
        res = self.batch_update(pyload)
        return res

    def __call__(self, docid):
        """将表格实例化"""
        self.docid = docid
        self.sheet_metadata = self.get_sheet_properties()
        return self
