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
    file_obj = open(file_path, 'r', encoding='utf-8', errors='ignore')
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
        r"E:\traces\trace-tem-zip05\test-trace-tem-zip05.txt",
        r"E:\traces\trace-tem-zip06\test-trace-tem-zip06.txt",
        r"E:\traces\trace-tem-zip07\test-trace-tem-zip07.txt",
        r"E:\traces\trace-tem-zip08\test-trace-tem-zip08.txt",
        r"E:\traces\trace-tem-zip09\test-trace-tem-zip09.txt",
        r"E:\traces\trace-tem\test-trace-tem.txt",
        r"E:\traces\trace-tem-zip11\test-trace-tem-zip11.txt",
        r"E:\traces\trace-tem-zip12\test-trace-tem-zip12.txt",
        r"E:\traces\trace-tem-zip13\test-trace-tem-zip13.txt",
        r"E:\traces\trace-tem-zip14\test-trace-tem-zip14.txt",
        r"E:\traces\trace-tem-zip15\test-trace-tem-zip15.txt"
    ]
    count = 0
    plot_row = 4
    plot_column = 3
    figure, ax = plt.subplots(plot_row, plot_column)
    for i in range(len(paths)):
        result = calculate_freq(paths[i])

        # sub_ax = ax[int(count / 4), int(count % 3)]
        # sub_ax.plot(result.keys(), result.values())
        fig_text = ("zip99" if count == 5 else paths[count].split(".")[0][-5:])
        # sub_ax.title.set_text(fig_text)
        # sub_ax.set_xticks([])
        fig = plt.subplot(4, 3, count + 1)
        plt.xticks([])
        plt.title(fig_text)
        plt.plot(result.keys(), result.values())
        count = count + 1
    plt.show()
