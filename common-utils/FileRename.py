import os

# 图片存放的路径
path = r"D:\实验室\2020.10-系统组月报\2020.10"
date = "202010"

# 遍历更改文件名
for file in os.listdir(path):
    # os.rename(os.path.join(path,file),os.path.join(path,str(num))+".jpg")
    if file.__contains__(date):
        name, month = file.split("-")
        month, docType = month.split(".")
        print(name)
        print(month)
        print(docType)
        new_file_name = str(month + "月报-" + name + "." + docType)
        print(new_file_name)
        os.rename(os.path.join(path, file), os.path.join(path, new_file_name))
        # print(os.path.join(path,file))
    # num = num + 1