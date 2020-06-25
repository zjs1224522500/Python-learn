import zipfile
import threading
import numpy as np

global i
i = 0


def extractfile(zfile, password):
    try:
        zfile.extractall(pwd=bytes(password, "utf8"))
        print("文件解压密码为: ", password)
        return password
    except:
        global i
        # i = i + 1
        # print("密码错误第%s次" % i)


def main():
    zfile = zipfile.ZipFile(r'C:\Users\Elvis Zhang\Desktop\624.zip')
    s = np.arange(100.00, 999.99, 0.01)
    for password in s:
        t = threading.Thread(target=extractfile, args=(zfile, password))
        t.start()
        t.join()

    # passfile = open(r'C:\密码字典.txt')
    # for line in passfile.readlines():
    #     Password = line.strip('\n')
    #     t = threading.Thread(target=extractfile, args=(zfile, Password))
    #     t.start()
    #     t.join()


if __name__ == "__main__":
    main()
