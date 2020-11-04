# -*- coding: utf-8 -*-
# @Time  : 2020/11/4 下午11:26
# @Author : 司云中
# @File : topics_producer2.py
# @Software: Pycharm

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

# 声明exchange
channel.exchange_declare(exchange='topic_exchange', exchange_type='topic')

message = '来自天辉和中立阵营'

# 设定通用的模式主题,可以设定多个允许的主题,供queue自由进行模式绑定
routing_key = ['天辉.hero','中立.monster']

# 发送消息
for i in routing_key:
    channel.basic_publish(
        exchange='topic_exchange',routing_key=i, body=message
    )
channel.close()