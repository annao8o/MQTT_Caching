from utils.config import *
from utils.GenRequest import *
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

def run(integrated_file):
    env = integrated_file['environment']


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--algo', action='store_true',
                        help='algorithm name.')
    args = vars(parser.parse_args())

    if os.path.exists(file_path + file_name):
        integrated_file = load_file(file_path, file_name)
        # data_list = file['data_list']
        # requests = file['requests']
        # env = file['environment']
        # zipf = file['zipf']
    else:
        data_list = make_data(num_server, num_data, data_size, life_time)
        zipf = Zipf()
        zipf.set_env(zipf_param, num_data)
        requests = make_request_events(num_server, arrival_rate, end_time, zipf, data_list)
        env = Environment(requests, end_time, update_period, num_server, cache_size, arrival_rate, data_list)
        integrated_file = {'data_list': data_list, 'requests': requests, 'zipf': zipf, 'environment': env}

        save_file(file_path, file_name, integrated_file)

    run(integrated_file)