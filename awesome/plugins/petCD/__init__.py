# -*- coding: utf-8 -*-
"""
@Time:  2018/12/26 18:27
@author:10248
"""

from none import on_command, CommandSession, on_natural_language, NLPSession, NLPResult


# 宠物CD查询
@on_command('petCD', aliases=('宠物', '宠物查询'), only_to_me=False)
async def daily(session: CommandSession):
    await session.send('战无宠物CD(鸭鸭)：http://www.yayaquanzhidao.cn/?ID=9')


@on_natural_language(keywords=('宠物'))
async def _(session: NLPSession):
    return NLPResult(90.0, 'petCD', {})
