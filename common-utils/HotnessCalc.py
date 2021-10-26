if __name__ == '__main__':
    file_path = r"C:\Users\Administrator\Desktop\thr-test\hotness.txt"
    file_obj = open(file_path, 'r', encoding='utf-8', errors='ignore')
    lines = file_obj.readlines()

    hotness_map = {}
    hotness_arr = []
    ops = ""
    global_counter = 0
    key_arr = []
    total_hot_map = {}
    # order_dict = {}
    # order_dict = collections.OrderedDict()
    for line in lines:
        line = line.strip().replace('\n', '')
        ops = line.split(" ")
        key = ops[0]
        hotness_map[key] = ops[1]
        hotness_arr.append(int(ops[1]))
        key_split = key.split("_")
        level = key_split[1]
        if level in total_hot_map:
            total_hot_map[level].append(int(ops[1]))
        else:
            total_hot_map[level] = []

    for level in total_hot_map.items():
        print("Level %d" % int(level[0]))
        hot_array = level[1]
        hot_array.sort()
        size = len(hot_array)
        print("Avg: %ld" % (sum(hot_array) / size))
        print("50th: %ld" % hot_array[int(size * 0.5)])
        print("90th: %ld" % hot_array[int(size * 0.9)])
        print("99th: %ld" % hot_array[int(size * 0.99)])

