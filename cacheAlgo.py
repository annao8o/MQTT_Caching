import numpy as np


class CacheAlgo:
    def __init__(self, name, num_brk, num_top):
        self.name = name
        self.num_top = num_top
        self.num_broker = num_brk
        self.caching_map = np.zeros((num_brk, num_top), dtype=np.bool_)

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


    def proposed_caching(self):
        topic_lst = ist()
        for top in self.top_lst:
            topic_lst.append((top, top.popularity))
        # sort the topics with popularity in descending order
        topic_lst.sort(key=lambda x: x[1], reverse=True)
        for (t, p) in topic_lst:
            avail, avail_svr = self.isFull()
            if avail is False:
                break
            min_traffic = float('inf')
            min_broker = 0
            for brk in avail_svr:
                traffic = self.calc_traffic(brk, top)
                if traffic < min_traffic:
                    min_traffic = traffic
                    min_broker = brk
            self.data_store(min_broker, top)

        return

    # eta 만큼 update
    def update_cache(self):

        return

    def optimal_caching(self):  #brute force
        return


    def random_caching(self):
        return


    def no_caching(self):
        return


    def calc_total_traffic(self, broker, topic):
        ex_input = ex_output = in_output = in_input = 0
        tmp_caching_map = self.caching_map.copy()
        tmp_caching_map[broker][topic] = True

        for b in range(self.num_broker):
            for k in range(self.num_top):
                ex_input += self.calc_ex_input(b,k)
                ex_output += self.calc_ex_output(b,k)
                in_output += self.calc_in_output(b,k)
                in_input += self.calc_in_input(b,k)

        total_traffic = ex_input + ex_output + in_output + in_input

        return total_traffic

    def calc_ex_input(self, broker, topic):


        return


    def calc_ex_output(self, broker, topic):


        return


    def calc_in_output(self, broker, topic):


        return


    def calc_in_input(self, broker, topic):


        return


    def isFull(self):
        avail_flag = False
        avail_svr = list()
        for idx, value in enumerate(self.remain_capacity):
            if value > 0:
                avail_svr.append(idx)
                avail_flag = True
        return avail_flag, avail_svr


    def data_store(self, svr, item):
        if type(item) == np.ndarray:
            self.caching_map[svr] = item
        elif type(item) == int:
            self.caching_map[svr][item] = True
        elif type(item) == list:
            for i in item:
                self.caching_map[svr][i] = True
        else:
            raise Exception("type error in data_store() function): data must be integer or list.")


    def process_req(self, req):     #req=(t, svr, requested_top)
        req_brk = req[1]
        req_top = req[2]
        cached_svr = np.where(self.caching_map[:, req_top.id] == True)[0]  # Find the brokers caching the requested topic
        delay = 0

        if cached_svr:  # If the requested topic is cached in one of the brokers
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
