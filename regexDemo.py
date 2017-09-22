#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'tangcheng'
__mtime__ = '9/21/2017'
"""

import re
string="hellomypythonhispythonourpythonend"
pattern=".python."
result=re.compile(pattern).findall(string)
print(result)
for i in result:
    print(i)