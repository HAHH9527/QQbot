# -*- coding: utf-8 -*-
"""
@Time:  2018/12/28 1:00
@author:10248
"""
import json
import ssl
import time
from urllib import parse, request


async def get_serendipity(values):
    S = s = n = ''  # 服务器 奇遇名 角色名
    serendipity_len = 5  # 数据条数
    if len(values) >= 1:
        if values[0] != '.':
            S = values[0]
    if len(values) >= 2:
        if values[1] != '.':
            s = values[1]
    if len(values) >= 3:
        if values[2] != '.':
            n = values[2]
    if len(values) >= 4:
        serendipity_len = values[3]
    parametes = parse.urlencode({'m': 1, 'test': 1,
                                 'S': S,  # 服务器
                                 's': s,  # 奇遇名
                                 'n': n  # 角色名
                                 })
    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'https://jx3.derzh.com/serendipity/?' + parametes
    req = request.Request(url)
    with request.urlopen(req) as data:
        this_data = data.read().decode('utf-8')
    json_dict = json.loads(this_data)
    results = json_dict['result']
    serendipity_str = '奇遇:'
    flag_for = 0
    for result in results:
        serendipity_str += '\n\n' + result['name'] + ':' + \
                           '\n|-' + result['server'] + \
                           '\n|-' + result['serendipity'] + \
                           '\n|-' + await time_format(result['time'])
        flag_for = flag_for + 1
        if flag_for >= int(serendipity_len):
            break
    return serendipity_str


async def time_format(time_stamp):
    this_time = time.localtime(int(time_stamp))
    return time.strftime('%Y{y}%m{m}%d{d} %H:%M:%S', this_time).format(y='年', m='月', d='日')
