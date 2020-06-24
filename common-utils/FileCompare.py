# -*- coding:utf-8 -*-
import os
import timeit
import multiprocessing
import hashlib


# 计算 md5
def getHash(f):
    # line=f.readline()
    md5_hash = hashlib.md5()
    while True:
        # md5_hash.update(line)                                、
        # line=f.readline()
        content = f.read(1024)
        if not content:
            break
        md5_hash.update(content)
    return md5_hash.hexdigest()


# 返回所有文件名
def readFilename(path, all_file):
    file_list = os.listdir(path)

    for filename in file_list:
        filepath = os.path.join(path, filename)
        # filepath=unicode(filepath,"utf-8")

        if os.path.isdir(filepath):
            readFilename(filepath, all_file)
        else:
            all_file.append(filepath)

    return all_file


#
def begin():
    summary_dict = {}
    ff1 = "C://Users//Elvis Zhang//Desktop//file"
    ff2 = "C://Users//Elvis Zhang//Desktop//obj"
    all_jpg1 = []
    all_jpg1 = readFilename(ff1, all_jpg1)
    # print allJPG1

    all_jpg2 = []
    all_jpg2 = readFilename(ff2, all_jpg2)
    # print allJPG2

    count = 0
    for a1 in all_jpg1:
        for b1 in all_jpg2:
            # print a1,b1
            with open(a1, 'rb') as f1, open(b1, 'rb') as f2:
                m1 = getHash(f1)
                # print m1
                m2 = getHash(f2)
                # print m2

            if m1 == m2:
                count = count + 1
                print(count)
                print("%s = %s" % (a1, b1))

                # add to dict
                summary_dict[a1] = b1

                # output file
                filepath = 'C://Users//Elvis Zhang//Desktop//link.txt'
                # filepath = 'H:\\RINS1000\\' + 'Link.txt'
                with open(filepath, 'a') as fp:
                    fp.write(a1.split("\\")[-1] + "\t\t")
                    fp.write(b1.split("\\")[-1] + "\n")

                fp.close()
            f1.close()
            f2.close()
    print(summary_dict)
    print(len(summary_dict))

    # 取差集
    diff = list(set(all_jpg1).difference(set(summary_dict.keys())))
    print(len(diff))
    for di in diff:
        print(di.split("\\")[-1])
    return summary_dict


if __name__ == '__main__':
    start = timeit.default_timer()

    pool = multiprocessing.Pool(1)
    pool.apply(func=begin)
    pool.close()
    pool.join()

    end = timeit.default_timer()
    print(str(end - start))