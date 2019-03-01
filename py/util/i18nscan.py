# -*- coding:utf-8 -*-
import os

PATH = "C:\\Users\i348910\eclipse-workspace"
FILES = os.listdir(PATH)
count = 0


class Properties(object):

    def __init__(self, path, file_name):
        self.fileName = path + os.sep + file_name
        self.properties = {}

    def get_properties(self):
        # define null dict
        summary_dict = {}
        # count repeated ke
        global count
        # open file
        pro_file = open(self.fileName, 'Ur')

        # read file line by line
        for line in pro_file.readlines():
            # get str of line
            line = line.strip().replace('\n', '')
            # line is empty or start with # it means it is comment
            if not line or line[0] == '#':
                continue
            # key = value format the str
            key, value = line.split('=')[0], line.split('=')[1]
            # if there is a duplicated key.then print the key and the path
            if key in summary_dict:
                print('Dir - {}  Repeated Key - {}'.format(self.fileName, key))
                count = count + 1
            summary_dict[key] = value


def tree(path, files):
    for file in files:

        # filter useless directory
        if file.startswith('bin') | file.startswith('test') | file.startswith('.') | file.startswith('target'):
            continue
        # use recursion to search directory
        if os.path.isdir(os.path.join(path, file)):
            path2 = path + os.sep + file
            files = os.listdir(path2)
            tree(path2, files)
        else:
            # if there is no file which ends with .properties,continue
            if '.properties' not in file:
                continue
            # only search file start with i18n.properties and get properties
            if file.startswith('i18n.properties'):
                p = Properties(path, file)
                p.get_properties()


def ems(path, files):
    for file in files:
        if file.startswith('ems'):
            path3 = path + os.sep + file
            service = os.listdir(path3)
            # print('service name: {}'.format(file))
            tree(path3, service)
    print(count)


# execute
ems(PATH, FILES)
