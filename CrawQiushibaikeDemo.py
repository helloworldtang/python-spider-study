#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'tangcheng'
__mtime__ = '9/22/2017'
"""
import urllib.request
import re


def get_content(url, page):
    # 模拟浏览器
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]

    # 将opener安装为全局
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    # 构建对应用户提取的正则表达式
    user_pattern = 'target="_blank" title="(.*?)">'
