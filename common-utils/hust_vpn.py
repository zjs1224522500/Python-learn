# -*- coding: UTF-8 -*-
import os
import re
import sys
import ctypes

deleted_routes = []


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def change_route(routes, bk):
    # 想要代理的 IP
    # routes = ['222.20.xx.xx', '222.20.xx.xx', ]
    print(routes)
    print(bk)

    # 输出 222.20 相关的路由信息
    pipe = os.popen('route print 222.20.*')
    txt = pipe.read()
    # 按照格式匹配
    result = re.search(r' 222.20.* (222.20.*) (222.20.*) ', txt)
    if result:
        # 解析 mask
        mask = result.group(0).split()[1]
        # 读取网关和接口
        gate = result.group(1).strip()
        # 此处的接口为开启 VPN 之后本地获取到的 IP 接口
        inter = result.group(2).strip()

        print(f'mask:{mask} gateway:{gate} interface:{inter}')

        # 读取对应的路由
        pipe = os.popen('route print')
        txt = pipe.readlines()
        print(len(txt))
        for line in txt:
            # 按照空格分割得到结果
            # 正则表达式 [ ]+
            result = re.split('[ ]+', line.strip())
            # print(result)

            # 提取出的数据长度为 5 的行数据，则为路由 (target mask gate interface metric)
            # 只处理 对应路由的网关和接口为我们一开始提取的网关和接口 的路由数据
            # 即找到那些使用了 VPN 的路由
            if len(result) == 5 and result[2].strip() == gate and result[3].strip() == inter:
                para1 = result[0].strip()
                # print(para1)
                # 删除这些使用了 VPN 的路由
                os.system(f'route delete {para1} {gate}')

                # backup
                cmd = 'route add {} mask 255.255.255.255 {}'.format(para1, gate)
                deleted_routes.append(cmd)

        for route in routes:
            print("routes")
            os.system(f'route add {route} mask 255.255.255.255 {gate}')
    else:
        # print('如果重复运行该程序，因主要网关已被清理将无法找到VPN网关，请尝试优化程序或重启VPN。')
        print("err")

    # backup
    # input('input:')
    print("*******Backup******")
    print(len(deleted_routes))
    # input('input:')

    if len(deleted_routes) > 0:
        try:
            bk_fp = open(bk, "w+")
            for line in deleted_routes:
                bk_fp.write(line + "\n")

            bk_fp.close()
        except Exception as e:
            print("open exception: %s: %s" % (e.errno, e.strerror))

    input('input:')


def recover(path):
    fp = open(path)
    for line in fp.readlines():
        if line.startswith("route"):
            os.system(line)

    input('input:')


if __name__ == '__main__':
    # param: bk_file_path, and routes ip
    action = sys.argv[1]
    bk_path = sys.argv[2]
    routes = sys.argv[3:]
    print(action)
    print(bk_path)
    print(routes)
    # input('input:')

    if is_admin():
        print("is admin")
        print("exec ")
        if action == "change":
            change_route(routes, bk_path)
        elif action == "recover":
            recover(bk_path)
    else:
        print("not admin")
        param = __file__ + " " + action + " " + bk_path + " " + " ".join(routes)
        print(param)
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, param, None, 1)
        else:  # in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(param), None, 1)




