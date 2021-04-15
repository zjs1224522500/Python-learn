#!/bin/sh

output_file=$1

dd if=/dev/zero of=$output_file bs=1M count=100 conv=fdatasync
dd if=/dev/zero of=$output_file bs=512KB count=100 conv=fdatasync
dd if=/dev/zero of=$output_file bs=256KB count=100 conv=fdatasync
dd if=/dev/zero of=$output_file bs=128KB count=100 conv=fdatasync
dd if=/dev/zero of=$output_file bs=64KB count=100 conv=fdatasync
dd if=/dev/zero of=$output_file bs=32KB count=100 conv=fdatasync
dd if=/dev/zero of=$output_file bs=16KB count=100 conv=fdatasync
dd if=/dev/zero of=$output_file bs=8KB count=100 conv=fdatasync
dd if=/dev/zero of=$output_file bs=4KB count=100 conv=fdatasync
