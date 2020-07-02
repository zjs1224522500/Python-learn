def search_param(file_name):
    length_dict = {}
    file = open(file_name, 'r')
    lines = file.readlines()
    for line in lines:
        line = line.strip().replace('\n', '')
        length = search_length(line)
        if length is not None:
            counter = length_dict.get(length, 0)
            length_dict[length] = 1 + counter
    return length_dict


def sort_dict_with_value(dict_data):
    return sorted(dict_data.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)


def search_length(line):
    if line.__contains__('[Parameter]'):
        start = line.index("length")
        end = line.index(", offset")
        return str(int(int(line[start + 6:end]) / 1024))
    else:
        return None


def print_length_dict(dict_data):
    total = 0
    for (k, v) in dict_data:
        total += v
        print(str(k) + "KB : " + str(v))
    print("Average Size: %d KB" % (total / dict_data.__len__()))


if __name__ == '__main__':
    path = "C://Users/lyh/Desktop/tcmu-runner.log"
    print_length_dict(sort_dict_with_value(search_param(path)))

