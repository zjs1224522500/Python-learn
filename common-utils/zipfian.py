#!/usr/bin/python
# -*- coding: UTF-8 -*-

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# x = random.zipf(a=2, size=1000)
# sns.displot(x[x<10], kde=False)
#
# plt.show()


def calculate_freq(file_path):
    file_obj = open(path, 'r', encoding='utf-8', errors='ignore')
    lines = file_obj.readlines()
    key_dict = {}
    for line in lines:
        data = line.split(" ")
        key = data[1].replace("\n", "")
        if key in key_dict.keys():
            key_dict[key] = key_dict[key] + 1
        else:
            key_dict[key] = 1
    result = dict(sorted(key_dict.items(), key=lambda item: item[1], reverse=True))
    print(result)
    return result


if __name__ == '__main__':
    paths = [
        r"C:\Users\Elvis Zhang\Desktop\test-trace-tem-zip05.txt",
        r"C:\Users\Elvis Zhang\Desktop\test-trace-tem.txt",
        r"C:\Users\Elvis Zhang\Desktop\test-trace-tem-zip15.txt"
    ]
    count = 1
    for path in paths:
        result = calculate_freq(path)
        plt.subplot(2, 2, count)
        plt.xticks([])
        plt.plot(result.keys(), result.values())
        count = count + 1
    plt.show()
