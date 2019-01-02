# -*- coding: utf-8 -*-
"""
@Time:  2018/12/30 16:07
@author:10248
"""
import json

import ssl
from urllib import parse, request


async def get_exam(values):
    q = ''
    if len(values) >= 1:
        q = values[0]
    parametes = parse.urlencode({'m': 1,
                                 'q': q
                                 })
    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'https://jx3.derzh.com/exam/?' + parametes
    req = request.Request(url)
    with request.urlopen(req) as page:
        this_data = page.read().decode('utf-8')
    json_data = json.loads(this_data)
    results = json_data['result']
    exam_str = '科举:'
    for result in results:
        exam_str += '\n\n问题:' + result['ques'] + \
                    '\n答案:' + result['answ']
    return exam_str
