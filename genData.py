from element import Topic
import numpy as np

def make_topic(num_top):
    topic_lst = list()

    for k in range(num_top):
        topic = Topic(k)
        topic_lst.append(topic)

    return topic_lst


def make_request(num_brk, arrival, end_time, zipf, top_lst):
    requests = list()

    t = 0

    while t < end_time:
        req_num = np.random.poisson(arrival, size=num_brk)
        for ...

    requests.sort(key=lambda  x: x[0])  #time

    return requests


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