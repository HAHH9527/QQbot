# -*- coding: utf-8 -*-
"""
@Time:  2018/12/30 15:56
@author:10248
"""

from nonebot import on_command, CommandSession
from awesome.plugins.exam.data_source import get_exam


# 科举查询
@on_command('exam', aliases=('科举', '科举查询'), shell_like=True)
async def exam(session: CommandSession):
    values = session.args['argv']
    await session.send(await get_exam(values))
