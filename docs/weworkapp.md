# 企业应用相关配置

## 创建企业应用


1. 从企业微信客户端进入企业微信控制台
![](./imgs/Snipaste_2023-01-17_00-28-05.png)

2. 点击应用管理, 再点击创建应用
![](./imgs/Snipaste_2023-01-17_00-32-39.png)

3. 配置应用基础信息
![](./imgs/Snipaste_2023-01-17_00-34-47.png)

4. 配置企业可信 IP (可百度 IP 获取)
![](./imgs/Snipaste_2023-01-17_00-36-35.png)

5. 在协作, 文档的 API 配置应用
![](./imgs/Snipaste_2023-01-17_00-38-20.png)

6. 设置可调用接口的应用
![](./imgs/Snipaste_2023-01-17_00-40-12.png)

7. 获取 `corpid`
![](./imgs/Snipaste_2023-02-28_15-38-54.png)


8. 获取 `corpsecret`
![](./imgs/Snipaste_2023-02-28_15-39-43.png)


## 获取文档 ID

> 目前仅支持应用创建文档

```python
corpid = "wwxxxxxxxxxxx"
corpsecret = "U8xxxxxxxxxxxxxx"


client = WedocClient(corpid, corpsecret)

# 文件类型为表格
doc_type = 4

# 文件名称

doc_name = "测试"

res = client.doc.create_doc(doc_name, doc_type, admin_users=["xxxxxxxxx"])
print(res)

```

`admin_users` 需要在控制台查看

![](./imgs/Snipaste_2023-02-28_15-45-15.png)
