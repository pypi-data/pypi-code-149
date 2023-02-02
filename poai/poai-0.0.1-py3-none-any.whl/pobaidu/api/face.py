# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/2/2 23:39 
@Description     ：
'''

import base64

import requests
import json

def face_merge(client_id, client_secret, base_img='', face_img='', output_path=r'./output/face_merge.jpg'):
    url = f"https://aip.baidubce.com/oauth/2.0/token?client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials"

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    token_response = requests.request("POST", url, headers=headers, data=payload)

    print(token_response.text)

    res = json.loads(token_response.text)
    access_token = res['access_token']
    url = f"https://aip.baidubce.com/rest/2.0/face/v1/merge?access_token={access_token}"
    with open(base_img, 'rb') as fp:
        base_img = base64.b64encode(fp.read()).decode()
    with open(face_img, 'rb') as fp:
        face_img = base64.b64encode(fp.read()).decode()
    print(base_img)
    payload = json.dumps({
        "image_target": {
            "image": base_img,
            "image_type": "BASE64",
            "quality_control": "NONE"
        },
        "image_template": {
            "image": face_img,
            "image_type": "BASE64"
        },
        "merge_degree": "HIGH"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(json.loads(response.text)['result']['merge_image'])
    res_img = json.loads(response.text)['result']['merge_image']
    # 解码图片
    imgdata = base64.b64decode(res_img)
    # 将图片保存为文件
    with open(output_path, 'wb') as f:
        f.write(imgdata)

