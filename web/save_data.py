#coding:utf-8
from django.test import TestCase
import redis
import json
import redis
#连接redis消息队列
"""
s = redis.Redis(host='192.168.48.132', port=6379, db=0)

channel = 'password'

msg_queue = s.pubsub()
msg_queue.subscribe(channel)


def get_data():
    pass

def save_data():
    pass
"""