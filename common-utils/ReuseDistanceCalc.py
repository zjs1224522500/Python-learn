import os
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns
import collections

import statsmodels.api as sm  # recommended import according to the docs

if __name__ == '__main__':
    file_path = r"C:\Users\Elvis Zhang\Desktop\test (3).txt"
    file_obj = open(file_path, 'r', encoding='utf-8', errors='ignore')
    lines = file_obj.readlines()

    key_map = {}
    length_map = {}
    ops = ""
    global_counter = 0
    key_arr = []
    # order_dict = {}
    # order_dict = collections.OrderedDict()
    for line in lines:
        line = line.strip().replace('\n', '')
        ops = line.split(" ")
        key = ops[1]
        key_arr.append(key)
        if ops[0] != 'R':
            continue
        global_counter += 1
        if key not in key_map:
            # start index
            key_map[key] = global_counter
            length_map[key] = []
        else:
            distance = len(set(key_arr[key_map[key]:global_counter - 1]))
            length_map[key].append(distance)
            # length_map[key].append(global_counter - key_map[key] - 1)
            key_map[key] = global_counter
        if global_counter > 1000000:
            break

    duplicate_count = 0
    dist = []
    for kv in length_map.items():
        if len(kv[1]):
            avg = math.ceil(sum(kv[1]) / len(kv[1]))
            # print(kv[0], avg)
            dist.append(avg)
            duplicate_count += 1
        else:
            dist.append(-1)
    print("Total keys: %ld; Unique key: %ld; Duplicated Keys: %ld" % (global_counter, len(length_map), duplicate_count))
    get_once_key = len(length_map) - duplicate_count
    print("Get once: %lf" % (get_once_key / global_counter))
    # =============绘制cdf图===============
    # plt.subplot(121)
    # hist, bin_edges = np.histogram(dist)
    # cdf = np.cumsum(hist)
    # plt.plot(cdf)
    kwargs = {'cumulative': True}
    sns.distplot(dist, hist_kws=kwargs, kde_kws=kwargs)

    plt.axvline(x=2000, ls=":", c="green")  # 添加垂直直线
    plt.axvline(x=5000, ls=":", c="green")  # 添加垂直直线
    plt.axvline(x=10000, ls=":", c="green")  # 添加垂直直线
    # plt.axvline(x=15000, ls=":", c="green")  # 添加垂直直线
    # plt.axvline(x=20000, ls=":", c="green")  # 添加垂直直线
    # plt.axhline(y=0.5, ls=":", c="green")  # 添加垂直直线
    ax = plt.gca()
    ax.get_xaxis().get_major_formatter().set_scientific(False)

    # x_ticks = np.arange(0, 200000, 20000)
    # x_labels = [j / 10000 for j in x_ticks]
    # my_x_ticks = np.arange(0, 10000000, 1000000)
    # labels = [i / 1000000 for i in my_x_ticks]
    # # plt.xticks(my_x_ticks, labels)
    # plt.xlim([-1, 200000])
    # plt.xticks(x_ticks, x_labels)
    plt.show()
