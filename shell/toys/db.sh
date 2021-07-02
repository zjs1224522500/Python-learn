#!/bin/bash

db_set() {
        # 将参数 key,value 写入 数据库文件
        echo "$1,$2" >> database
}

db_get() {
        # grep "^$1," database ：从 database 中查询以 $1 开头的行
        # sed -e "s/^$1,//"：替换 以 $1 开头的 数据为空，即得到 value
        # tail -n 1：显示最后一个结果
        grep "^$1," database | sed -e "s/^$1,//" | tail -n 1
}