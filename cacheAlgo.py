import numpy as np
from config import *
import copy
from itertools import combinations

random.seed(1)


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
        for (t, p) in topic_lst:    # popularity 높은 것 부터.
            avail_svr = self.isFull()
            # print(avail_svr)
            if len(avail_svr) == 0:
                break
            min_traffic = float('inf')
            min_brk_set = None
            for n in range(len(avail_svr)):
                combi = list(combinations(avail_svr, n+1))
                for brk_set in combi:
                    traffic = self.calc_total_traffic(brk_set, t.id)
                    if traffic < min_traffic:
                        min_traffic = traffic
                        min_brk_set = brk_set
            # print("algorithm: ", self.name, "topic: ", t.id, "min comb: ", min_brk_set)
            self.data_store(min_brk_set, t.id)


            # # for c in combi:
            # #     for idx in c:
            #
            # for brk in avail_svr:
            #     # print("avail: ", avail_svr, "brk : ", brk)
            #     traffic = self.calc_total_traffic(brk, t.id)
            #     # print("broker: ", brk, "curr_traffic:", traffic, "min_traffic: ", min_traffic)
            #     if traffic < min_traffic:
            #         min_traffic = traffic
            #         min_broker = brk
            # self.data_store(min_broker, t.id)


    def optimal_caching(self):  #brute force
        while True:
            avail_svr = self.isFull()
            if len(avail_svr) == 0:
                break
            min_traffic = float('inf')
            min_set = (None,None)
            for top in self.env.top_lst:
                for n in range(len(avail_svr)):
                    combi = list(combinations(avail_svr, n + 1))
                    for brk_set in combi:
                        traffic = self.calc_total_traffic(brk_set, top.id)
                        # print("current: ", top.id, brk_set, traffic)
                        # print("min: ", min_set, min_traffic)
                        if traffic < min_traffic:
                            min_traffic = traffic
                            min_brk_set = brk_set
                            min_set = (min_brk_set, top.id)
            # print("algorithm: ", self.name, " topic: ", min_set[1], " min comb: ", min_set[0])
            self.data_store(min_set[0], min_set[1])

            # for top in self.env.top_lst:
            #     for brk in avail_svr:
            #         traffic = self.calc_total_traffic(brk, top.id)
            #         if (traffic < min_traffic) and (self.caching_map[brk][top.id] != True):
            #             min_traffic = traffic
            #             min_set = (brk, top.id)
            # self.data_store(min_set[0], min_set[1])


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


    def calc_total_traffic(self, broker_set, topic):
        # print(self.caching_map.copy())
        tmp_caching_map = copy.deepcopy(self.caching_map)
        if type(broker_set) == tuple:
            for broker in broker_set:
                tmp_caching_map[broker][topic] = True
        elif type(broker_set) == int:
            tmp_caching_map[broker_set][topic] = True

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

        # print(ex_input_result, ex_output_result, in_output_result, in_input_result)
        total_traffic = ex_input_result + ex_output_result + in_output_result + in_input_result

        return total_traffic


    def calc_ex_input(self, broker, topic, tmp_map):
        return self.env.asso_map[broker][topic] * (tmp_map[broker][topic] * self.env.asso_map[broker][topic] * update_rate + (1 - tmp_map[broker][topic] * self.env.lambda_map[topic]))


    def calc_ex_output(self, topic):
        return self.env.lambda_map[topic]


    def calc_in_output(self, broker, topic, tmp_map):
        n = self.env.brk_lst[broker].get_load()
        p = (1 - (1 - self.env.top_lst[topic].get_popularity())**n)

        # prob_sub = 0
        # for i in range(n):
        #     prob_sub += (np.random.binomial(i+1, 1/num_broker, n) * (1 - (1 - self.env.top_lst[topic].get_popularity())**(i+1)))
        return p * self.env.lambda_map[topic] * abs(1 - (self.env.asso_map[broker][topic] + tmp_map[broker][topic]))


    def calc_in_input(self, broker, topic, tmp_map):
        caching_svr = np.where(tmp_map[:, topic] == True)[0]
        if len(caching_svr) != 0:
            return (self.env.lambda_map[topic] * (
                    tmp_map[broker][topic] + (1 - tmp_map[broker][topic]) * self.env.asso_map[broker][topic])) / len(
                caching_svr)
        else:
            return (self.env.lambda_map[topic] * (
                    tmp_map[broker][topic] + (1 - tmp_map[broker][topic]) * self.env.asso_map[broker][topic]))


    def data_store(self, broker_set, topic):
        if type(broker_set) == tuple:
            for broker in broker_set:
                self.caching_map[broker][topic] = True
                self.remain_capacity[broker] -= data_size
        elif type(broker_set) == int:
            self.caching_map[broker_set][topic] = True
            self.remain_capacity[broker_set] -= data_size

        # if type(item) == np.ndarray:
        #     self.caching_map[svr] = item
        # elif type(item) == int:
        #     self.caching_map[svr][item] = True
        # elif type(item) == list:
        #     for i in item:
        #         self.caching_map[svr][i] = True
        # else:
        #     raise Exception("type error in func data_store(): data must be integer or list.")
        # self.remain_capacity[svr] -= data_size
        # # print(f'caching {item} in {svr}, {self.caching_map}')


    def process_req(self, req):     #req=(time, broker, topic)
        req_brk = req.broker
        req_top = req.topic
        cached_svr = np.where(self.caching_map[:, req_top.id] == True)[0]  # Find the brokers caching the requested topic
        topic_svr = self.env.brk_lst[np.where(self.env.asso_map[:, req_top.id] == True)[0][0]] # Find the brokers having the requested topic
        delay = 0

        ex_input = ex_output = in_input = in_output = 0
        # print(f'algorithm: {self.name}// request for {req_top.id} arrives {req_brk.id}')

        if len(cached_svr) != 0:  # If the requested topic is cached in one of the brokers
            hit = 1
            if req_brk.id in cached_svr:   # cached in the requesting broker
                req_brk.forward(req)  #requesting broker the forwards the user directly
            else:   # 다른 broker에 캐싱되어 있으면
                target_brk = self.env.brk_lst[cached_svr[random.randrange(len(cached_svr))]] # target broker 설정하고
                req_brk.routing(target_brk)    # target broker에 routing
                target_brk.routing(req_brk)
                req_brk.forward(req)

        else:   # If the requested topic is not cached in any broker
            hit = 0
            # print(req_top.id, "is cached in ", req_top.get_svr().id)
            if req_brk.id == topic_svr.id:
                req_brk.fetch()
                req_brk.forward(req)
            else:
                req_brk.routing(topic_svr) #topic server에 routing
                topic_svr.fetch() #topic server는 publisher로부터 data fetch
                topic_svr.routing(req_brk)   # topic server는 Data를 requesting broker에 routing
                req_brk.forward(req)

        for brk in self.env.brk_lst:
            ex_in, ex_out, in_in, in_out = brk.get_traffic()

            ex_input += ex_in
            ex_output += ex_out
            in_input += in_in
            in_output += in_out
            brk.clear()

        return ex_input, ex_output, in_input, in_output, hit, delay

    def update(self):
        cached_items = np.where(self.caching_map == True)[1]
        cached_items = set(cached_items)
        # print(self.name, cached_items)

        for item in cached_items:
            asso_svr = np.where(self.env.asso_map[:, item] == True)[0]
            # print(self.name, item, asso_svr)
            for svr in asso_svr:
                self.env.brk_lst[svr].fetch()

