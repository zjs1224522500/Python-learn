def search_param(file_name):
    read_length_dict = {}
    write_length_dict = {}
    file = open(file_name, 'r', encoding='utf-8')
    lines = file.readlines()
    for line in lines:
        line = line.strip().replace('\n', '')
        is_read, length = search_length(line)
        if length is not None:
            if is_read:
                counter = read_length_dict.get(length, 0)
                read_length_dict[length] = 1 + counter
            else:
                counter = write_length_dict.get(length, 0)
                write_length_dict[length] = 1 + counter
    return read_length_dict, write_length_dict


def sort_dict_with_value(dict_data):
    return sorted(dict_data.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)


def search_length(line):
    if line.__contains__('[Parameter]'):
        start = line.index("length")
        end = line.index(", offset")
        is_read = line.__contains__('[Parameter] Read')
        return is_read, str(float(float(line[start + 6:end]) / 1024))
    else:
        return True, None


def print_length_dict(dict_data):
    total_size = 0
    total_count = 0
    for (k, v) in dict_data:
        total_size += (float(k) * int(v))
        total_count += int(v)
        print(str(k) + "KB : " + str(v))
    if total_count:
        print("Total count： %d, Average Size: %f KB" % (total_count, (total_size / total_count)))


if __name__ == '__main__':
    path = "C://Users/lyh/Desktop/tcmu-runner (23).log"
    read_dict, write_dict = search_param(path)
    print("**************Read Dict:*****************")
    print_length_dict(sort_dict_with_value(read_dict))
    print("**************Write Dict:****************")
    print_length_dict(sort_dict_with_value(write_dict))


