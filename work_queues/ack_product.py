# -*- coding: utf-8 -*-
# @Time  : 2020/10/25 下午9:05
# @Author : 司云中
# @File : ack.py
# @Software: Pycharm


import time
import pika
# 建立channel通道
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

message = '......syz love you!'
# 将message发送到rabbitmq就可以执行其他的了

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
channel.close()


