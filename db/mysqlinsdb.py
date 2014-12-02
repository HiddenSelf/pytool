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

t_plan = "汽车达人"
nowtime = datetime.datetime.now()
status = ["待完成", "已完成", "已放弃"]

def conn():
    try:
        conn = MySQLdb.connect(host='localhost', user='homestead', passwd='secret', db='topka_production', port=3306)
        cur = conn.cursor()
        return cur
    except Exception, e:
        print e

cur = conn()
sql = "insert into crm_plans(admin_id,\
                            created_admin_id,\
                            dealer_id,\
                            user_id,\
                            crm_follow_way_id,\
                            crm_follow_categories,\
                            status,\
                            star,\
                            quit_at,\
                            quit_reason,\
                            assess,\
                            confirm,\
                            confirm_at,\
                            plan_at,\
                            completed_at,\
                            delay_days,\
                            created_at,\
                            updated_at,\
                            deleted_at) value('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"

for i in xrange(100):
    # cur.execute(sql %(i, i, i, i, i, t_plan+"categories", random.sample(status, 1)), random.sample([0, 1], 1), nowtime, t_plan+"原因",random.sample([0, 1], 1), t_plan+"confirm", nowtime, nowtime, nowtime, i, nowtime, nowtime, nowtime)
    cur.execute(sql %(i,i,i,i,i,i,i,i,i,i,i,i,i,i,i,i,i))
    cur.close()
