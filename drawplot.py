import numpy as np
import matplotlib.pyplot as plt

# external = np.array([68959, 94541, 81475, 100980])
# internal = np.array([165608/2, 137684/2, 156348/2, 155520/2])
# # total = [234567,232225,237823,256500]
#
# label = ['proposed', 'optimal', 'random', 'no']
#
# x = np.arange(len(label))
# plt.bar(x-0.1, external, label='external', width=0.2, color='blue')
# plt.bar(x+0.1, internal, label='internal', width=0.2, color='red')
# # plt.bar(x, total)
# plt.xticks(x, label)
#
# plt.legend()
# plt.xlabel('Algorithm')
# plt.ylabel('Traffic')
# plt.title('Traffic Comparison')
#
# plt.show()
# plt.savefig('Total Traffic.png')
#
# plt.close()


## plot

optimal = np.array([1696, 5454, 9595, 14771, 16518, 20720, 25591, 31428, 33092, 32327])
proposed = np.array([1702, 5462, 9795, 14929, 17734, 25265, 25604, 32329, 33105, 32339])
random = np.array([1821, 7060, 11914, 17388, 22465, 26410, 28404, 32865, 39541, 38751])
nc = np.array([2020, 8338, 14120, 20120, 25140, 31908, 38136, 44458, 52112, 54624])

# total = [234567,232225,237823,256500]

label = np.arange(1, 11)

x = np.arange(len(label))
plt.plot(label, optimal, label="optimal")
plt.plot(label, proposed, label="proposed")
plt.plot(label, random, label='random')
plt.plot(label, nc, label='nc')

# plt.xticks(x, label)

plt.legend()
plt.xlabel('The number of brokers')
plt.ylabel('Traffic')
plt.title('Traffic Comparison')

plt.show()
plt.savefig('broker vs Total Traffic.png')

plt.close()