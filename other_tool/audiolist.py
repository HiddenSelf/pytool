#! /usr/sbin/python env
# -*- coding:utf-8 -*-

'''
Created on PyCharm  

@author: Edison

@date: 14/12/1  下午3:22

@summary: 

@note: 

@version: 
'''
__author__ = 'Edison'

import os
import sys
import datetime
import random
import MySQLdb

t_plan = r"汽车达人"
nowtime = datetime.datetime.now()
status = ["待完成", "已完成", "已放弃"]

def conn():
    try:
        conn = MySQLdb.connect(host='localhost', user='homestead', passwd='secret', db='topka_production', port=3306, charset="utf8")
        cur = conn.cursor()
        return cur, conn
    except Exception, e:
        print e

cur, conn = conn()
sql = "insert into crm_plans(admin_id,created_admin_id,dealer_id,user_id,crm_follow_way_id,crm_follow_categories,status,star,quit_at,quit_reason,assess,confirm,confirm_at,plan_at,completed_at,delay_days,created_at,updated_at,deleted_at) value(%d,%d,%d, %d, %d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"

for i in xrange(10):
    cur.execute(sql %(i, i, i, i, i, t_plan+"categories", random.sample(range(2), 1)[0], random.sample(range(1), 1)[0], nowtime, t_plan+"reason", random.sample(range(1), 1)[0], random.sample(range(1), 1)[0], nowtime, nowtime, nowtime, random.sample(range(10), 1)[0], nowtime, nowtime, nowtime))

conn.commit()
cur.close()