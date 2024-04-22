#!/bin/bash
#coding=UTF-8
BASE_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
# 切换到脚本所在目录
cd "$BASE_DIR/.."
source bin/.env


param="$1"
# 执行不同的命令
case $param in
    all)
        nohup $PYTHON_HOME $CHECK_RUN all > retry.log 2>&1 &
        ;;
    update)
        nohup $PYTHON_HOME $CHECK_RUN update > retry.log 2>&1 &
        ;;
    other)
        nohup $PYTHON_HOME $CHECK_RUN other $2 $3 $4 > retry.log 2>&1 &
        ;;
    *)
        echo "Usage: $0 [all|update|other]"
        exit 1
        ;;
esac