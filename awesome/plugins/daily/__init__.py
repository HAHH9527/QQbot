# -*- coding: utf-8 -*-
"""
@Time:  2018/12/26 18:00
@author:10248
"""

from none import on_command, CommandSession, on_natural_language, NLPSession, NLPResult

from awesome.plugins.daily.data_source import get_daily


@on_command('daily', aliases=('日常', '日常查询'), only_to_me=False)
async def daily(session: CommandSession):
    daily_str = await get_daily()
    await session.send(daily_str)


@on_natural_language(keywords=('日常'))
async def _(session: NLPSession):
    return NLPResult(90.0, 'daily', {})
