import random
import math

num_topic = 100
num_sub = 1000
num_broker = 3
cache_size = 20   #message
data_size = 1   #message

update_rate = 0.01   #per seconds
arrival_rate = 10   #per seconds
zipf_param = 0.7
end_time = 1000

gamma = 1.1

algo_lst = ["proposed", "optimal", "random", "no_caching"]

file_path = 'save/'
file_name = 'test_file_tmp2.bin'

