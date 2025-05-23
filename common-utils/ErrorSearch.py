import os


def search_param(file_name):
    error_code_dict = {}
    src_file = open(file_name, 'r', encoding='utf-8')
    lines = src_file.readlines()
    for line in lines:
        line = line.strip().replace('\n', '')
        err_code = search_error_code(line)
        if err_code is not None:
            counter = error_code_dict.get(err_code, 0)
            error_code_dict[err_code] = 1 + counter

    return error_code_dict


def search_error_code(line):
    input_word = 'failed ret:'
    if line.__contains__(input_word):
        start = line.index(input_word)
        end = line.index(",bucket")
        return str(line[start + 11:end])
    else:
        return None


def merge_dict(dict1, dict2):
    return dict2.update(dict1)


if __name__ == '__main__':
    dir = "C:\\Users\\Elvis Zhang\\Desktop\\hik\\fio\\"
    files = os.listdir(dir)
    total_err = {}
    for file in files:
        if file.__contains__("rainbow_error.log"):
            path = dir + file
            err_dict = search_param(path)
            merge_dict(err_dict, total_err)
    print(total_err)
