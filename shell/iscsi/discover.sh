#!/bin/bash

target_ip=$1

echo "=====================Discovery iscsi server======================"
iscsiadm -m discovery -t sendtargets -p $target_ip:3260

