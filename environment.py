import numpy as np
import random
from element import Broker
import math
from config import *

class Environment:   # load balancer
    def __init__(self, requests, end_time, num_client, num_broker, cache_size, arrival_rate, top_lst):
        self.num_broker = num_broker

        self.brk_lst = list()
        self.client_lst = list()
        self.associate_map = np.zeros((num_client, num_broker), dtype=np.bool_)
        self.total_load = 0
        self.curr_t = 0
        self.end_time = end_time
        self.top_lst = top_lst
        self.algo_lst = list()

        self.requests = requests
        self.curr_req = list()
        self.arrival_rate = arrival_rate

        self.create_env(cache_size)


    def create_env(self, cache_size):
        print("create environment..")

        # generate the brokers
        self.brk_lst = [Broker(i, cache_size, len(self.top_lst), self) for i in range(self.num_broker)]

        # assign a topic(publisher) to a broker
        self.assign_top()

        # assign the subscribers to the brokers
        self.match_sub_broker(self.client_lst)


    def assign_top(self):
        assign_lst = random.uniform(1, self.num_broker, size=len(self.top_lst))
        for top, brk in enumerate(assign_lst):
            brk = math.trunc(brk)
            brk.add_topic(top)

        # for k in self.top_lst:
        #     assign = False
        #     while assign:
        #         brk = self.brk_lst[random.randint()]
        #         if brk.num_top <= len(self.top_lst) / self.num_broker:
        #             brk.add_topic(k)
        #             assign = True

    def match_sub_broker(self, sub):
        if type(sub) == list():
            for s in sub:
                brk = self.brk_lst[random.randint()]
                if self.check_load(brk):
                    brk.add_subscriber(s)
        else:
            brk = self.brk_lst[random.randint()]
            if self.check_load(brk):
                brk.add_subscriber(sub)


    def check_load(self, brk):
        return brk.get_load < gamma * (self.total_load / self.num_broker)


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
            self.brk_lst[req[1]].process_req(req[2])
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

