# -*- coding: utf-8 -*-
# @Time  : 2020/10/25 下午9:07
# @Author : 司云中
# @File : ack_consumer.py
# @Software: Pycharm


import time
import pika
# 建立channel通道
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
def callback(ch, method, propeties, body):
    print("Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print('done')
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 由消费者告诉rabbitmq处理完消息可以删除了，如果当前consumer挂掉了，重新递交给其他的consumer，如果有的话


channel.basic_consume(queue='hello', on_message_callback=callback)
channel.start_consuming()



