#!/bin/bash

output_file=$1

fio -numjobs=16 -bs=4k -ioengine=libaio -iodepth=32 -direct=1 -rw=randwrite -time_based -runtime=20 -refill_buffers -norandommap -randrepeat=0 -group_reporting -name=fio-randwrite-iops -filename=$output_file
fio -numjobs=16 -bs=4k -ioengine=libaio -iodepth=32 -direct=1 -rw=randread -time_based -runtime=20 -refill_buffers -norandommap -randrepeat=0 -group_reporting -name=fio-randread-iops -filename=$output_file
fio --numjobs=16 -bs=128k -ioengine=libaio -iodepth=32 -direct=1 -rw=write -time_based -runtime=20 -refill_buffers -norandommap -randrepeat=0 -group_reporting -name=fio-write-throughput -filename=$output_file
fio --numjobs=16 -bs=128k -ioengine=libaio -iodepth=32 -direct=1 -rw=read -time_based -runtime=20 -refill_buffers -norandommap -randrepeat=0 -group_reporting -name=fio-read-throughput -filename=$output_file
fio --numjobs=16 -bs=4k -ioengine=libaio -iodepth=1 -direct=1 -rw=randwrite -time_based -runtime=20 -refill_buffers -norandommap -randrepeat=0 -group_reporting -name=fio-randwrite-lat -filename=$output_file
fio --numjobs=16 -bs=4k -ioengine=libaio -iodepth=1 -direct=1 -rw=randread -time_based -runtime=20 -refill_buffers -norandommap -randrepeat=0 -group_reporting -name=fio-randread-lat -filename=$output_file

