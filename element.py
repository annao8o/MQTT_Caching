import numpy as np
import random
from enum import Enum, auto


class Topic:    # topic = publisher
    def __init__(self, id):
        self.id = id
        self.popularity = 0
        self.connected_svr = None

    def set_popularity(self, popularity):
        self.popularity = popularity

    def get_popularity(self):
        return self.popularity

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

    def add_topic(self,top):    # top: int
        self.topic_lst.append(top)

    def add_subscriber(self, sub):  # sub: int
        self.sub_lst.append(sub)
        #sub.connect_broker(self)

    def get_load(self):
        # print(len(self.sub_lst))
        if len(self.sub_lst) == 0:
            return 0
        else:
            return len(self.sub_lst)

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

    def make_requests(self, size):
        req_sub = [self.sub_lst[random.randrange(len(self.sub_lst))] for _ in range(size)]
        request = [sub.get_interest() for sub in req_sub]

        return request


    def forward(self):
        self.ex_output += 1


    def routing(self, target_brk):
        target_brk.rcv_traffic(self)
        self.in_output += 1


    def rcv_traffic(self, brk):
        self.in_input += 1


    def clear(self):
        self.ex_output = self.ex_input = self.in_output = self.in_input = 0




class Subscriber:
    def __init__(self, id):
        self.id = id
        self.interest = None
        self.conn_brk = None

    def set_interest(self, topic):
        self.interest = topic

    def get_interest(self):
        return self.interest

    def connect_broker(self, brk):
        self.conn_brk = brk