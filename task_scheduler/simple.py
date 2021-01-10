# -*- coding: utf-8 -*-
# @Time  : 2021/1/10 下午9:53
# @Author : 司云中
# @File : simple.py
# @Software: Pycharm
import time
from heapq import heappush, heappop

from functools import total_ordering
from collections import deque

@total_ordering
class JobItem(object):
    """任务对象"""

    def __init__(self, executing_ts, task):
        self.executing_ts = executing_ts  # 执行时间
        self.task = task                  # 任务函数

    def __eq__(self, other):
        return self.executing_ts == other.executing_ts

    def __lt__(self, other):
        return self.executing_ts < other.executing_ts


new_deque = {}  # 声明空对列

def get_wait(timeout):
    """阻塞等待timeout时间内是否来了新任务"""
    pass

def simple_job_dispatcher():
    """任务调度"""

    heap = []   # 声明一个堆
    ready_deque = deque()  # 声明空对列


    while True:   # 无限循环
        wait_time = 1
        if heap:   # 如果堆不空
            now = time.time()
            if heap[0].executing_ts - now <= 0: # 堆顶任务已经到达
                ready_deque.append(heappop(heap))       # 弹出堆顶任务并加入到就绪队列

                continue  # 继续循环
            else:
                wait_time = heap[0].executing_ts - now    # 否则计算当前等待时间
        try:
            # 从新任务队列等待并取出新任务
            # 超时时间即为堆顶任务等待时间
            # 在get_wait内部阻塞wait_time时间
            # 超时时间到达后,get_wait停止阻塞跳出,进入下次循环并执行堆顶任务
            task_item = get_wait(wait_time)
            if task_item is None:
                continue  # 进行下次循环

            heappush(heap, task_item)  # 将新任务压入堆
        except:
            pass



