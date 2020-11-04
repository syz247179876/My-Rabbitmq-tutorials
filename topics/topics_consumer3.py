# -*- coding: utf-8 -*-
# @Time  : 2020/11/3 下午11:54
# @Author : 司云中
# @File : topics_consmer.py
# @Software: Pycharm

# 相比于direct模式,更加的适应复杂的模式匹配,能够实现多条件的路由绑定

import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_exchange', exchange_type='topic')

# 声明队列
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

# 订阅该queue具体关心的主题,例如该主题只关注"夜魇.hero.*下的模式"
# 不与该demo中任何producer提供的routing_key相绑定
bind_routing = '夜.*'


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
