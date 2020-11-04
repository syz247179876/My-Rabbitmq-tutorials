# -*- coding: utf-8 -*-
# @Time  : 2020/11/3 下午11:54
# @Author : 司云中
# @File : topics_consmer.py
# @Software: Pycharm

import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_exchange', exchange_type='topic')

# 声明队列
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue


# 订阅该queue具体关心的主题,例如该主题只关注"天辉.hero.*下的模式"
# 可以绑定 "天辉.hero"
bind_routing = '天辉.*'


channel.queue_bind(
    exchange='topic_exchange',
    queue=queue_name,
    routing_key=bind_routing
)

def callback(ch, method, properties, body):
    print(f"接收到消息{body.decode()}")

channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True
)
channel.start_consuming()



