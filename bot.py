# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 16:49:33 2018

@author: 10248
"""
from os import path
import nonebot
import config

# bot启动主文件
if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(path.join(path.dirname(__file__), 'awesome', 'plugins'),
                         'awesome.plugins')
    nonebot.run(host='127.0.0.1', port=8800)
this_bot = nonebot.get_bot()


def get_this_bot():
    return this_bot
