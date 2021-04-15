#!/bin/bash

cd
echo "=====================Umount============================"
umount /home/testuser/shunzitest

echo "=====================iscsi logout======================"
cd /home/testuser/shun
./logout.sh

echo "=====================Check disks======================="
fdisk -l

