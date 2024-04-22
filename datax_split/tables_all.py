import datetime
year=datetime.datetime.now().year
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
          
          {'name': '招投标基本信息表', 'db': 'db_df_bidding', 'table': 't_bidding_info', 'db_start': 0, 'db_num': 0,
           't_start':  year, 't_num':  year, 'hive_db': DB,
           'hive_table': 'ods_q_db_df_bidding_t_bidding_info', 'update_column': 'local_row_update_time',
           'partition_column': 'partition_date'},
          {'name': 'db1',
           'db': 'db_code',
           'table': 't_admin_division_code',
           'db_start': 0,
           'db_num': 0,
           't_start': 0,
           't_num': 0,
           'hive_db': DB,
           'hive_table': 'ods_q_db_code_t_admin_division_code'},
          {'name': 'db1',
           'db': 'db_code',
           'table': 't_country_code',
           'db_start': 0,
           'db_num': 0,
           't_start': 0,
           't_num': 0,
           'hive_db': DB,
           'hive_table': 'ods_q_db_code_t_country_code'},
          {'name': 'db1',
           'db': 'db_code',
           'table': 't_currency_code',
           'db_start': 0,
           'db_num': 0,
           't_start': 0,
           't_num': 0,
           'hive_db': DB,
           'hive_table': 'ods_q_db_code_t_currency_code'},
          {'name': 'db1',
           'db': 'db_code',
           'table': 't_econ_kind_code',
           'db_start': 0,
           'db_num': 0,
           't_start': 0,
           't_num': 0,
           'hive_db': DB,
           'hive_table': 'ods_q_db_code_t_econ_kind_code'},
          {'name': 'db1',
           'db': 'db_code',
           'table': 't_industry_code',
           'db_start': 0,
           'db_num': 0,
           't_start': 0,
           't_num': 0,
           'hive_db': DB,
           'hive_table': 'ods_q_db_code_t_industry_code'},
          {'name': 'db1',
           'db': 'db_code',
           'table': 't_job_title_code',
           'db_start': 0,
           'db_num': 0,
           't_start': 0,
           't_num': 0,
           'hive_db': DB,
           'hive_table': 'ods_q_db_code_t_job_title_code'},
          {'name': 'db1',
           'db': 'db_code',
           'table': 't_procedure_code',
           'db_start': 0,
           'db_num': 0,
           't_start': 0,
           't_num': 0,
           'hive_db': DB,
           'hive_table': 'ods_q_db_code_t_procedure_code'},
          {'name': '撼地股比表', 'db': 'handi', 'table': 'task_syx_conprop', 'db_start': 0, 'db_num': 0, 't_start': 0,
           't_num': 0, 'hive_db': DB, 'hive_table': 'ods_h_hd_task_syx_conprop', 'update_column': 'updated',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '非正常户', 'db': 'db_business', 'table': 't_abnormal_enterprises', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_business_t_abnormal_enterprises', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '行政处罚多源综合表', 'db': 'db_business', 'table': 't_administrative_punishment', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_business_t_administrative_punishment', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '海关登记信息', 'db': 'db_business', 'table': 't_creditimportexport_data', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_business_t_creditimportexport_data', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '一般纳税人', 'db': 'db_business', 'table': 't_general_taxpayer', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 0, 'hive_db': DB, 'hive_table': 'ods_q_db_business_t_general_taxpayer',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '购地数据', 'db': 'db_business', 'table': 't_goudi_information', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 0, 'hive_db': DB, 'hive_table': 'ods_q_db_business_t_goudi_information',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '重大税收违法', 'db': 'db_business', 'table': 't_huge_tax_punishment', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 0, 'hive_db': DB, 'hive_table': 'ods_q_db_business_t_huge_tax_punishment',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '纳税A级', 'db': 'db_business', 'table': 't_pay_taxes', 'db_start': 0, 'db_num': 0, 't_start': 0,
           't_num': 0, 'hive_db': DB, 'hive_table': 'ods_q_db_business_t_pay_taxes',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '限制高消费', 'db': 'db_business_reproduce', 'table': 't_restricted_consumer', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_business_reproduce_t_restricted_consumer', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '终本案件', 'db': 'db_business_reproduce', 'table': 't_terminationcaseitem', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_business_reproduce_t_terminationcaseitem', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '诚信大数据', 'db': 'db_business_reproduce', 'table': 't_credit_info', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_business_reproduce_t_credit_info', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '域名信息', 'db': 'db_business_reproduce', 'table': 't_domains_alls', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_business_reproduce_t_domains_alls', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '招投标企业关系表', 'db': 'db_df_bidding', 'table': 't_bidding_related', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 0, 'hive_db': DB, 'hive_table': 'ods_q_db_df_bidding_t_bidding_related',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '招投标内容表', 'db': 'db_df_bidding', 'table': 't_bidding_content', 'db_start': 0, 'db_num': 0,
           't_start': year, 't_num': year, 'hive_db': DB,
           'hive_table': 'ods_q_db_df_bidding_t_bidding_content', 'update_column': 'local_row_update_time', 'partition_column': 'partition_date'},
          {'name': '环保处罚表', 'db': 'db_df_credit', 'table': 't_huanbaochufas', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 0, 'hive_db': DB, 'hive_table': 'ods_q_db_df_credit_t_huanbaochufas',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '环保处罚表_新', 'db': 'db_enterprise_other', 'table': 't_huanbaochufas', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_enterprise_other_t_huanbaochufas', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '基础属性标签表', 'db': 'db_df_miningdata', 'table': 't_mining_tags_scale', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'db_df_miningdata_t_mining_tags_scale', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '基础属性标签表', 'db': 'db_zlr_xiaowei', 'table': 't_mining_tags_scale', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_zlr_xiaowei_t_mining_tags_scale', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '商标公告表', 'db': 'db_df_trademark_other', 'table': 't_trademark_notice', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_df_trademark_other_t_trademark_notice', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '商标企业查询表', 'db': 'db_df_trademark_other', 'table': 't_trademark_relation', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_df_trademark_other_t_trademark_relation', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '司法拍卖', 'db': 'db_enterprise_other', 'table': 't_auctions', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 0, 'hive_db': DB, 'hive_table': 'ods_q_db_enterprise_other_t_auctions',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '立案信息', 'db': 'db_enterprise_other', 'table': 't_cases', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 0, 'hive_db': DB, 'hive_table': 'ods_q_db_enterprise_other_t_cases',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '被执行企业', 'db': 'db_enterprise_other', 'table': 't_executedpersons', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_enterprise_other_t_executedpersons', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '失信被执行企业', 'db': 'db_enterprise_other', 'table': 't_executions', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 0, 'hive_db': DB, 'hive_table': 'ods_q_db_enterprise_other_t_executions',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '法院公告', 'db': 'db_enterprise_other', 'table': 't_notices', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 0, 'hive_db': DB, 'hive_table': 'ods_q_db_enterprise_other_t_notices',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '欠税信息', 'db': 'db_enterprise_other', 'table': 't_overduetaxs', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 0, 'hive_db': DB, 'hive_table': 'ods_q_db_enterprise_other_t_overduetaxs',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '开庭公告', 'db': 'db_enterprise_other', 'table': 't_kaitinggonggaos', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_enterprise_other_t_kaitinggonggaos', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '招聘信息', 'db': 'db_enterprise_other', 'table': 't_new_jobs', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 15, 'hive_db': DB, 'hive_table': 'ods_q_db_enterprise_other_t_new_jobs',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '专利信息', 'db': 'db_intellectual_property', 'table': 't_patents_new', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_intellectual_property_t_patents_new', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '专利信息关系', 'db': 'db_intellectual_property', 'table': 't_patents_relations_new', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_intellectual_property_t_patents_relations_new',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '建筑类资质', 'db': 'db_qualification_certificate', 'table': 't_building', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_building', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': 'CCC产品认证', 'db': 'db_qualification_certificate', 'table': 't_ccc', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_ccc', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': 'CCC自我声明表', 'db': 'db_qualification_certificate', 'table': 't_ccc_self_declaration',
           'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_ccc_self_declaration',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': 'CESI产品认证', 'db': 'db_qualification_certificate', 'table': 't_cesi_certification', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_cesi_certification',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '计算机信息系统集成项目经理资质', 'db': 'db_qualification_certificate',
           'table': 't_computer_project_manager', 'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0,
           'hive_db': DB, 'hive_table': 'ods_q_db_qualification_certificate_t_computer_project_manager',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '化妆品生产许可信息', 'db': 'db_qualification_certificate', 'table': 't_cosmetic_produce_license',
           'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_cosmetic_produce_license',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '药品经营企业', 'db': 'db_qualification_certificate', 'table': 't_drug_business', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_drug_business', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '国产药品批准文号', 'db': 'db_qualification_certificate', 'table': 't_drug_permit_cn', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_drug_permit_cn',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '药品生产企业', 'db': 'db_qualification_certificate', 'table': 't_drug_produce', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_drug_produce', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '电子认证服务机构许可证', 'db': 'db_qualification_certificate',
           'table': 't_electronic_certification_agency', 'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0,
           'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_electronic_certification_agency',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '房地产开发企业资质', 'db': 'db_qualification_certificate', 'table': 't_estate_qualification',
           'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_estate_qualification',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '灭火系统', 'db': 'db_qualification_certificate', 'table': 't_firefighting_system', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_firefighting_system',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '食品添加剂生产许可证', 'db': 'db_qualification_certificate', 'table': 't_food_additives',
           'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_food_additives',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '食品经营许可证', 'db': 'db_qualification_certificate', 'table': 't_food_business_license',
           'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_food_business_license',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '食品农产品认证', 'db': 'db_qualification_certificate', 'table': 't_food_license', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_food_license', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '出口食品生产企业备案', 'db': 'db_qualification_certificate', 'table': 't_food_product_ent',
           'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_food_product_ent',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '食品生产许可证', 'db': 'db_qualification_certificate', 'table': 't_food_product_license',
           'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_food_product_license',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '工业产品生产许可证', 'db': 'db_qualification_certificate', 'table': 't_industry_produce',
           'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_industry_produce',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '自愿性工业产品认证', 'db': 'db_qualification_certificate', 'table': 't_industry_volunteer',
           'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_industry_volunteer',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': 'GMP,GSP认证', 'db': 'db_qualification_certificate', 'table': 't_license_drug', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_license_drug', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '管理体系', 'db': 'db_qualification_certificate', 'table': 't_management_system', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_management_system',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '医疗器械经营', 'db': 'db_qualification_certificate', 'table': 't_medical_instruments_business',
           'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_medical_instruments_business',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '进口医疗器械', 'db': 'db_qualification_certificate', 'table': 't_medical_instruments_import',
           'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_medical_instruments_import',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '医疗器械生产企业', 'db': 'db_qualification_certificate', 'table': 't_medical_instruments_produce',
           'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_medical_instruments_produce',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '国产医疗器械注册', 'db': 'db_qualification_certificate',
           'table': 't_medical_instruments_registered', 'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0,
           'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_medical_instruments_registered',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '探矿权', 'db': 'db_qualification_certificate', 'table': 't_mining_exploration', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_mining_exploration',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '采矿权', 'db': 'db_qualification_certificate', 'table': 't_mining_license', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_mining_license',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '电信设备进网许可', 'db': 'db_qualification_certificate', 'table': 't_network_license',
           'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_network_license',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '安全生产许可证', 'db': 'db_qualification_certificate', 'table': 't_product_safe_license',
           'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_product_safe_license',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '无线电发射设备进关核准', 'db': 'db_qualification_certificate', 'table': 't_radio_customs_approve',
           'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_radio_customs_approve',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '无线电发射设备型号核准', 'db': 'db_qualification_certificate', 'table': 't_radio_model_approve',
           'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_radio_model_approve',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '服务认证', 'db': 'db_qualification_certificate', 'table': 't_service', 'db_start': 0, 'db_num': 0,
           't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_service', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '排污许可', 'db': 'db_qualification_certificate', 'table': 't_sewage_permit', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_sewage_permit', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '电信许可证书', 'db': 'db_qualification_certificate', 'table': 't_telecommunications_license',
           'db_start': 0, 'db_num': 0, 't_start': 0, 't_num': 0, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_telecommunications_license',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '资质证书', 'db': 'db_qualification_certificate', 'table': 't_certificate_main', 'db_start': 0,
           'db_num': 0, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_qualification_certificate_t_certificate_main',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '工商变更记录结构化表', 'db': 'db_df_enterprisef', 'table': 't_changerec_format_alls', 'db_start': 0,
           'db_num': 15, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_df_enterprisef_t_changerec_format_alls', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '裁判文书（不含正文）', 'db': 'db_df_lawsuits_v1', 'table': 't_lawsuits_rolerelations', 'db_start': 0,
           'db_num': 15, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_df_lawsuits_v1_t_lawsuits_rolerelations', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '商标信息表', 'db': 'db_df_trademark', 'table': 't_trademark_info', 'db_start': 0, 'db_num': 15,
           't_start': 0, 't_num': 15, 'hive_db': DB, 'hive_table': 'ods_q_db_df_trademark_t_trademark_info',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '商标商品服务表', 'db': 'db_df_trademark', 'table': 't_trademark_product', 'db_start': 0,
           'db_num': 15, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_df_trademark_t_trademark_product', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '商标流程表', 'db': 'db_df_trademark', 'table': 't_trademark_step', 'db_start': 0, 'db_num': 15,
           't_start': 0, 't_num': 15, 'hive_db': DB, 'hive_table': 'ods_q_db_df_trademark_t_trademark_step',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '司法拍卖', 'db': 'db_ent_relations', 'table': 't_auctions_relations', 'db_start': 0, 'db_num': 15,
           't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_ent_relations_t_auctions_relations', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '立案信息', 'db': 'db_ent_relations', 'table': 't_cases_relations', 'db_start': 0, 'db_num': 15,
           't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_ent_relations_t_cases_relations', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '著作权/软件著作权', 'db': 'db_ent_relations', 'table': 't_copyrights_relations', 'db_start': 0,
           'db_num': 15, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_ent_relations_t_copyrights_relations', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '开庭公告', 'db': 'db_ent_relations', 'table': 't_kaitinggonggaos_relations', 'db_start': 0,
           'db_num': 15, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_ent_relations_t_kaitinggonggaos_relations', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '法院公告', 'db': 'db_ent_relations', 'table': 't_notices_relations', 'db_start': 0, 'db_num': 15,
           't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_ent_relations_t_notices_relations', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '经营异常（工商公示）', 'db': 'db_enterprise', 'table': 't_abnormal', 'db_start': 0, 'db_num': 15,
           't_start': 0, 't_num': 15, 'hive_db': DB, 'hive_table': 'ods_q_db_enterprise_t_abnormal',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '企业地址（工商公示）', 'db': 'db_enterprise', 'table': 't_address', 'db_start': 0, 'db_num': 15,
           't_start': 0, 't_num': 15, 'hive_db': DB, 'hive_table': 'ods_q_db_enterprise_t_address',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '企业分支机构', 'db': 'db_enterprise', 'table': 't_branches', 'db_start': 0, 'db_num': 15,
           't_start': 0, 't_num': 15, 'hive_db': DB, 'hive_table': 'ods_q_db_enterprise_t_branches',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '企业变更记录（工商公示）', 'db': 'db_enterprise', 'table': 't_change_records', 'db_start': 0,
           'db_num': 15, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_enterprise_t_change_records', 'update_column': 'local_row_update_time',
           'other': False,
           'partition_column': 'partition_date'},
          {'name': '抽查检查（工商公示）', 'db': 'db_enterprise', 'table': 't_checkups', 'db_start': 0, 'db_num': 15,
           't_start': 0, 't_num': 15, 'hive_db': DB, 'hive_table': 'ods_q_db_enterprise_t_checkups',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '清算组成员信息（工商公示）', 'db': 'db_enterprise', 'table': 't_clear_account', 'db_start': 0,
           'db_num': 15, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_enterprise_t_clear_account', 'update_column': 'local_row_update_time',
           'other': False,
           'partition_column': 'partition_date'},
          {'name': '双随机抽查结果（工商公示）', 'db': 'db_enterprise', 'table': 't_double_checkups', 'db_start': 0,
           'db_num': 15, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_enterprise_t_double_checkups', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '企业邮箱（工商公示）', 'db': 'db_enterprise', 'table': 't_emails', 'db_start': 0, 'db_num': 15,
           't_start': 0, 't_num': 15, 'hive_db': DB, 'hive_table': 'ods_q_db_enterprise_t_emails',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '企业主要人员（工商公示）', 'db': 'db_enterprise', 'table': 't_employees_alls', 'db_start': 0,
           'db_num': 15, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_enterprise_t_employees_alls', 'update_column': 'local_row_update_time',
           'other': False,
           'partition_column': 'partition_date'},
          {'name': '企业基本信息', 'db': 'db_enterprise', 'table': 't_enterprise', 'db_start': 0, 'db_num': 15,
           't_start': 0, 't_num': 15, 'hive_db': DB, 'hive_table': 'ods_q_db_enterprise_t_enterprise',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '股权出质（工商公示）', 'db': 'db_enterprise', 'table': 't_equityquality', 'db_start': 0, 'db_num': 15,
           't_start': 0, 't_num': 15, 'hive_db': DB, 'hive_table': 'ods_q_db_enterprise_t_equityquality',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '企业历史法人', 'db': 'db_enterprise', 'table': 't_history_names', 'db_start': 0, 'db_num': 15,
           't_start': 0, 't_num': 15, 'hive_db': DB, 'hive_table': 'ods_q_db_enterprise_t_history_names',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '企业历史名称', 'db': 'db_enterprise', 'table': 't_history_oper_names', 'db_start': 0, 'db_num': 15,
           't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_enterprise_t_history_oper_names', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '企业历史注册资本', 'db': 'db_enterprise', 'table': 't_history_regist_capis', 'db_start': 0,
           'db_num': 15, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_enterprise_t_history_regist_capis', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '股权冻结（工商公示）', 'db': 'db_enterprise', 'table': 't_judicial_freezes', 'db_start': 0,
           'db_num': 15, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_enterprise_t_judicial_freezes', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '知识产权出质（工商公示）', 'db': 'db_enterprise', 'table': 't_knowledge_properties', 'db_start': 0,
           'db_num': 15, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_enterprise_t_knowledge_properties', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '行政许可（工商公示）', 'db': 'db_enterprise', 'table': 't_license_info', 'db_start': 0, 'db_num': 15,
           't_start': 0, 't_num': 15, 'hive_db': DB, 'hive_table': 'ods_q_db_enterprise_t_license_info',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '动产抵押（工商公示）', 'db': 'db_enterprise', 'table': 't_mortgages', 'db_start': 0, 'db_num': 15,
           't_start': 0, 't_num': 15, 'hive_db': DB, 'hive_table': 'ods_q_db_enterprise_t_mortgages',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '企业股东信息（工商公示）', 'db': 'db_enterprise', 'table': 't_partners_alls', 'db_start': 0,
           'db_num': 15, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_enterprise_t_partners_alls', 'update_column': 'local_row_update_time',
           'other': False,
           'partition_column': 'partition_date'},
          {'name': '严重违法（工商公示）', 'db': 'db_enterprise', 'table': 't_serious_illegal', 'db_start': 0,
           'db_num': 15, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_enterprise_t_serious_illegal', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '简易注销公告（工商公示）', 'db': 'db_enterprise', 'table': 't_simple_cancellation_announcement',
           'db_start': 0, 'db_num': 15, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_enterprise_t_simple_cancellation_announcement',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '企业社保信息（工商公示）', 'db': 'db_enterprise', 'table': 't_social_security', 'db_start': 0,
           'db_num': 15, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_enterprise_t_social_security', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '企业电话（工商公示）', 'db': 'db_enterprise', 'table': 't_telephones', 'db_start': 0, 'db_num': 15,
           't_start': 0, 't_num': 15, 'hive_db': DB, 'hive_table': 'ods_q_db_enterprise_t_telephones',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '企业网址（工商公示）', 'db': 'db_enterprise', 'table': 't_websites', 'db_start': 0, 'db_num': 15,
           't_start': 0, 't_num': 15, 'hive_db': DB, 'hive_table': 'ods_q_db_enterprise_t_websites',
           'update_column': 'local_row_update_time', 'other': False, 'partition_column': 'partition_date'},
          {'name': '企业年报（工商公示）', 'db': 'db_enterprise_reports', 'table': 't_report_details', 'db_start': 0,
           'db_num': 15, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_enterprise_reports_t_report_details', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '企业对外投资', 'db': 'db_sub_enterprises', 'table': 't_enterprise_investment', 'db_start': 0,
           'db_num': 15, 't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_sub_enterprises_t_enterprise_investment', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'},
          {'name': '企业行业信息', 'db': 'db_sub_enterprises', 'table': 't_last_industry', 'db_start': 0, 'db_num': 15,
           't_start': 0, 't_num': 15, 'hive_db': DB,
           'hive_table': 'ods_q_db_sub_enterprises_t_last_industry', 'update_column': 'local_row_update_time',
           'other': False, 'partition_column': 'partition_date'}]