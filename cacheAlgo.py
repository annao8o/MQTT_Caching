import numpy as np


class CacheAlgo:
    def __init__(self, name, num_brk, num_top):
        self.algo_name = name
        self.caching_map = np.zeros((num_brk, num_top), dtype=np.bool_)

    def caching(self):
        if self.algo_name == "proposed":
            self.proposed_caching()
        elif self.algo_name == "optimal":
            self.optimal_caching()
        elif self.algo_name == "random":
            self.random_caching()
        elif self.algo_name == "no_caching"
            self.no_Caching()
        print(f'{self.algo_name} caching map is\n{self.caching_map}')


    def calc_traffic(self):
