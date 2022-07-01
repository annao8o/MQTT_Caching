import numpy as np
import random
from element import Broker, Subscriber
import math
from config import *

class Environment:   # load balancer
    def __init__(self, requests, top_lst, sub_lst):
        self.top_lst = top_lst
        self.brk_lst = list()
        self.client_lst = sub_lst
        self.algo_lst = list()

        self.asso_map = np.zeros((num_broker, num_topic), dtype=np.bool_)
        self.lambda_map = np.zeros(num_topic, dtype=np.float_)
        self.total_load = 0
        self.total_req = 0

        self.curr_t = 0
        self.requests = requests
        self.curr_req = list()

        self.create_env(cache_size)


    def create_env(self, cache_size):
        print("create environment..")

        # generate the brokers
        self.brk_lst = [Broker(i, cache_size, len(self.top_lst), self) for i in range(num_broker)]
        self.client_lst = [Subscriber(i) for i in range(num_sub)]

        # assign a topic(publisher) to a broker
        self.assign_top()

        # assign the subscribers to the brokers
        self.match_sub_broker(self.client_lst)

        for top in self.top_lst:
            self.lambda_map[top.id] = arrival_rate * top.popularity

    def assign_top(self):
        assign_lst = np.random.uniform(0, num_broker, size=num_topic)
        for top, brk in enumerate(assign_lst):
            brk = math.trunc(brk)
            self.brk_lst[brk].add_topic(top)
            self.asso_map[brk][top] = True
            self.top_lst[top].set_svr(self.brk_lst[brk])

        # for k in self.top_lst:
        #     assign = False
        #     while assign:
        #         brk = self.brk_lst[random.randint()]
        #         if brk.num_top <= len(self.top_lst) / self.num_broker:
        #             brk.add_topic(k)
        #             assign = True

    def match_sub_broker(self, sub):
        for s in sub:
            brk = self.brk_lst[random.randrange(num_broker)]
            self.total_load += 1
            if self.check_load(brk):
                brk.add_subscriber(s)
                # print((brk, s))


    def check_load(self, brk):
        return brk.get_load() < gamma * (self.total_load / num_broker)


    def add_algo(self, algo):
        if type(algo).__name__ == 'CacheAlgo':
            self.algo_lst.append(algo)
            print(f'Success to add algorithm: {algo.name}')
        else:
            print("wrong algo class")


    def load_curr_request(self, t):
        self.curr_req.clear()
        self.curr_t = t
        for r in self.requests:
            if r[0] == t:
                self.curr_req.append(r)


    def request(self):
        ex_traffic_lst = [0 for _ in range(len(self.algo_lst))]
        in_traffic_lst = [0 for _ in range(len(self.algo_lst))]
        hit_lst = [0 for _ in range(len(self.algo_lst))]
        delay_lst = [0 for _ in range(len(self.algo_lst))]

        while self.curr_req:
            req = self.curr_req.pop(0)  # (t, svr_id, requested_top)
            # self.brk_lst[req[1]].process_req(req[2])
            self.total_req += 1
            for idx, algo in enumerate(self.algo_lst):
                ex_traffic, in_traffic, hit, delay = algo.process_req(req)
                ex_traffic_lst[idx] += ex_traffic
                in_traffic_lst[idx] += in_traffic
                hit_lst[idx] += hit
                delay_lst[idx] += delay
        return ex_traffic_lst, in_traffic_lst, hit_lst, delay_lst


    def caching(self):
        for algo in self.algo_lst:
            # algo.clear()
            algo.caching()

