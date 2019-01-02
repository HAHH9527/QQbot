# -*- coding: utf-8 -*-
"""
@Time:  2018/12/26 18:27
@author:10248
"""

from nonebot import on_command, CommandSession
from awesome.plugins.petCD.data_source import get_petCD


# 宠物CD查询
@on_command('petCD', aliases=('宠物', '宠物查询'), only_to_me=False)
async def daily(session: CommandSession):
    await session.send(await get_petCD())
