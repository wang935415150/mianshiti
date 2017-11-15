#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "yiguozhubuxia"
# Date: 2017/11/14

from concurrent.futures import ProcessPoolExecutor
import time
c=ProcessPoolExecutor(100)

def ha():
    print(1)
    time.sleep(2)
    print(2)

for i in range(2000):
    c.submit(ha)

