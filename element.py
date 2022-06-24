import numpy as np
import random

class Message:
    def __init__(self):

class Topic:
    def __init__(self, id):
        self.id = id
        self.connected_svr = None

    def set_svr(self, svr):
        self.connected_svr = svr


class Controller:   # load balancer
    def __init__(self):
        self.brk_lst = list()

    def add_broker(self, brk):
        if type(brk) == int:
            self.brk_lst.append(brk)
        if type(brk) == object:
            self.brk_lst.append(brk.id)
        if type(brk) == list():
            self.brk_lst = brk

    def match_sub_broker(self, sub, broker):
        brk = random.randint()
        if self.check_load():

    def check_load(self):



class Broker:
    def __init__(self, id, cache_size, num_data):
        self.id = id
        self.cache_size = cache_size
        self.caching_map = np.zeros(num_data, dtype=np.bool_)
        self.sub_lst = list()
        self.topic_lst = list()
        self.ex_traffic = 0
        self.in_traffic = 0

    def add_topic(self,top):
        self.topic_lst.append(top)

    def add_sub(self, sub):
        self.sub_lst.append(sub)

    def forward_msg(self):
        self.ex_traffic += 1

    def routing_msg(self, brk, msg):
        self.in_traffic += 1
        brk.rcv_traffc(msg)

    def rcv_traffic(self, msg):


class Subscriber:
    def __init__(self, id, interest):
        self.id = id
        self.interest = interest
        self.conn_brk = None

    def connect_broker(self, brk):


class Zipf:
    def __init__(self):
        self.pdf = None
        self.cdf = None

    def set_env(self, expn, num_contents):
        temp = np.power(np.arange(1, num_contents + 1), -expn)
        zeta = np.r_[0.0, np.cumsum(temp)]
        # zeta = np.r_[0.0, temp]
        self.pdf = [x / zeta[-1] for x in temp]
        self.cdf = [x / zeta[-1] for x in zeta]

    def get_sample(self, size=None):
        if size is None:
            f = random.random()
        else:
            f = np.random.random(size)
        return np.searchsorted(self.cdf, f) - 1