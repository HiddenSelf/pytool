#! /usr/sbin/python env
# -*- coding:utf-8 -*-

'''
Created on PyCharm  

@author: {edison}

@date: {14-12-1} {下午10:59}

@summary: 

@note: 

@version: 
'''
__author__ = 'edison'


import os,sys
import MySQLdb

from sqlalchemy import *

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sql_connection = "mysql+mysqldb://noah:123456@127.0.0.1:3306/test?charset=utf8"
engine = create_engine(sql_connection, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class NovaBase():
    pass

BASE = declarative_base()

class InstanceTypes(BASE, NovaBase):
    __tablename__ = "abc"
    id = Column(Integer,primary_key=True)
    name = Column(String(255))
    pwd  = Column(String(255))

flavors = session.query(InstanceTypes).all()

for f in flavors:
    print f.id, f.name

it = InstanceTypes(id=1, name='ccc', pwd='bbb')
session.add(it)
session.commit()