#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'tangcheng'
__mtime__ = '12/12/2017'
"""

from urllib import request
from urllib import parse
from urllib.request import urlopen

# http://dujia.qunar.com/pq/list_%E5%AE%9C%E6%98%8C?
# searchfrom=around&arounddep=%E6%AD%A6%E6%B1%89&tf=Ihot_01

data = {}

data['searchfrom'] = 'around'

data["arounddep"] = '%E6%AD%A6%E6%B1%89'

data['tf'] = 'Ihot_01'

value = parse.urlencode(data)

print(value)

url = 'http://dujia.qunar.com/pq/list_%E5%AE%9C%E6%98%8C' + '?' + value

response = urlopen(url)

print(response.read())