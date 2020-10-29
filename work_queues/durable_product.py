# -*- coding: utf-8 -*-
# @Time  : 2020/10/27 下午2:16
# @Author : 司云中
# @File : dispatch_consumer.py
# @Software: Pycharm

import pika
# 建立channel通道
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)


channel.basic_publish(exchange='',
                      routing_key="task_queue",
                      body='syz666',
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))

channel.close()