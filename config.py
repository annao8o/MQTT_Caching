import random
import math

num_topic = 10
num_sub = 10
num_broker = 3
cache_size = 2   #message
data_size = 1   #message

update_rate = 0.01   #per seconds
arrival_rate = 2   #per seconds
zipf_param = 0.7
end_time = 10

gamma = 1.1

algo_lst = ["proposed", "optimal", "random", "no_caching"]

file_path = 'save/'
file_name = 'simple(arrival 2).bin'

