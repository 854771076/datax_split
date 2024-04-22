from . import settings
from .utils import *
from .datax_to_hive_run import *
from .tables_test import TABLES

def check_task():
    settings.max_workers=1
    settings.datax_config = {
        "job": {
            "setting": {
                "speed": {"channel": 5,"record": -1}
            },
            "content": []
        }
    }
    settings.logger = getLog()
    settings.today_time = datetime.date.today()
    settings.yesterday_time = settings.today_time + datetime.timedelta(-1)
    settings.partition_date = settings.yesterday_time.strftime("%Y%m%d")

    settings.Log_db = MysqlDB(settings.MYSQL_CONNECT)
    try:
        TYPE = sys.argv[1]
        if TYPE not in ['all', 'update', 'other']:
            TYPE = settings.TYPE
        else:
            settings.TYPE=TYPE
    except:
        TYPE = settings.TYPE
    settings.logger.info(f'重试开始--type:{TYPE}')
    start = time.time()
    ##1 全量  截止运行时间零点
    settings.logger.info('mysql_to_hive start')
    if TYPE == 'all':
        settings.log_data['executed_way'] = 1
        settings.partition_date = sys.argv[2] if len(sys.argv) > 2 else settings.partition_date
        settings.log_data['partition_date'] = settings.partition_date
        settings.log_data['local_row_update_time_start'] = settings.today_time.strftime("%Y-%m-%d 00:00:00")
        settings.log_data['local_row_update_time_end'] = settings.today_time.strftime("%Y-%m-%d 00:00:00")

    elif TYPE == 'update':
        settings.log_data['executed_way'] = 0
        settings.partition_date = sys.argv[2] if len(sys.argv) > 2 else settings.partition_date
        settings.log_data['partition_date'] = settings.partition_date
        settings.log_data['local_row_update_time_start'] = settings.today_time.strftime("%Y-%m-%d 00:00:00")
        settings.log_data['local_row_update_time_end'] = settings.today_time.strftime("%Y-%m-%d 00:00:00")

    ##3 指定时间段 追加放入昨天分区/指定分区里
    elif TYPE == 'other':
        settings.start_time = sys.argv[2]
        settings.end_time = sys.argv[3]
        # start_time = "2022-08-11 00:00:00"
        # end_time   = "2022-08-12 00:00:00"
        settings.partition_date = sys.argv[4] if len(sys.argv) > 4 else settings.partition_date
        settings.log_data['partition_date'] = settings.partition_date
        settings.log_data['executed_way'] = 2
        settings.log_data['local_row_update_time_start'] = settings.start_time
        settings.log_data['local_row_update_time_end'] = settings.end_time
    else:
        raise ValueError(f'不能识别类型{TYPE}')
    
    all_log={
        'partition_date':settings.partition_date,
        'executed_way':settings.log_data['executed_way'],
        'executed_state':'failed',
        'complit_state':2,
        'start_time':datetime.datetime.now(),
        'end_time':None,
        'remark':'',
    }
    print(settings.partition_date)
    if settings.MYSQL_LOG:
        Log_db = MysqlDB(settings.MYSQL_CONNECT)
        conn=Log_db.getconn()
        cur=conn.cursor()
        cur.execute(f'select table_name from {settings.log_tb_name} where partition_date="{settings.partition_date}" and complit_state!=1 and executed_way={settings.log_data["executed_way"]};')
        data=[i[0] for i in cur.fetchall()]
        ERROR_TABLES=list(filter(lambda x:x.get('table') in data,TABLES))

        cur.execute(f'select COUNT(*) from {settings.log_tb_name} where partition_date="{settings.partition_date}" and complit_state!=1 and executed_way={settings.log_data["executed_way"]};')
        TASK_COUNT=cur.fetchone()[0]
        cur.close()
        conn.close()
    else:
        ERROR_TABLES=[]
    if ERROR_TABLES and TASK_COUNT!=0:
        with concurrent.futures.ThreadPoolExecutor(max_workers=settings.max_workers) as executor:
            # 提交每个表的处理任务到线程池
            futures = [executor.submit(functools.partial(get_datax_json, table)) for table in ERROR_TABLES]

            # 等待所有任务完成
            concurrent.futures.wait(futures)
            if settings.MYSQL_LOG:
                Log_db = MysqlDB(settings.MYSQL_CONNECT)
                conn=Log_db.getconn()
                cur=conn.cursor()
                cur.execute(f'select table_name from {settings.log_tb_name} where partition_date="{settings.partition_date}" and complit_state!=1 and executed_way={settings.log_data["executed_way"]};')
                data=[i[0] for i in cur.fetchall()]
                ERROR_TABLES=list(filter(lambda x:x.get('table') in data,TABLES))
                cur.close()
                conn.close()
            if ERROR_TABLES:
                all_log['executed_state']='failed'
                all_log['complit_state']=2
            else:
                all_log['executed_state']='success'
                all_log['complit_state']=1

    else:
        all_log['executed_state']='success'
        all_log['complit_state']=1
    
    end = time.time()
    all_log['end_time']=datetime.datetime.now()
    settings.Log_db.save([all_log],settings.log_all_tb_name,'append')
    settings.logger.info(f'导入完成---总耗时{(end - start)}秒')
if __name__ == '__main__':
    check_task()