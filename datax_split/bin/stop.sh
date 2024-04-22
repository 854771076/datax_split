#!/bin/bash
#coding=UTF-8
BASE_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
# 切换到脚本所在目录
cd "$BASE_DIR/.."
source bin/.env
kid=`ps -ef |grep $MAIN_RUN| grep -v "grep"|awk '{print $2}'`
kill -9 $kid
if [ "$?" -eq 0 ]; then
    echo "kill成功，pid:"$kid
else
    echo "kill失败，没有找到对应的进程"
fi