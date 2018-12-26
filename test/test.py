# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 13:12:23 2018

@author: 10248
"""

"""
import requests
import json

data = 'category_id=0&add_ad=1&p=1&num=20'
header = {'Content-Type':'application/x-www-form-urlencoded',
            'Content-Length':'33',
            'Connection':'Keep-Alive',
            'Accept-Encoding':'gzip',
            'User-Agent':'okhttp/3.9.0'}
response = requests.post('http://www.jx3tong.com/?m=api&c=info&a=content_list',data = data,headers = header)

daily_info = json.loads(response.text)['daily_info']#获取json中daily_info字段
daily_update_time = daily_info.get('daily_update_time')#获取daily_info中daily_update_time
daily_list = daily_info.get('daily_list')#获取daily_info中daily_lsit
daily_update_time_list = daily_update_time.split('  ')
daily_str = '今天是'+daily_update_time_list[0]+' 星期'+daily_update_time_list[1]+' 日常:\n'
for mission in daily_list:
    daily_str+=mission.get('title')+'\n'
print(daily_str)
"""

import time

now = time
now_str = now.strftime('%Y{y}%m{m}%d{d}').format(y='年',m='月',d='日')

now_str += ' 星期'
now_day = now.strftime('%w')
if now_day == '0':
    now_str += '日'
elif now_day =='1':
    now_str += '一'
elif now_day == '2':
    now_str += '二'
elif now_day == '3':
    now_str += '三'
elif now_day == '4':
    now_str += '四'
elif now_day == '5':
    now_str += '五'
elif now_day == '6':
    now_str += '六'
