import random
import math

num_topic = 100
num_sub = 1000
num_broker = 5
cache_size = 20   #message
data_size = 1   #message

update_rate = 0.1   #per seconds
arrival_rate = 2   #per seconds
zipf_param = 0.7
end_time = 100

gamma = 1.1

algo_lst = ["proposed", "optimal", "random", "no_caching"]

file_path = 'save/'
file_name = 'test5(arrival=2).bin'

flag = 1
env_name = 'test5_env.bin'
req_name = 'test5(arrival=1).bin'