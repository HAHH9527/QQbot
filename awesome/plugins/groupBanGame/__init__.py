# -*- coding: utf-8 -*-
"""
@Time:  2019/1/2 14:57
@author:10248
"""
import random

import bot
from nonebot import on_command, CommandSession


@on_command('groupBanGame', aliases=('我要套餐',), only_to_me=False)
async def groupBanGame(session: CommandSession):
    group_id = session.ctx['group_id']
    user_id = session.ctx['user_id']
    duration = random.randint(60, 600)
    await bot.get_this_bot().send_group_msg(group_id=group_id, message='您要的' + str(duration) + '秒套餐')
    await bot.get_this_bot().set_group_ban(group_id=group_id, user_id=user_id, duration=duration)
