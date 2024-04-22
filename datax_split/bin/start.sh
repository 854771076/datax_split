#!/bin/bash
#coding=UTF-8
BASE_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
# 切换到脚本所在目录
cd "$BASE_DIR/.."
source bin/.env


# 获取参数值
param="$1"
# 执行不同的命令
case $param in
    all)
        nohup python3 ${MAIN_RUN} all > running.log 2>&1 &
        ;;
    update)
        nohup python3 ${MAIN_RUN} update > running.log 2>&1 &
        ;;
    other)
        nohup python3 ${MAIN_RUN} other $2 $3 $4 > running.log 2>&1 &
        ;;
    *)
        echo "Usage: $0 [all|update|other]"
        exit 1
        ;;
esac
tail -f running.log