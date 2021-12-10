import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import scipy

path = r"C:\Users\Administrator\Desktop\motivation_test\c_l1.txt"

if __name__ == '__main__':
    file_obj = open(path, 'r', encoding='utf-8', errors='ignore')
    lines = file_obj.readlines()
    count = 0
    for line in lines:
        latency_data = line[0:line.find("[")]
        latency_arr = latency_data.split(",")
        len_data = latency_arr.__len__()
        # print("Time: %d second" % count)
        # print("Query count: %d" % len_data)
        result = list(map(int, latency_arr[0:len_data - 1]))
        result_sorted = np.sort(result)

        # print("90th: %d" % result_sorted[int(len(result) * 0.9)])
        # print("99th %d" % result_sorted[int(len(result) * 0.99)])
        # print("99.9th %d" % result_sorted[int(len(result) * 0.999)])
        p99th = result_sorted[int(len(result) * 0.99)]
        # print("99.99th %d" % result_sorted[int(len(result) * 0.9999)])
        # print("Avg %d" % (sum(result_sorted) / (len(result))))
        print("%d-%d" % (count, p99th))
        count += 1
