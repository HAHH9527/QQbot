# -*- coding: utf-8 -*-
"""
@Time:  2018/12/28 1:00
@author:10248
"""
import json
import ssl
import time
from urllib import parse, request

import prettytable
from prettytable import PrettyTable


async def get_serendipity(values):
    S = s = n = ''
    # 服务器
    if len(values) >= 1:
        S = values[0]
    # 奇遇名
    if len(values) >= 2:
        s = values[1]
    # 角色名
    if len(values) >= 3:
        n = values[2]
    ssl._create_default_https_context = ssl._create_unverified_context
    values = parse.urlencode({'m': 1, 'test': 1,
                              'S': S,  # 服务器
                              's': s,  # 奇遇名
                              'n': n  # 角色名
                              })
    url = 'https://jx3.derzh.com/serendipity/?' + values
    req = request.Request(url)
    with request.urlopen(req) as data:
        this_data = data.read().decode('utf-8')
    print(this_data)
    json_dict = json.loads(this_data)
    results = json_dict['result']
    table = PrettyTable(["服务器", "名字", "奇遇", "时间"])
    for result in results:
        table.add_row([result['server'], result['name'], result['serendipity'], await time_format(result['time'])])
        table.set_style(prettytable.PLAIN_COLUMNS)
        return str(table)


async def time_format(time_stamp):
    this_time = time.localtime(int(time_stamp))
    return time.strftime('%Y{y}%m{m}%d{d} %H:%M:%S', this_time).format(y='年', m='月', d='日')
