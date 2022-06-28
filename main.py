from config import *
from element import Zipf
from environment import *
from genData import *
from cacheAlgo import CacheAlgo
import os.path
import pickle
import argparse


def load_file(path, name):
    with open(os.path.join(path, name), 'rb') as f:
        file = pickle.load(f)
        print("success to load the file: %s" % path+name)
    return file

def save_file(path, name, obj):
    with open(os.path.join(path, name), 'wb') as f:
        pickle.dump(obj, f)
    print("Success to generate and save the file: %s" % path+name)

def run(integrated_file, algo_lst):
    env = integrated_file['environment']

    for algo in algo_lst:
        env.add_algo(CacheAlgo(algo, env))

    ex_traffic_result = [0 for _ in range(len(algo_lst))]
    in_traffic_result = [0 for _ in range(len(algo_lst))]
    hit_result = [0 for _ in range(len(algo_lst))]
    delay_result = [0 for _ in range(len(algo_lst))]

    # proactive caching
    env.caching()

    t = 0
    while t <= end_time:
        env.load_curr_request(t)

        ex_traffic_lst, in_traffic_lst, hit_lst, delay_lst = env.requests()
        for i in range(len(algo_lst)):
            ex_traffic_result[i] += ex_traffic_lst[i]
            in_traffic_result[i] += in_traffic_lst[i]
            hit_result[i] += hit_lst[i]
            delay_result[i] += delay_lst[i]

        t += 1

    result = {f'total_request: {env.total_requests}, ex_traffic: {ex_traffic_result}, in_traffic: {in_traffic_result}, hit_count: {hit_result}, '
              f'total_delay: {delay_result}, total_traffic: {np.array(a) + np.array(b)}, hit_ratio: {np.array(hit_result) / env.total_request}'}
    print(result)

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--algo', action='store_true',
    #                     help='algorithm name.')
    # args = vars(parser.parse_args())

    if os.path.exists(file_path + file_name):
        integrated_file = load_file(file_path, file_name)

    else:
        top_list = make_topic(num_topic)
        zipf = Zipf()
        zipf.set_env(zipf_param, num_topic)
        requests = make_request(num_broker, arrival_rate, end_time, zipf, top_list)
        env = Environment(requests, end_time, num_broker, cache_size, arrival_rate, top_list)
        integrated_file = {'topic_list': top_list, 'requests': requests, 'zipf': zipf, 'environment': env}

        save_file(file_path, file_name, integrated_file)

    run(integrated_file, algo_lst)