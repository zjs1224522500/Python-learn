import os

def format_lines(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    lines = file.readlines()
    for i in range(len(lines)):
        line_i = lines[i].strip().replace('\n', '')
        if line_i.startswith(', value length'):
            # print(line_i)
            last_line = lines[i - 1]
            if line_i.__contains__('2021-'):
                other_index = line_i.index('2021-')
            else:
                other_index = line_i.index('21-')
            # new_line = last_line + line_i
            lines[i - 1] = last_line.strip().replace('\n', '') + line_i[0:other_index] + "\n"
            lines[i] = "\n" + lines[i][other_index:]
            # line_i = line_i[other_index:]
            # print(lines[i - 1])
    return lines

def write_lines(file_name, lines):
    if os.path.exists(file_name):
        os.remove(file_name)
    file = open(file_name, 'a+', encoding='utf-8')
    for line in lines:
        file.write(line)
    file.close()


if __name__ == '__main__':
    path_pattern = "C:\\Users\\Administrator\\Desktop\\hikvision\\fio-{}\\tcmu-runner.log"
    for i in range(8):
        path = path_pattern.format(i)
        if os.path.exists(path):
            lines = format_lines(path)
            new_path = path + ".new"
            write_lines(new_path, lines)
        else:
            continue
