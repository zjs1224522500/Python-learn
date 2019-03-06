# -*- coding:utf-8 -*-


def trim(string):
    while True:
        if string[:1] == ' ':
            string = string[1:]
        elif string[-1:] == ' ':
            string = string[:-1]
        else:
            break
    return string


# Test case
if trim('hello  ') != 'hello' or trim('  hello') != 'hello' or trim('  hello  ') != 'hello' \
        or trim('  hello  world  ') != 'hello  world' or trim('') != '' or trim('    ') != '':
    print('Failed!')
else:
    print('Success!')
