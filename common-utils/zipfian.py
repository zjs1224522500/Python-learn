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
        # calculate frequency
        if key in key_dict.keys():
            key_dict[key] = key_dict[key] + 1
        else:
            key_dict[key] = 1
    # sort by frequency of key
    result = dict(sorted(key_dict.items(), key=lambda item: item[1], reverse=True))
    # print(result)
    return result


def calculate_distribution(fre_vals):
    length = len(fre_vals)
    ratios = [0.001, 0.005, 0.01, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
    print("Max freq: %d" % fre_vals[0])
    print("Min freq: %d" % fre_vals[-1])
    txt_format = "ratio {} with frequency {}"
    for ratio in ratios:
        print(txt_format.format(ratio, fre_vals[int(length * ratio)]))


def draw_single(single_path):
    result = calculate_freq(single_path)
    fig_text = single_path
    plt.title(fig_text)
    plt.xticks([])
    plt.ylim((0, 100))
    plt.plot(result.keys(), result.values())
    plt.show()
    print(single_path)
    calculate_distribution(list(result.values()))
    print()


def draw_all(path_arr):
    count = 0
    plot_row = 4
    plot_column = 3
    figure, ax = plt.subplots(plot_row, plot_column)
    for i in range(len(path_arr)):
        result = calculate_freq(path_arr[i])

        # sub_ax = ax[int(count / 4), int(count % 3)]
        # sub_ax.plot(result.keys(), result.values())
        fig_text = ("zip99" if count == 5 else path_arr[count].split(".")[0][-5:])
        # sub_ax.title.set_text(fig_text)
        # sub_ax.set_xticks([])
        fig = plt.subplot(plot_row, plot_column, count + 1)
        plt.xticks([])
        plt.title(fig_text)
        plt.plot(result.keys(), result.values())
        count = count + 1
    plt.show()


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
        r"E:\traces\trace-tem-zip15\test-trace-tem-zip15.txt",
        r"E:\traces\workloadd\test-workloadd.txt"
    ]
    # draw_all(paths)
    # draw_single(paths[-1])
    # draw_single(paths[5])

    native_ycsb_paths = [
        r"E:\traces\workloada-1G-1G\test-workloada-1G-1G.txt",
        r"E:\traces\workloada-1G-0.5G\test-workloada-1G-0.5G.txt",
        r"E:\traces\workloadd-1G-1G\test-workloadd-1G-1G.txt",
        r"E:\traces\workloadd-1G-0.5G\test-workloadd-1G-0.5G.txt",
        r"E:\traces\workloadd-1G-1G\warm-workloadd-1G-1G.txt"
    ]
    # draw_single(native_ycsb_paths[0])
    # draw_single(native_ycsb_paths[1])
    draw_single(native_ycsb_paths[2])
    # draw_single(native_ycsb_paths[3])
    # draw_single(native_ycsb_paths[4])

    # 14 - seq load
    # 12-1 - zipfian write
    # 0 ycsb-a
    # 6 ycsb-d
    kvbench_paths = [
        r"E:\traces\kvbench\ycsb-0.trace",
        r"E:\traces\kvbench\ycsb-12-1.trace",
        r"E:\traces\kvbench\ycsb-14.trace",
        r"E:\traces\kvbench\ycsb-6.trace",
        r"E:\traces\kvbench\ycsb-12-0.trace",
        r"E:\traces\kvbench\ycsb-12-0-0.trace"
        ]
    # draw_single(kvbench_paths[0])
    # draw_single(kvbench_paths[1])
    # draw_single(kvbench_paths[2])
    draw_single(kvbench_paths[3])
    # draw_single(kvbench_paths[4])
    # draw_single(kvbench_paths[5])

    ycsbc_paths = [
        r"E:\traces\ycsbc\ycsba.trace",
        r"E:\traces\ycsbc\ycsbd.trace"
    ]
    # draw_single(ycsbc_paths[0])
    # draw_single(ycsbc_paths[1])

