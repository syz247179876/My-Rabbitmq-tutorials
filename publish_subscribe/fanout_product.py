# -*- coding: utf-8 -*-
# @Time  : 2020/10/29 下午12:50
# @Author : 司云中
# @File : fanout_consumer.py
# @Software: Pycharm


import pika
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 声明一个名为notice,类型为fanout的类型
channel.exchange_declare(exchange='notice',
                         exchange_type='fanout')

# 广播到所有的队列
message = '天怒vs黑鸟'
channel.basic_publish(exchange='notice',
                     routing_key='',
                     body=message)
print(f"sent {message}")
# 发送完关闭连接
connection.close()