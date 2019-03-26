# -*- coding: utf-8 -*-
"""
@Time:  2019/1/2 13:42
@author:10248
"""
import bot
from nonebot import on_command, CommandSession


@on_command('mytest', only_to_me=False)
async def mytest(session: CommandSession):
    await bot.get_this_bot().send_private_msg(user_id=1024830255, message='你好～')
