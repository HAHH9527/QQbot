# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 17:20:53 2018

@author: 10248
"""

import re

from none.default_config import *

SUPERUSERS = {1024830255}
COMMAND_START = {'!', '！'}
NICKNAME: Union[str, Iterable[str]] = {'帮主', '狗帮主', '美女', '姐妹'}