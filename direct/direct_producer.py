# -*- coding: utf-8 -*-
# @Time  : 2020/10/30 上午9:37
# @Author : 司云中
# @File : direct_product.py
# @Software: Pycharm

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 声明exchange类型和exchange名字
channel.exchange_declare(exchange='direct_notice',
                         exchange_type='direct')

# 阵营
aim_routing_key = '天辉'


message = '我:小娜迦--海妖之歌'

# 发送消息,对应exchange名,routing_key
channel.basic_publish(
    exchange='direct_notice',
    routing_key=aim_routing_key,  # consumer中也要有与之对应的routing_key,则消息才会被正确接受
    body=message
)

print(f'已经向{aim_routing_key}阵营发送了一条消息')

channel.close()
