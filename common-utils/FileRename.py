import os
import time

# 月报存放的路径
actual_month = time.strftime("%Y.%m", time.localtime())
path = r"D:\实验室\{}-系统组月报\{}".format(actual_month, actual_month)
date = actual_month.replace(".", "")

# 遍历更改文件名
for file in os.listdir(path):
    # os.rename(os.path.join(path,file),os.path.join(path,str(num))+".jpg")
    if file.__contains__(date) and not file.startswith(date):
        name, month = file.split("-")
        month, docType = month.split(".")
        print(name.strip())
        print(month.strip())
        print(docType.strip())
        new_file_name = str(month.strip() + "月报-" + name.strip() + "." + docType.strip())
        print(new_file_name)
        os.rename(os.path.join(path, file), os.path.join(path, new_file_name))
        # print(os.path.join(path,file))
    # num = num + 1