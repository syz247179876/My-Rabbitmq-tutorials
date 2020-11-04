# -*- coding: utf-8 -*-
# @Time  : 2020/10/27 下午3:23
# @Author : 司云中
# @File : durable_product.py
# @Software: Pycharm

import pika


connection = pika.BlockingConnection(
pika.ConnectionParameters(host='localhost'))

channel = connection.channel()  # 声明通道
channel.queue_declare(queue='task_queue', durable=True)

message1 = '水人波浪形态'
message2 = '第一滴血!'


channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message1,
    properties=pika.BasicProperties(
        delivery_mode=2,  # 让消息持久化
    ))

channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message2,
    properties=pika.BasicProperties(
        delivery_mode=2,  # 让消息持久化
    ))
connection.close()