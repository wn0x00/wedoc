# 快速上手


## 安装

```shell
pip install wedoc
```

## 使用

### 创建文档

```python
corpid = "ww0c09xxxxxxxxxxx"
corpsecret = "U8Bdxxxxxxxxxxxxxxxxxxx"


client = WedocClient(corpid, corpsecret)
res = client.access_token
print(res)

doc_type = 4
doc_name = "测试"
res= client.doc.create_doc(doc_name, doc_type)
print(res)
```

### 操作表格

获取 sheet 页基础信息

```python
docid= "dcaRoy0xxxxxxxxxxxxxxxxx"

wb = client.workbook(docid)
print(wb.sheet_metadata)

```

操作 sheet 页

```python
print(wb.get_sheet_names())
print(wb.get_active_sheet())

res = wb.add_sheet("测试")
print(res)

print(wb.get_sheet_names())
res = wb.delete_sheet("测试")
print(res)
print(wb.get_sheet_names())
```

操作表格

```python
print(wb.get_column_count())
print(wb.get_row_count())
print(wb.docid)
res = wb.get_sheet_properties()
print(res)

res = wb.get_cell(row=2,column="B")
print(res)
res = wb.set_cell(1, "A", "测试")
print(res)
```
