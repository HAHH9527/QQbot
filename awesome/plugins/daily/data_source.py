# -*- coding: utf-8 -*-
"""
@Time:  2018/12/26 18:00
@author:10248
"""

import time
import json

import requests


# 获取日常消息
async def get_daily():
    data = 'category_id=0&add_ad=1&p=1&num=20'
    header = {'Content-Type': 'application/x-www-form-urlencoded',
              'Content-Length': '33',
              'Connection': 'Keep-Alive',
              'Accept-Encoding': 'gzip',
              'User-Agent': 'okhttp/3.9.0'}
    response = requests.post('http://www.jx3tong.com/?m=api&c=info&a=content_list', data=data,
                             headers=header)  # 调用剑三通接口
    daily_info = json.loads(response.text)['daily_info']  # 获取json中daily_info字段
    daily_update_time = daily_info.get('daily_update_time')  # 获取daily_info中daily_update_time
    daily_list = daily_info.get('daily_list')  # 获取daily_info中daily_lsit
    daily_update_time_list = daily_update_time.split(' ')
    daily_str = '现在是' + await get_nowtime() + '\n日常:'
    for mission in daily_list:
        daily_str += '\n' + mission.get('title').lstrip().rstrip()
    daily_str += '\n本数据更新时间：' + daily_update_time_list[0]
    return daily_str


# 获取现在时间 2000年1月1日 星期一 12:12:12
async def get_nowtime():
    now = time
    nowtime = now.strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日')
    nowtime += ' 星期'
    now_day = now.strftime('%w')
    if now_day == '0':
        nowtime += '日'
    elif now_day == '1':
        nowtime += '一'
    elif now_day == '2':
        nowtime += '二'
    elif now_day == '3':
        nowtime += '三'
    elif now_day == '4':
        nowtime += '四'
    elif now_day == '5':
        nowtime += '五'
    elif now_day == '6':
        nowtime += '六'
    nowtime += ' ' + now.strftime('%H:%M:%S')
    return nowtime
