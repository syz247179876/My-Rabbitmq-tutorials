# -*- coding: utf-8 -*-
# @Time  : 2020/10/29 上午10:53
# @Author : 司云中
# @File : publish.py
# @Software: Pycharm


# exchange_type等于fanout-----广播机制

# 声明exchange_declare
import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 声明一个名为notice,类型为fanout的类型
channel.exchange_declare(exchange='notice',
                         exchange_type='fanout')

# 区别与之前的default exchange, fanout类型是broadcast机制,
# 并且队列中不能存在旧消息,需要一个完全新的随机的队列作为广播队列
# 官方提出了传入''给queue,来由服务随机生成一个队列
# 其中exclusive表示当前队列只被使用于一次connection,一旦connection断开,则删除该队列.
# 如果exclusive为False的话,则每次建立连接又会生成新的队列
result = channel.queue_declare(queue='', exclusive=True)

# 获取队列名,形如amq.gen-JzTY20BRgKO-HjmUJj0wLg
# print(f'队列名:{result.method.queue}')

# 将exchange绑定到对应的queue上,一个exchange对应多个queue
channel.queue_bind(exchange='notice',
                   queue=result.method.queue)

def callback(ch, method, properties, body):
    print(f'message:{body.decode()}')

# 配置处理对象,队列,回调函数,消息确认
channel.basic_consume(
    queue=result.method.queue,on_message_callback=callback, auto_ack=True
)

# 开始接受消息
channel.start_consuming()

