import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.size'] = 13

missing = 5
delay = 10
i = 2
param = "loss " + str(missing) + "% delay " + str(delay) + "ms "
file_txt = "_" + str(missing) + "_" + str(delay) + ".txt"

fileList = ["cubic", "westwood", "hybla"]
plt.figure(figsize=(10, 5), dpi=100)

timeRes = []
cwndRes = []
ssthRes = []
path = "data/" + fileList[i] + file_txt
f = open(path)
lines = f.readlines()
count = 1
for line in lines:
    words = line.split()
    timeRes.append(float(words[0]))
    cwndRes.append(int(words[6]))
    ssthRes.append(int(words[7]))
    count += 1
    # if count > 10000:
    #     break

y = range(0, 10, 2)

plt.plot(timeRes, cwndRes, linewidth=1, label="拥塞窗口")
plt.plot(timeRes, ssthRes, linewidth=1, label="阈值")
plt.yticks(y)

plt.xlabel("时间/s", fontproperties="SimHei")
plt.ylabel("拥塞窗口大小", fontproperties="SimHei")
plt.title(fileList[i] + " " + param, fontproperties="SimHei")
plt.legend()
f.close()
plt.savefig("photo_4.png")
plt.show()
