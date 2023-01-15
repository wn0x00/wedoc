from wedoc.api.base import WedocApiBase


class Document(WedocApiBase):
    def create_doc(self, doc_name, doc_type, spaceid="", fatherid="", admin_users=[]):
        """创建文档"""
        api = "/wedoc/create_doc"
        pyload = {
            "doc_type": doc_type,
            "doc_name": doc_name,
        }

        res = self.request("post", api, pyload=pyload)
        return res

    def rename_doc(self, docid, new_name):
        """重命名文档"""
        api = "/wedoc/rename_doc"
        pyload = {"docid": docid, "new_name": new_name}
        res = self.request("post", api, pyload=pyload)
        return res

    def del_doc(self, docid):
        """删除文档"""
        api = "/wedoc/del_doc"
        pyload = {"docid": docid}
        res = self.request("post", api, pyload=pyload)
        return res

    def get_doc_base_info(self, docid):
        """获取文档基础信息"""
        api = "/wedoc/get_doc_base_info"
        pyload = {"docid": docid}
        res = self.request("post", api, pyload=pyload)
        return res
