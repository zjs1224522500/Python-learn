import json

str = "--db=/mnt/hd0/shunzi/lsbmdb/temp-test --use_existing_db=1 --monitor_log=/mnt/hd0/shunzi/lsbmdb/D-test-log --compaction_min_score=1 --file_size=2 \
--write_buffer_size=64 --data_merged_each_round=8 \
--compaction_buffer_length=231 --compaction_buffer_length=232 --compaction_buffer_length=13 \
--range_portion=0 --range_size=100 --max_print_level=3  --print_version_info=1 --print_compaction_buffer=1 --print_dash=1 --hitratio_interval=1 \
--hot_ratio=100 --read_portion=95 --num=100 --throughput=-1 --benchmarks=mix --preload_metadata=1 --open_files=1000 --hot_file_threshold=256 \
\
 --read_key_from=0 --read_key_upto=10485760 --write_key_from=0 --write_key_upto=10485760 --key_from=0 --key_upto=10485760 \
 --block_cache_size=270 --key_cache_size=0 --warmup=0 --read_workload=latest --write_workload=latest --readspeed=-1 --writespeed=-1 \
--read_threads=0 --random_reads=-1 --writes=10485760 --countdown=25000 --noise_percent=0  --buffered_merge=1"


def cmd2json(input_str, start_symbol, contain_symbol):
    json_dict = {}
    param_array = input_str.split()
    str_arr = []
    for param in param_array:
        start_index = param.index(start_symbol)
        if start_index == 0:
            key_value = param if contain_symbol else param[start_index + len(start_symbol):]
            kv_array = key_value.split("=")
            json_dict[kv_array[0] + "="] = kv_array[1]
            str_arr.append("\"" + kv_array[0] + "=" + kv_array[1] + "\"")

    # output_str = json.dumps(json_dict)
    output_str = ""
    for e in str_arr:
        output_str += (e + ",")
    return output_str


if __name__ == '__main__':
    output = cmd2json(str, "--", True)

    print(output.replace(":", ","))


