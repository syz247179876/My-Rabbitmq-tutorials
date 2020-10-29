# -*- coding: utf-8 -*-
# @Time  : 2020/10/27 下午2:17
# @Author : 司云中
# @File : dispatch_worker.py
# @Software: Pycharm

import pika
# 建立channel通道
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)


def callback(ch, method, propeties, body):
    print("Received %r" % body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 消息确认


channel.basic_consume(queue='task_queue',on_message_callback=callback)


channel.start_consuming()
channel.close()
