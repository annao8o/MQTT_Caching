import numpy as np
from config import *
import copy


class CacheAlgo:
    def __init__(self, name, env):
        self.name = name
        self.env = env
        self.caching_map = np.zeros((num_broker, num_topic), dtype=np.bool_)
        self.remain_capacity = np.full(num_broker, cache_size, dtype=np.int_)

    def caching(self):
        if self.name == "proposed":
            self.proposed_caching()
        elif self.name == "optimal":
            self.optimal_caching()
        elif self.name == "random":
            self.random_caching()
        elif self.name == "no_caching":
            self.no_caching()
        print(f'{self.name} caching map is\n{self.caching_map}')

    def isFull(self):
        avail_svr = list()
        for idx, value in enumerate(self.remain_capacity):
            # print(idx, value)
            if value > 0:
                avail_svr.append(idx)
                # print("available", idx)
        return avail_svr

    def proposed_caching(self):
        topic_lst = list()
        for top in self.env.top_lst:
            topic_lst.append((top, top.popularity))
        # sort the topics with popularity in descending order
        topic_lst.sort(key=lambda x: x[1], reverse=True)
        for (t, p) in topic_lst:
            avail_svr = self.isFull()
            # print(avail_svr)
            if len(avail_svr) == 0:
                break
            traffic = 0
            min_traffic = float('inf')
            min_broker = None
            for brk in avail_svr:
                # print("avail: ", avail_svr, "brk : ", brk)
                traffic = self.calc_total_traffic(brk, t.id)
                # print("broker: ", brk, "curr_traffic:", traffic, "min_traffic: ", min_traffic)
                if traffic < min_traffic:
                    min_traffic = traffic
                    min_broker = brk
            self.data_store(min_broker, t.id)


    def optimal_caching(self):  #brute force
        while True:
            avail_svr = self.isFull()
            if len(avail_svr) == 0:
                break
            temp = np.zeros((num_broker, num_topic), dtype=np.float_)
            traffic = 0
            min_traffic = float('inf')
            min_set = (None,None)
            for top in self.env.top_lst:
                for brk in avail_svr:
                    traffic = self.calc_total_traffic(brk, top.id)
                    if (traffic < min_traffic) and (self.caching_map[brk][top.id] != True):
                        min_traffic = traffic
                        min_set = (brk, top.id)
            self.data_store(min_set[0], min_set[1])


            # for top in self.env.top_lst:  #topic: obj
            #     for brk in avail_svr:
            #         traffic = self.calc_total_traffic(brk, top.id)
            #         temp[brk][top.id] = traffic
            # min_idx = np.argwhere(temp==np.min(temp[np.nonzero(temp)]))[0]    #caching 이 안되어 있는 곳을 선택해야 함.
            # print(min_idx)
            # self.data_store(int(min_idx[0]), int(min_idx[1]))


    def random_caching(self):
        for brk in range(num_broker):
            while self.remain_capacity[brk] > 0:
                top = random.randrange(num_topic)
                if self.caching_map[brk][top]:
                    continue
                self.data_store(brk, top)


    def no_caching(self):
        return


    def calc_total_traffic(self, broker, topic):
        ex_input = ex_output = in_output = in_input = 0
        # print(self.caching_map.copy())
        tmp_caching_map = copy.deepcopy(self.caching_map)
        tmp_caching_map[broker][topic] = True
        # print(broker, topic, tmp_caching_map)

        ex_input_result = ex_output_result = in_output_result = in_input_result = 0
        for b in range(num_broker):
            ex_input = ex_output = in_output = in_input = 0
            for k in range(num_topic):
                ex_input += self.calc_ex_input(b,k, tmp_caching_map)
                ex_output += self.calc_ex_output(k)
                in_output += self.calc_in_output(b,k, tmp_caching_map)
                in_input += self.calc_in_input(b,k, tmp_caching_map)
            ex_input_result = ex_input
            ex_output_result = self.env.brk_lst[b].get_load() * ex_output
            in_output_result = in_output
            in_input_result = in_input
        total_traffic = ex_input_result + ex_output_result + in_output_result + in_input_result

        return total_traffic


    def calc_ex_input(self, broker, topic, tmp_map):
        return self.env.asso_map[broker][topic] * (tmp_map[broker][topic] * update_rate + (1 - tmp_map[broker][topic] * self.env.lambda_map[topic]))


    def calc_ex_output(self, topic):
        return self.env.lambda_map[topic]


    def calc_in_output(self, broker, topic, tmp_map):
        # n = self.env.brk_lst[broker].get_load()
        # print(n)
        # prob_sub = 0
        # for i in range(n):
        #     print(1/num_broker)
        #     print(np.random.binomial(i+1, n, 1/num_broker))
        #     print(1 - (1 - self.topic_lst[topic].get_popularity())**(i+1))
        #     prob_sub += (np.random.binomial(i+1, n, 1/num_broker) * (1 - (1 - self.topic_lst[topic].get_popularity())**(i+1)))
        # return prob_sub * self.env.lambda_map[topic] * abs(1 - (self.env.asso_map[broker][topic] + tmp_map[broker][topic]))
        return 1


    def calc_in_input(self, broker, topic, tmp_map):
        caching_svr = np.where(tmp_map[:, topic] == True)[0]
        if len(caching_svr) != 0:
            return (self.env.lambda_map[topic] * (
                    tmp_map[broker][topic] + (1 - tmp_map[broker][topic]) * self.env.asso_map[broker][topic])) / len(
                caching_svr)
        else:
            return (self.env.lambda_map[topic] * (
                    tmp_map[broker][topic] + (1 - tmp_map[broker][topic]) * self.env.asso_map[broker][topic]))


    def data_store(self, svr, item):
        if type(item) == np.ndarray:
            self.caching_map[svr] = item
        elif type(item) == int:
            self.caching_map[svr][item] = True
        elif type(item) == list:
            for i in item:
                self.caching_map[svr][i] = True
        else:
            raise Exception("type error in func data_store(): data must be integer or list.")
        self.remain_capacity[svr] -= data_size
        # print(f'caching {item} in {svr}, {self.caching_map}')


    def process_req(self, req):     #req=(t, svr, requested_top)
        req_brk = req[1]
        req_top = req[2]
        cached_svr = np.where(self.caching_map[:, req_top.id] == True)[0]  # Find the brokers caching the requested topic
        delay = 0

        if len(cached_svr) != 0:  # If the requested topic is cached in one of the brokers
            hit = 1
            if req_brk in cached_svr:   # cached in the requesting broker
                #ex_traffic = req_brk.forward()  #requesting broker the forwards the user directly
                ex_traffic = 1
                in_traffic = 0
            else:
                # in_traffic = req_brk.routing()
                in_traffic = 2
                ex_traffic = 1

        else:   # If the requested topic is not cached in any broker
            hit = 0
            connected_svr = req_top.get_svr()
            if connected_svr.id == req_brk:
                ex_traffic = 2
                in_traffic = 0
            else:
                ex_traffic = 2
                in_traffic = 2

        return ex_traffic, in_traffic, hit, delay
