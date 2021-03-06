#!/usr/bin/env python
# coding: utf-8

def ip_range(num, limit=25):
    ''' 返回指定范围数值 '''
    bnum, enum = num - limit, num + limit
    if bnum < 1:
        bnum, enum = 1, enum + abs(bnum)
    elif enum > 254:
        bnum, enum = bnum - (enum - 254), 254
    return range(bnum, enum)

def output(target):
    '''
    name: Subnet Generater
    depends: cdn
    priority: 2
    version: 0.2
    '''
    if getattr(target, 'cdn', True): return

    pos = target.ip.rfind('.')
    segment, last_num = target.ip[:pos], int(target.ip[pos + 1:])

    subnet = [segment +'.'+ str(i) for i in ip_range(last_num)]
    target.subnet = set(subnet)
