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


## test2

# optimal = np.array([1696, 5454, 9595, 14771, 16518, 20720, 25591, 31428, 33092, 32327])
# proposed = np.array([1702, 5462, 9795, 14929, 17734, 25265, 25604, 32329, 33105, 32339])
# random = np.array([1821, 7060, 11914, 17388, 22465, 26410, 28404, 32865, 39541, 38751])
# nc = np.array([2020, 8338, 14120, 20120, 25140, 31908, 38136, 44458, 52112, 54624])
#
# # total = [234567,232225,237823,256500]
#
# label = np.arange(1, 11)
#
# x = np.arange(len(label))
# plt.plot(label, optimal, label="optimal")
# plt.plot(label, proposed, label="proposed")
# plt.plot(label, random, label='random')
# plt.plot(label, nc, label='nc')
#
# # plt.xticks(x, label)
#
# plt.legend()
# plt.xlabel('The number of brokers')
# plt.ylabel('Traffic')
# plt.title('Traffic Comparison')
#
# plt.show()
# plt.savefig('broker vs Total Traffic.png')
#
# plt.close()


# test3_zipf
'''
optimal1 = np.array([1490, 4412, 8406, 11208, 15472, 18469])
proposed1 = np.array([1430, 4540, 8419, 11401, 15648, 18532])
random1 = np.array([1655, 6595, 12153, 16546, 21322, 25452])
nc1 = np.array([1928, 7686, 14106, 19798, 26180, 31566])

fig, (ax1, ax2) = plt.subplots(1,2)
fig.tight_layout()

label = np.arange(1, 7)

# zipf = 0.7
ax1.plot(label, optimal1, label="optimal")
ax1.plot(label, proposed1, label="proposed")
ax1.plot(label, random1, label='random')
ax1.plot(label, nc1, label='nc')
ax1.set_title('zipf skewness = 0.7')

# zipf = 1.0
optimal2 = np.array([1277, 3893, 6069, 8966, 11245, 14074])
proposed2 = np.array([1332, 3937, 6155, 9062, 11352, 14212])
random2 = np.array([1731, 7343, 12391, 14739, 22025, 26505])
nc2 = np.array([1980, 8184, 14194, 19552, 26178, 31902])

ax2.plot(label, optimal2, label="optimal")
ax2.plot(label, proposed2, label="proposed")
ax2.plot(label, random2, label='random')
ax2.plot(label, nc2, label='nc')
ax2.set_title('zipf skewness = 1.0')

ax1.set(xlabel='The number of brokers', ylabel='Traffic amounts')
ax2.set(xlabel='The number of brokers', ylabel='Traffic amounts')

# plt.xticks(x, label)

plt.legend()

plt.savefig('Test3_zipf.pdf')

plt.close()

'''

# test3_zipf_# of brokers
'''
optimal1 = np.array([0.51659751, 0.572445348, 0.51774461, 0.542582078, 0.518026941, 0.520054155])
proposed1 = np.array([0.51659751, 0.561260803, 0.51774461, 0.539372994, 0.508716323, 0.522084955])
random1 = np.array([0.283195021, 0.359430605, 0.554892206, 0.641816835, 0.659667195, 0.690133694])
nc1 = np.array([0, 0, 0, 0, 0, 0])

fig, (ax1, ax2) = plt.subplots(1,2)
fig.tight_layout()

label = np.arange(1, 7)

# zipf = 0.7
ax1.plot(label, optimal1, label="optimal")
ax1.plot(label, proposed1, label="proposed")
ax1.plot(label, random1, label='random')
ax1.plot(label, nc1, label='nc')
ax1.set_title('zipf skewness = 0.7')

# zipf = 1.0
optimal2 = np.array([0.714141414, 0.679577465, 0.725151806, 0.672930422, 0.70655442, 0.700846192])
proposed2 = np.array([0.71010101, 0.688128773, 0.725151806, 0.672930422, 0.70655442, 0.692550191])
random2 = np.array([0.251515152, 0.402917505, 0.518696069, 0.645251397, 0.74183203, 0.726231956])
nc2 = np.array([0, 0, 0, 0, 0, 0])

ax2.plot(label, optimal2, label="optimal")
ax2.plot(label, proposed2, label="proposed")
ax2.plot(label, random2, label='random')
ax2.plot(label, nc2, label='nc')
ax2.set_title('zipf skewness = 1.0')

# ax1.set(xlabel='The number of brokers', ylabel='Hit ratio')
# ax2.set(xlabel='The number of brokers', ylabel='Hit ratio')
plt.xlabel('The number of brokers')
plt.ylabel('Hit ratio')
# plt.xticks(x, label)

plt.legend()

plt.savefig('Test3_zipf_hit_ratio.pdf')

plt.close()
'''

