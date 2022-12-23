# -*- coding: UTF-8 -*-
import os
import re
import sys


# 想要代理的 IP
# routes = ['222.20.xx.xx', '222.20.xx.xx', ]
routes = sys.argv[1:]
print(routes)

txt = os.popen('route print 222.20.*')
txt = txt.read()
result = re.search(r' 222.20.* (222.20.*) (222.20.*) ', txt)
if result:
    mask = result.group(0).split()[1]
    # 读取网关和接口
    gate = result.group(1).strip()
    # 此处的接口为开启 VPN 之后本地获取到的 IP 接口
    inter = result.group(2).strip()

    print(f'mask:{mask} gateway:{gate} interface:{inter}')

    # 读取对应的路由
    txt = os.popen('route print')
    txt = txt.readlines()
    for line in txt:
        # 按照空格分割得到结果
        # 正则表达式 [ ]+
        result = re.split('[ ]+', line.strip())
        # print(result)

        # 提取出的数据长度为 5 的行数据，则为路由
        # 只处理 对应路由的网关和接口为我们一开始提取的网关和接口 的路由数据
        # 即找到那些使用了 VPN 的路由
        if len(result) == 5 and result[2].strip() == gate and result[3].strip() == inter:
            para1 = result[0].strip()
            # print(para1)
            # 删除这些使用了 VPN 的路由
            os.system(f'route delete {para1} {gate}')

    for route in routes:
        print("routes")
        os.system(f'route add {route} mask 255.255.255.255 {gate}')
else:
    # print('如果重复运行该程序，因主要网关已被清理将无法找到VPN网关，请尝试优化程序或重启VPN。')
    print("err")