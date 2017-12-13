#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'tangcheng'
__mtime__ = '12/13/2017'
"""


from scrapy.spiders import CSVFeedSpider
from mycsv.items import MycsvItem
class MycsvspiderSpider(CSVFeedSpider):
    name = 'mycsvspider'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/mydata.cvs']
    headers = ['name','sex','addr','email']
    delimiter = ','
    def parse_row(self, response, row):
        i = MycsvItem()
        i['name'] = row['name'].encode()
        i['sex'] = row['sex'].encode()
        print("名字是:")
        print(i['name'])
        print("性别是:")
        print(i['sex'])
        print("----------------------")
        return i