import os


def read_keys_from_file(path, ops):
    file_obj = open(path, 'r', encoding='utf-8', errors='ignore')
    lines = file_obj.readlines()
    key_set = set()
    for line in lines:
        line = line.replace("\n", "")
        line = line.split(" ")
        if line[0] == ops:
            key_set.add(line[1])
    return key_set


if __name__ == '__main__':
    path1 = r"C:\Users\Administrator\Desktop\test-workloadd-10-10-zip99 (2).txt"
    path2 = r"C:\Users\Administrator\Desktop\warm-workloada-10-10-zip99.txt"
    kset1 = read_keys_from_file(path1, "R")
    kset3 = read_keys_from_file(path1, "I")
    kset2 = read_keys_from_file(path2, "I")
    diff_set = kset1 - kset2
    print("set1 size %d" % len(kset1))
    print("set2 size %d" % len(kset2))
    print("set3 size %d" % len(kset3))
    print("Diff with size: %d" % len(diff_set))
    new_diff = diff_set - kset3
    print("Diff with size: %d" % len(new_diff))

# print(diff_set)

