#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'tangcheng'
__mtime__ = '12/13/2017'
"""


import scrapy
class MycsvItem(scrapy.Item):
    name = scrapy.Field()
    sex = scrapy.Field()