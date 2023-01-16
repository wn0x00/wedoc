# 企业微信文档接口

## 案例

```python
from wedoc import WedocClient


if __name__ =="__main__":
    corpid = "xxxxxxxxxxxxx"
    corpsecret = "xxxxxxxxxxxxx"

    docid = "xxxxxxxxxxxxxxxxxxxxxx"
    client = WedocClient(corpid, corpsecret)
    res = client.access_token
    print(res)
    doc_type = 4
    doc_name = "物料"
    res = client.doc.create_doc(doc_name, doc_type)
    print(res)
    res = client.workbook.get_sheet_properties(docid)
    print(res)

```

## 文档接口

- 创建文档
- 重命名文档
- 删除文档
- 获取文档基础信息

## 表格接口

- 获取表格行列信息
- 获取表格数据
- 编辑表格内容
- 创建 sheet 页
- 删除 sheet 页
- 读取总行数
- 读取总列数
- 读取单元格内容
- 设置单元格内容
