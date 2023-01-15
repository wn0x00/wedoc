# 企业微信文档接口

## 案例

```python
from wedoc import WedocClient


if __name__ =="__main__":
    corpid = "xxxxxxxxxxxxx"
    corpsecret = "xxxxxxxxxxxxx"

    client = WedocClient(corpid, corpsecret)
    res = client.get_crop_access_token()
    client.doc.create_doc()

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
