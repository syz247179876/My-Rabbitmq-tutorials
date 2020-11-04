# -*- coding: utf-8 -*-
# @Time  : 2020/10/30 上午9:37
# @Author : 司云中
# @File : direct_consumer.py
# @Software: Pycharm

print('我是夜魇阵营的,我正在监听夜魇阵营消息!')

import pika

#  相比于fanout,增加了routing_key来限制选择消息转发指定的队列

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 声明exchange类型和名字
channel.exchange_declare(exchange='direct_notice',
                         exchange_type='direct')

# 创建随机空队列,生命周期仅存活一次connection
result = channel.queue_declare(queue='',exclusive=True)

# 获取队名
queue_name = result.method.queue

# 阵营
receive_queues_routing_key = ['夜魇']

# 绑定阵营(queue)
for camp in receive_queues_routing_key:
    # 将exchange和queue绑定
    channel.queue_bind(
        exchange='direct_notice',
        queue=queue_name,
        routing_key=camp
    )

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body.decode()))

channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True
)

channel.start_consuming()



