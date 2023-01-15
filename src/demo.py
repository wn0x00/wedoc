import requests
import json


def get_crop_access_token(corpid, corpsecret):
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


def get_sheet_info(access_token, sheet_id):
    url = f"https://qyapi.weixin.qq.com/cgi-bin/wedoc/get_doc_base_info?access_token={access_token}&debug=1"
    pyload = {
        "docid": sheet_id,
    }
    headers = {"Content-Type": "application/json"}
    res = requests.post(url, headers=headers, data=json.dumps(pyload))
    return res.json()


def create_doc(access_token):
    url = f"https://qyapi.weixin.qq.com/cgi-bin/wedoc/create_doc?access_token={access_token}&debug=1"
    pyload = {
        "doc_type": "4",
        "doc_name": "剑心测试",
    }
    headers = {"Content-Type": "application/json"}
    res = requests.post(url, headers=headers, data=json.dumps(pyload))
    return res.json()


if __name__ == "__main__":
    corpid = "ww0c0936b1528ad42b"
    corpsecret = "U8BdEfvnySFcJE5PvLCOfd1dhj4-hawQU8I4f5vXVhM"
    res = get_crop_access_token(corpid, corpsecret)
    print(res.get("access_token"))
    sheet_id = "dcFaoW-UCcjABuh7L9JkKVLnZfQMlYpLiWtyDyCj_mh8jOzWu5Io-gDbTWGzyAX-WUVZ4zbvZJbSbEYCdniuFaHw"
    # res = get_sheet_info(res.get("access_token"), sheet_id)
    # print(res)
    res = create_doc(res.get("access_token"))
    print(res)
