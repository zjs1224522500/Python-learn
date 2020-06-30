# -*- coding:utf-8 -*-
import os
import timeit
import multiprocessing
import hashlib


# 计算 md5
def get_hash(f):
    # line=f.readline()
    md5_hash = hashlib.md5()
    while True:
        content = f.read(1024)
        if not content:
            break
        md5_hash.update(content)
    return md5_hash.hexdigest()


# 返回所有文件名
def read_file_name(path, all_file):
    file_list = os.listdir(path)

    for filename in file_list:
        filepath = os.path.join(path, filename)
        # filepath=unicode(filepath,"utf-8")

        if os.path.isdir(filepath):
            read_file_name(filepath, all_file)
        else:
            all_file[filename] = filepath
            # all_file.append(filepath)

    return all_file


def compare_all(files_one, files_two):
    summary_dict = {}
    count = 0
    for file_one in files_one:
        for file_two in files_two:
            # print file_one,file_two
            with open(file_one, 'rb') as f1, open(file_two, 'rb') as f2:
                m1 = get_hash(f1)
                # print m1
                m2 = get_hash(f2)
                # print m2

            if m1 == m2:
                count = count + 1
                print(count)
                print("%s = %s" % (file_one, file_two))

                # add to dict
                summary_dict[file_one] = file_two

                # output file
                filepath = "C://Users/lyh/Desktop/log/0630/link.txt"
                # filepath = 'H:\\RINS1000\\' + 'Link.txt'
                with open(filepath, 'a') as fp:
                    fp.write(file_one.split("\\")[-1] + "\t\t")
                    fp.write(file_two.split("\\")[-1] + "\n")

                fp.close()
            f1.close()
            f2.close()
    print(summary_dict)
    print(len(summary_dict))

    # 取差集
    diff = list(set(files_one).difference(set(summary_dict.keys())))
    print(len(diff))
    for di in diff:
        print(di.split("\\")[-1])
    return summary_dict


def compare_with_same_name(files_one, files_two):
    count = 0
    differ_dict = []
    for file_one in files_one:
        if file_one in files_two:
            with open(files_one[file_one], 'rb') as f1, open(files_two[file_one], 'rb') as f2:
                m1 = get_hash(f1)
                # print m1
                m2 = get_hash(f2)
                if m1 == m2:
                    print("%s same\n" % file_one)
                else:
                    print("%s differ\n" % file_one)
                    count += 1
                    differ_dict.append(file_one)
                f1.close()
                f2.close()
        else:
            print("%s not both.\n" % files_one)
    print("Differ Count: %d" % count)
    print(differ_dict)


#
def begin():
    ff1 = "C://Users/lyh/Desktop/log/0630/file/test (4)/root/tcmu_kv_demo_obj"
    ff2 = "C://Users/lyh/Desktop/log/0630/hcs/hcs (2)/down"
    files_one = {}
    files_one = read_file_name(ff1, files_one)

    files_two = {}
    files_two = read_file_name(ff2, files_two)
    # return compare_all(files_one, files_two)
    return compare_with_same_name(files_one, files_two)


if __name__ == '__main__':
    start = timeit.default_timer()

    pool = multiprocessing.Pool(1)
    pool.apply(func=begin)
    pool.close()
    pool.join()

    end = timeit.default_timer()
    print(str(end - start))

