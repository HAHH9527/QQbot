# -*- coding: utf-8 -*-
"""
@Time:  2018/12/28 1:00
@author:10248
"""
from none import on_command, CommandSession

from awesome.plugins.serendipity.data_source import get_serendipity


# 奇遇查询
@on_command('serendipity', aliases=('奇遇', '奇遇查询'), shell_like=True, only_to_me=False)
async def serendipity(session: CommandSession):
    values = session.args['argv']
    await session.send(await get_serendipity(values))
