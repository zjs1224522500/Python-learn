import os
from string import Template

path = r"C:\Users\Administrator\Desktop\thr-test\kept-bf-5w-cf-5w-round2"


class TestData:
    total_throughput = 0.0
    read_throughput = 0.0
    write_throughput = 0.0
    block_cache_promote_ratio = 0.0
    block_hit_ratio = 0.0
    false_positive = 0.0
    block_cache_reuse_ratio = 0.0
    block_cache_hit_ratio = 0.0

    # def __init__(self, total, read, write, promote, hit, fp, reuse, cache_hit):
    #     self.total_throughput = total
    #     self.read_throughput = read
    #     self.write_throughput = write
    #     self.block_cache_hit_ratio = hit
    #     self.block_cache_promote_ratio = promote
    #     self.false_positive = fp
    #     self.block_cache_reuse_ratio = reuse
    #     self.block_hit_ratio = cache_hit


def extract_attr(line, start_str, end_str, is_expresion=False):
    start = 0
    end = 0
    attr = 0.0
    if line.__contains__(start_str):
        start = line.index(start_str)
        if len(end_str) > 0:
            end = line.index(end_str)
            attr = float(line[start + len(start_str):end])
        else:
            if is_expresion:
                attr = float(eval(line[start + len(start_str):]))
            else:
                attr = float(line[start + len(start_str):])
    return attr


def build_test_data(file_name):
    file_path = path + "\\" + file_name
    # print(file_path)
    file_obj = open(file_path, 'r', encoding='utf-8', errors='ignore')
    test_data = TestData()
    lines = file_obj.readlines()
    for line in lines:
        line = line.strip().replace('\n', '')
        if line.__contains__("Write ops: "):
            test_data.write_throughput = extract_attr(line, "Write ops: ", "ops/s") / 1000
        if line.__contains__("Read ops: "):
            test_data.read_throughput = extract_attr(line, "Read ops: ", "ops/s") / 1000
        if line.__contains__("Transaction throughput (KTPS) "):
            test_data.total_throughput = extract_attr(line, "Transaction throughput (KTPS) ", "")
        if line.__contains__("Promote to cache ratio "):
            test_data.block_cache_promote_ratio = extract_attr(line, "Promote to cache ratio ", "", is_expresion=True)
        if line.__contains__("Point Query Block Cache Hit ratio "):
            test_data.block_hit_ratio = extract_attr(line, "Point Query Block Cache Hit ratio ", "", is_expresion=True)
        if line.__contains__("False Poistive Ratio "):
            test_data.false_positive = extract_attr(line, "False Poistive Ratio ", "", is_expresion=True)

    test_data.block_cache_reuse_ratio = 1 - test_data.block_cache_promote_ratio
    test_data.block_cache_hit_ratio = test_data.block_cache_reuse_ratio * (1 - test_data.false_positive)
    return test_data


if __name__ == '__main__':
    test_dict = {}
    format_dict = {}
    for file in os.listdir(path):
        test_dict[file] = build_test_data(file)
    for kv in test_dict.items():
        key = ""
        if kv[0].__contains__("11G"):
            key = kv[0].replace("11G", "12G")
        else:
            key = kv[0]
        print(key, kv[1].__dict__)
        format_dict[key] = kv[1].__dict__

    wo_cache_name = Template("1t-NoCP-NoCache-leveldb-12G-$op_type-100M-$workload.txt")
    cache_10w_name = Template("1t-NoCP-Cache-10w-leveldb-12G-$op_type-100M-$workload.txt")
    pro_20480_name = Template("1t-CP-20480-Cache-10w-leveldb-12G-$op_type-100M-$workload.txt")
    pro_10240_name = Template("1t-CP-10240-Cache-10w-leveldb-12G-$op_type-100M-$workload.txt")
    pro_1024_name = Template("1t-CP-1024-Cache-10w-leveldb-12G-$op_type-100M-$workload.txt")

    data_groups = [wo_cache_name, cache_10w_name, pro_1024_name, pro_10240_name, pro_20480_name]
    workload_type = ['A', 'B', 'C', 'D']
    for data in ["total_throughput", "read_throughput", "write_throughput"]:
        for wl in workload_type:
            if wl == "C":
                ops = "read"
            else:
                ops = "rw"
            for group in data_groups[:3]:
                try:
                    print(str(format_dict[group.substitute(op_type=ops, workload=wl)][data]) + "\t", end="")
                except KeyError:
                    pass

            print("")
            # print(str(format_dict[wo_cache_name.substitute(op_type=ops, workload=wl)][data]) + "\t"
            #       + str(format_dict[cache_10w_name.substitute(op_type=ops, workload=wl)][data]) + "\t"
            #       + str(format_dict[pro_1024_name.substitute(op_type=ops, workload=wl)][data]) + "\t"
            #       + str(format_dict[pro_10240_name.substitute(op_type=ops, workload=wl)][data]) + "\t"
            #       + str(format_dict[pro_20480_name.substitute(op_type=ops, workload=wl)][data]) + "\t")

