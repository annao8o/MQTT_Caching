from config import *
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

    for brk in env.brk_lst:
        brk.print_info()

    ex_input_result = [0 for _ in range(len(algo_lst))]
    ex_output_result = [0 for _ in range(len(algo_lst))]
    in_input_result = [0 for _ in range(len(algo_lst))]
    in_output_result = [0 for _ in range(len(algo_lst))]
    hit_result = [0 for _ in range(len(algo_lst))]
    delay_result = [0 for _ in range(len(algo_lst))]

    # proactive caching
    env.caching()

    t = 0
    while t <= end_time:
        env.load_curr_request(t)

        ex_input_lst, ex_output_lst, in_input_lst, in_output_lst, hit_lst, delay_lst = env.request()
        for i in range(len(algo_lst)):
            ex_input_result[i] += ex_input_lst[i]
            ex_output_result[i] += ex_output_lst[i]
            in_input_result[i] += in_input_lst[i]
            in_output_result[i] += in_output_lst[i]
            hit_result[i] += hit_lst[i]
            delay_result[i] += delay_lst[i]

        t += 1

    result = {f'total_request: {env.total_req}, ex_input: {ex_input_result}, ex_output: {ex_output_result}, in_input: {in_input_result}, in_output: {in_output_result}, hit_count: {hit_result}, '
              f'total_delay: {delay_result}, total_external: {np.array(ex_input_result) + np.array(ex_output_result)}, total_internal: {np.array(in_input_result) + np.array(in_output_result)}, '
              f'total_traffic: {np.array(ex_input_result) + np.array(ex_output_result) + np.array(in_input_result) + np.array(in_output_result)}, '
              f'hit_ratio: {np.array(hit_result) / env.total_req}'}
    print(result)

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--algo', action='store_true',
    #                     help='algorithm name.')
    # args = vars(parser.parse_args())

    if os.path.exists(file_path + file_name):
        integrated_file = load_file(file_path, file_name)

    else:
        zipf = Zipf()
        zipf.set_env(zipf_param, num_topic)
        env = Environment(zipf)
        requests = make_request(num_broker, arrival_rate, end_time, zipf, env.top_lst, env.sub_lst, env.brk_lst)
        env.set_requests(requests)

        integrated_file = {'requests': requests, 'zipf': zipf, 'environment': env}
        save_file(file_path, file_name, integrated_file)

    run(integrated_file, algo_lst)