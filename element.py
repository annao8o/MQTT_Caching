import numpy as np
import random
from enum import Enum, auto

class MsgType(Enum):
    ex_input = auto()
    ex_output = auto()
    in_input = auto()
    in_output = auto()


class Topic:    # topic = publisher
    def __init__(self, id):
        self.id = id
        self.connected_svr = None

    def set_svr(self, svr):
        self.connected_svr = svr

    def get_svr(self):
        return self.connected_svr

class Broker:
    def __init__(self, id, cache_size, num_data, controller):
        self.id = id
        self.cache_size = cache_size
        self.caching_map = np.zeros(num_data, dtype=np.bool_)
        self.controller = controller
        self.sub_lst = list()
        self.topic_lst = list()
        self.ex_traffic = 0
        self.in_traffic = 0
        self.load = 0

    def add_topic(self,top):    # top: int
        self.topic_lst.append(top)

    def add_subscriber(self, sub):  # sub: obj
        self.sub_lst.append(sub)
        sub.connect_broker(self)

    def set_load(self):
        self.load += 1

    def get_load(self):
        return self.load

    # def process_req(self, top):
    #     if self.isContain(top):
    #         self.forward_msg()
    #     else:
    #         self.routing_msg()

    def isContain(self, top):
        avail = False
        if self.caching_map[top] or (top in self.topic_lst):
            avail = True
        return avail

    # def forward(self):
    #     self.ex_traffic += 1
    #     return 1
    #
    # def routing(self, brk):
    #     self.in_traffic += 1

    # def rcv_traffic(self, msg):



class Subscriber:
    def __init__(self, id, interest):
        self.id = id
        self.interest = interest
        self.conn_brk = None

    def connect_broker(self, brk):
        self.conn_brk = brk