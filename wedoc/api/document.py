from wedoc.api.base import WedocApiBase


class Document(WedocApiBase):
    def create_doc(
        self,
        doc_name: str,
        doc_type: int,
        spaceid: str = "",
        fatherid: str = "",
        admin_users: list = [],
    ) -> dict:
        """
        创建文档
        :param doc_name:
        :param doc_type:
        :param spaceid:
        :param fatherid:
        :param admin_users:
        :return:

        使用示例

        >>> from wedoc import WedocClient
        >>> client = WedocClient("corpid", "corpsecret")
        >>> client.doc.create_doc("doc_name", "doc_type")
        """
        api = "/wedoc/create_doc"
        pyload = {
            "doc_type": doc_type,
            "doc_name": doc_name,
            "admin_users": admin_users,
        }

        res = self.request("post", api, pyload=pyload)
        return res

    def rename_doc(self, docid: str, new_name: str) -> dict:
        """
        重命名文档

        :param doc_name:
        :param docid:
        :param new_name:
        :return:

        使用示例

        >>> from wedoc import WedocClient
        >>> client = WedocClient("corpid", "corpsecret")
        >>> client.doc.rename_doc("docid", "new_name")
        """
        api = "/wedoc/rename_doc"
        pyload = {"docid": docid, "new_name": new_name}
        res = self.request("post", api, pyload=pyload)
        return res

    def del_doc(self, docid: str) -> dict:
        """
        删除文档

        :param docid:
        :return:

        使用示例

        >>> from wedoc import WedocClient
        >>> client = WedocClient("corpid", "corpsecret")
        >>> client.doc.del_doc("docid")
        """
        api = "/wedoc/del_doc"
        pyload = {"docid": docid}
        res = self.request("post", api, pyload=pyload)
        return res

    def get_doc_base_info(self, docid: str) -> dict:

        """
        获取文档基础信息
        :param docid:
        :return:

        使用示例

        >>> from wedoc import WedocClient
        >>> client = WedocClient("corpid", "corpsecret")
        >>> client.doc.get_doc_base_info("docid")
        """
        api = "/wedoc/get_doc_base_info"
        pyload = {"docid": docid}
        res = self.request("post", api, pyload=pyload)
        return res
