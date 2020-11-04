# -*- coding: utf-8 -*-
# @Time  : 2020/11/3 下午11:54
# @Author : 司云中
# @File : topics_producer.py
# @Software: Pycharm

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

# 声明exchange
channel.exchange_declare(exchange='topic_exchange', exchange_type='topic')

message = '来自自夜魇阵营'
message2 = '夜魇军团的白虎拿下了一血!'

# 设定通用的模式主题
routing_key = ['夜魇.hero','夜魇.hero.action']

# 发送消息

channel.basic_publish(
    exchange='topic_exchange',routing_key=routing_key[0], body=message
)
channel.basic_publish(
    exchange='topic_exchange', routing_key=routing_key[1], body=message2
)

channel.close()