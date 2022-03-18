import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import scipy

path = r"C:\Users\Elvis Zhang\Desktop\lat-test\c_l1 (2).txt"

if __name__ == '__main__':
    file_obj = open(path, 'r', encoding='utf-8', errors='ignore')
    lines = file_obj.readlines()
    count = 0
    total_latency_list = []
    for line in lines:
        latency_data = line[0:line.find("[")]
        latency_arr = latency_data.split(",")
        len_data = latency_arr.__len__()
        # print("Time: %d second" % count)
        # print("Query count: %d" % len_data)
        result = list(map(int, latency_arr[0:len_data - 1]))
        total_latency_list += result
        result_sorted = np.sort(result)
        qps = result.__len__()
        # print("90th: %d" % result_sorted[int(len(result) * 0.9)])
        # print("99th %d" % result_sorted[int(len(result) * 0.99)])
        # print("99.9th %d" % result_sorted[int(len(result) * 0.999)])
        avg_lat = sum(result_sorted) / qps
        lat_ratio_1 = [0.5, 0.6, 0.7, 0.8]
        lat_ratio_2 = [0.90, 0.95, 0.99, 0.999]
        p90th = result_sorted[int(qps * lat_ratio_1[0])]
        p95th = result_sorted[int(qps * lat_ratio_1[1])]
        p99th = result_sorted[int(qps * lat_ratio_1[2])]
        p999th = result_sorted[int(qps * lat_ratio_1[3])]
        # print("99.99th %d" % result_sorted[int(len(result) * 0.9999)])
        # print("Avg %d" % (sum(result_sorted) / (len(result))))
        print("%d-%d-%d-%d-%d-%d-%d" % (count, qps, avg_lat, p90th, p95th, p99th, p999th))
        count += 1
    total_read = len(total_latency_list)
    avg_lat = sum(total_latency_list) / total_read
    total_latency_list = np.sort(total_latency_list)
    p90th = total_latency_list[int(total_read * 0.9)]
    p99th = total_latency_list[int(total_read * 0.99)]
    p999th = total_latency_list[int(total_read * 0.999)]
    print("%d-%d-%d-%d-%d" % (total_read, avg_lat, p90th, p99th, p999th))
