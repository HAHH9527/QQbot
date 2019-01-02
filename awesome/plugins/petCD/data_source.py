# -*- coding: utf-8 -*-
"""
@Time:  2019/1/2 13:22
@author:10248
"""

import json
from urllib import request


async def get_petCD():
    url = 'http://www.yayaquanzhidao.cn/GetCD.ashx'
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    data = '9'
    req = request.Request(url, headers=headers, data=data.encode('utf-8'))  # POST方法
    with request.urlopen(req) as page:
        this_data = page.read().decode('utf-8')
    json_data = json.loads(this_data)
    petCD_str = '宠物CD:\n'
    for the_pet in json_data:
        if the_pet['Buff'] <= 2:
            petCD_str += the_pet['Msg']
    petCD_str += 'PS:失联宠物不显示'
    return petCD_str