#test4 - zipf 0~1.0 & traffic
'''
optimal = np.array([22589, 21247, 19628, 19064, 18475, 19628, 19064, 15472, 14020, 11481, 11245])
proposed = np.array([22831, 21342, 19634, 19194, 18523, 19638, 19199, 15648, 14106, 11586, 11352])
random = np.array([21973, 21764, 20869, 20626, 21833, 21251, 20704, 21322, 21333, 21292, 22025])
nc = np.array([26902, 26492, 25752, 25212, 25384, 25752, 25212, 26180, 25782, 25254, 26178])

# total = [234567,232225,237823,256500]

label = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

x = np.arange(len(label))
plt.plot(label, optimal, label="optimal")
plt.plot(label, proposed, label="proposed")
plt.plot(label, random, label='random')
plt.plot(label, nc, label='nc')

# plt.xticks(x, label)

plt.legend()
plt.xlabel('Zipf skewness')
plt.ylabel('Traffic amounts')

plt.show()
plt.savefig('zipf vs Total Traffic.png')

plt.close()
'''

#test4 - zipf 0~1.0 & hit

# optimal = np.array([0.199804114, 0.247341473, 0.287977254, 0.306569343, 0.361587555, 0.278635256, 0.306569343, 0.518026941, 0.568726102, 0.672994489, 0.70655442])
# proposed = np.array([0.185504407, 0.2390705, 0.278635256, 0.305150041, 0.361188672, 0.287977254, 0.305150041, 0.508716323, 0.570738579, 0.672994489, 0.70655442])
# random = np.array([0.691283056, 0.675068925, 0.652112104, 0.687347932, 0.708216992, 0.691510967, 0.725060827, 0.659667195, 0.719058161, 0.691977955, 0.74183203])
# nc = np.array([0,0,0,0,0,0,0,0,0,0,0])

# total = [234567,232225,237823,256500]

# label = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
#
# x = np.arange(len(label))
# plt.plot(label, optimal, label="optimal")
# plt.plot(label, proposed, label="proposed")
# plt.plot(label, random, label='random')
# plt.plot(label, nc, label='nc')
#
# # plt.xticks(x, label)
#
# plt.legend()
# plt.xlabel('Zipf skewness')
# plt.ylabel('Hit ratio')
#
# plt.show()
# plt.savefig('Test4(zipf vs Hit).png')
#
# plt.close()

#test5 - arrival 1~10 & traffic
'''
optimal = np.array([1422, 3053, 3201, 6084, 7588, 9053, 10783, 12889, 13734, 14789])
proposed = np.array([1525, 3133, 3283, 6149, 7639, 9095, 10806, 12900, 13742, 14796])
random = np.array([2093, 4099, 3611, 8269, 10299, 12183, 17006, 18115, 18726, 21133])
nc = np.array([2506, 5118, 5128, 10268, 12818, 15040, 17898, 21612, 22972, 25408])

label = np.arange(1, 11)

x = np.arange(len(label))
plt.plot(label, optimal, label="optimal")
plt.plot(label, proposed, label="proposed")
plt.plot(label, random, label='random')
plt.plot(label, nc, label='nc')

# plt.xticks(x, label)

plt.legend()
plt.xlabel('Arrival rate')
plt.ylabel('Traffic amounts')

plt.savefig('Test5(arrival vs traffic).pdf')

plt.close()
'''

