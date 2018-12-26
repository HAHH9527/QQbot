# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 16:49:33 2018

@author: 10248
"""

from os import path

import none

import config

if __name__ == '__main__':
    none.init(config)
    none.load_plugins(path.join(path.dirname(__file__), 'awesome', 'plugins'),
                      'awesome.plugins')
    none.run(host='127.0.0.1', port=8800)