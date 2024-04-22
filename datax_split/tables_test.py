'''
{'name': '撼地股比表',
#mysql库名
'db': 'handi', 
#mysql表名
'table': 'task_syx_conprop', 
#分库起始脚标
'db_start': 0, 
#分库数量
'db_num': 0, 
#分表起始脚标
't_start': 0,
#分表数量
't_num': 0, 
#hive库名
'hive_db':DB, 
#hive表名
'hive_table': 'ods_h_hd_task_syx_conprop', 
#更新字段名
'update_column': 'updated',
#是否有other分表（如ods_q_db_df_bidding_t_bidding_info_other）
'other': False, 
#分区字段名
'partition_column': 'partition_date'}
'''
DB = 'ods_syx'
TABLES = [
            {'name': '基础属性标签表', 'db': 'db_zlr_xiaowei', 'table': 't_mining_tags_scale', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_zlr_xiaowei_t_mining_tags_scale', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},


           
           ]
# python3 datax_to_hive_run_test.py other 1970-01-01 2024-04-08 20240407
# python3 datax_to_hive_run_test.py other 2024-04-08 2024-04-09 20240408
# python3 datax_to_hive_run_test.py update
# python3 datax_to_hive_run_test.py other 1970-01-01 2024-04-08 20240407