#!/bin/bash
#coding=UTF-8
BASE_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
# 切换到脚本所在目录
cd "$BASE_DIR/.."
source bin/.env
# 切换到脚本所在目录
nohup $PYTHON_HOME ${MAIN_RUN} update >> logs/crontab/run_${PARTITION_DATE}_crontab.log 2>&1 &