# -*- coding: utf-8 -*-
# @Time  : 2020/10/27 下午3:23
# @Author : 司云中
# @File : durable_consumer.py
# @Software: Pycharm

import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)  # 设置每个consumer统一时刻接受一个消息

channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()