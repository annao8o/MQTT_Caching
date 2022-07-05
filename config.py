import random
import math

num_topic = 10
num_sub = 100
num_broker = 10
cache_size = 2   #message
data_size = 1   #message

update_rate = 0.1   #per seconds
arrival_rate = 10   #per seconds
zipf_param = 0.7
end_time = 100

gamma = 1.1

algo_lst = ["proposed", "optimal", "random", "no_caching"]

file_path = 'save/'
file_name = 'test2(brk=10).bin'

