import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import scipy

path = r"C:\Users\Administrator\Desktop\latency-test\lat-kept-bf\no-d.txt"

if __name__ == '__main__':
    file_obj = open(path, 'r', encoding='utf-8', errors='ignore')
    lines = file_obj.readlines()
    data = lines[0]
    latency_arr = data.split(",")
    len_data = latency_arr.__len__()
    print(len_data)
    print(latency_arr[latency_arr.__len__() - 1])
    # kwargs = {'cumulative': True, 'density': True}
    # sns.set()
    result = list(map(int, latency_arr[0:len_data - 1]))
    # sns.distplot(result, hist=False, hist_kws={'cumulative': True, 'density': True}, kde_kws={'cumulative': True})
    result_sorted = np.sort(result)
    p = np.linspace(0, 1, len(result))
    fig, ax = plt.subplots()
    ax.plot(result_sorted, p)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$p$')

    print(max(result))
    print(min(result))
    print("90th: %d" % result_sorted[int(len(result)*0.9)])
    print("99th %d" % result_sorted[int(len(result)*0.99)])
    print("99.9th %d" % result_sorted[int(len(result)*0.999)])
    print("99.99th %d" % result_sorted[int(len(result)*0.9999)])
    print("Avg %d" % (sum(result_sorted) / (len(result))))

    # x = np.random.randn(200)
    # sns.distplot(x, hist_kws=kwargs, kde_kws=kwargs)
    plt.xlim(xmin=0)
    plt.xlim(xmax=1000)
    # plt.ylim(0, 1)
    plt.show()