#test5 - arrival 1~10 & hit
'''
optimal = np.array([0.533333333, 0.513513514, 0.498265094, 0.557070707, 0.497441952, 0.512550882, 0.50646366, 0.513416387, 0.515652952, 0.527010561])
proposed = np.array([0.575757576, 0.54954955, 0.530881332, 0.557070707, 0.524596616, 0.545454545, 0.536627406, 0.543124102, 0.542486583, 0.555239643])
random = np.array([0.802020202, 0.77977978, 0.767522554, 0.678282828, 0.702479339, 0.708616011, 0.643493249, 0.553186392, 0.73568873, 0.649675061])
nc = np.array([0,0,0,0,0,0,0,0,0,0])

label = np.arange(1, 11)

x = np.arange(len(label))
plt.plot(label, optimal, label="optimal")
plt.plot(label, proposed, label="proposed")
plt.plot(label, random, label='random')
plt.plot(label, nc, label='nc')

# plt.xticks(x, label)

plt.legend()
plt.xlabel('Arrival rate')
plt.ylabel('Hit ratio')

plt.savefig('Test5(arrival vs hit).pdf')

plt.close()
'''

#test6 - topic 10~100 & hit, traffic

label = np.array([10,20,30,40,50,60,70,80,90,100])

#hit
optimal = np.array([0.384384384, 0.448296593, 0.470136014, 0.463125122, 0.474757474, 0.487144259, 0.492085477, 0.527195027, 0.504665475, 0.527010561])
proposed = np.array([0.384384384, 0.43006012, 0.457125961, 0.451255108, 0.474757474, 0.472031403, 0.485951721, 0.528166278, 0.500893389, 0.555239643])
random = np.array([0.641441441, 0.705410822, 0.737039227, 0.605954466, 0.651554148, 0.638272816, 0.646220815, 0.574009324, 0.718284693, 0.649675061])
nc = np.array([0,0,0,0,0,0,0,0,0,0])

plt.plot(label, optimal, label="optimal")
plt.plot(label, proposed, label="proposed")
plt.plot(label, random, label='random')
plt.plot(label, nc, label='nc')

plt.xlabel('The number of topics')
plt.ylabel('Hit ratio')

plt.legend()

plt.savefig('Test6(topic vs hit).pdf')

plt.close()



#test6 - topic 10~100 & traffic
'''
optimal = np.array([18238, 16636, 16173, 16668, 16232, 16208, 15805, 15642, 15684, 14789])
proposed = np.array([18249, 16778, 16531, 16835, 16286, 16305, 15972, 15679, 15847, 14796])
random = np.array([21678, 20576, 21145, 21900, 21639, 21106, 21830, 23265, 21996, 21133])
nc = np.array([26366, 25844, 26414, 26610, 26378, 26258, 26344, 27276, 26290, 25408])

label = np.array([10,20,30,40,50,60,70,80,90,100])

x = np.arange(len(label))
plt.plot(label, optimal, label="optimal")
plt.plot(label, proposed, label="proposed")
plt.plot(label, random, label='random')
plt.plot(label, nc, label='nc')

# plt.xticks(x, label)

plt.legend()
plt.xlabel('The number of topics')
plt.ylabel('Traffic amounts')

plt.savefig('Test6(topic vs traffic).pdf')

plt.close()
'''

#test7 - cache size & traffic
'''
optimal = np.array([18238, 16636, 16173, 16668, 16232, 16208, 15805, 15642, 15684, 14789])
proposed = np.array([18249, 16778, 16531, 16835, 16286, 16305, 15972, 15679, 15847, 14796])
random = np.array([21678, 20576, 21145, 21900, 21639, 21106, 21830, 23265, 21996, 21133])
nc = np.array([26366, 25844, 26414, 26610, 26378, 26258, 26344, 27276, 26290, 25408])

label = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

x = np.arange(len(label))
plt.plot(label, optimal, label="optimal")
plt.plot(label, proposed, label="proposed")
plt.plot(label, random, label='random')
plt.plot(label, nc, label='nc')

plt.legend()
plt.xlabel('Normalized cache size')
plt.ylabel('Traffic amounts')

plt.show()
plt.savefig('Test7(cache size vs traffic).png')

plt.close()
'''