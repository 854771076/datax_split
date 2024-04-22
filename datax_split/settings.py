
environment = 'dev'
if environment == 'dev':
    READER_MYSQL_CONNECT = {
        'host': '',
        'port': 3306,
        'user': '',
        'password': '',
        'charset': 'utf8',
    }
    MYSQL_CONNECT = {
        'host': '',
        'port': 3306,
        'user': 'root',
        'password': '',
        'charset': 'utf8',
        'db': 'logs'
    }
    # python版本
    python = 'python'
    DATAX_BIN_PATH = 'd://datax/bin/datax.py'

    # 日志配置
    log_tb_name = "t_mysql2ods_executed_sync_log"
    log_name = f'{log_tb_name}-all.log'
    error_log_name = f'{log_tb_name}-all.error.log'
    # 只生成 0 生成加运行 1 只运行 2
    RUN_TYPE = 1
    TYPE = 'update'
    # 是否启动MYSQL日志
    MYSQL_LOG = True
else:
    READER_MYSQL_CONNECT = {
        'host': '',
        'port': 3306,
        'user': '',
        'password': '',
        'charset': 'utf8',
    }
    MYSQL_CONNECT = {
        'host': '',
        'port': 3306,
        'user': '',
        'password': '',
        'charset': 'utf8',
        'db': ''
    }
    # python版本
    python = 'python'
    DATAX_BIN_PATH = '/home/ods_syx_rw_user/datax/bin/datax.py'
    # 日志表配置
    log_tb_name = "t_mysql2ods_executed_sync_log"
    log_name = f'{log_tb_name}.log'
    error_log_name = f'{log_tb_name}.error.log'
    # 只生成 0 生成加运行 1 只运行 2
    RUN_TYPE = 1
    TYPE = 'update'
    # 是否启动MYSQL日志
    MYSQL_LOG = True
log_all_tb_name = "t_mysql2ods_executed_all_sync_log"
# 重试次数
Retry = 3
#队列
mapred_job_queue_name = 'root.users.ods_job'
# json存放目录
BASE_JSON_DIR = 'json/'
# 是否删除已有分区
is_del = True
# 最大线程数
max_workers = 10
# reader配置
reader_parameter = {
    "username": READER_MYSQL_CONNECT['user'],
    "password": READER_MYSQL_CONNECT['password'],
    "connection": [
        {"jdbcUrl": [f"jdbc:mysql://{READER_MYSQL_CONNECT['host']}:{READER_MYSQL_CONNECT['port']}?useSSL=false&useUnicode=true&characterEncoding=UTF-8&serverTimezone=UTC"]
            , "querySql": []}]
}
# writer配置
writer_parameter = {
    "writeMode": "append",
    "column": [],
    "defaultFS": "hdfs://nameservice1",
    "hadoopConfig":{
            "dfs.nameservices": "nameservice1",
            "dfs.ha.namenodes.nameservice1": "namenode1,namenode2",
            "dfs.namenode.rpc-address.nameservice1.namenode1": ":8020",
            "dfs.namenode.rpc-address.nameservice1.namenode2": ":8020",
            "dfs.client.failover.proxy.provider.nameservice1": "org.apache.hadoop.hdfs.server.namenode.ha.ConfiguredFailoverProxyProvider"
    },
    "path": "/user/hive/warehouse/%s.db/%s",
    "fileType": "orc",
    "fileName": "",
    "fieldDelimiter": "\u0001",

}
# datax主配置
datax_config = {
    "job": {
        "setting": {
            "speed": {"channel": 10,"record": -1}
        },
        "content": []
    }
}

log_data={
    'partition_date':'',
    'database_name':'',
    'table_name':'',
    'executed_way':1,
    'executed_state':'',
    'complit_state':2,
    'start_time':'',
    'end_time':'',
    'local_row_update_time_start':'',
    'local_row_update_time_end':'',
    'numrows':0,
    'remark':'',
    'db_num':0,
    't_num':0,
    't_num_0':0,
    'ods_t_name':'',
    'map_input_nums':0,
}
