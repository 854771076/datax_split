mysql_arr_table = [
        ####共99张  + 1撼地年报 + 7张code表 总计107张
        ##股比表最先跑 20220928
        {"type": "qxb",     "name": "企业基本信息",  "db": "db_enterprise", "table": "t_enterprise", "db_num": 15, "t_num": 15},
        {"type": "handi",   "name": "撼地股比表",    "db": "handi",         "table": "task_syx_conprop", "db_num": 0, "t_num": 0},
        {"type": "qxb",     "name": "企业历史法人",  "db": "db_enterprise", "table": "t_history_names", "db_num": 15, "t_num": 15},
        #1 司法16张表  ##20220714
        ##1 and 2
        {"type": "qxb",   "name": "股权出质（工商公示）", "db": "db_enterprise", "table": "t_equityquality",       "db_num": 15, "t_num": 15},

        {"type": "qxb",   "name": "开庭公告", "db": "db_enterprise_other",   "table": "t_kaitinggonggaos",           "db_num": 0, "t_num": 15},
        {"type": "qxb",   "name": "开庭公告", "db": "db_ent_relations",      "table": "t_kaitinggonggaos_relations", "db_num": 15, "t_num": 15},

        ###1.1 notice.txt 迁移用表
        {"type": "qxb",   "name": "法院公告", "db": "db_enterprise_other",   "table": "t_notices",            "db_num": 0, "t_num": 0},
        {"type": "qxb",   "name": "法院公告", "db": "db_ent_relations",      "table": "t_notices_relations",  "db_num": 15, "t_num": 15},
        #
        {"type": "qxb",   "name": "立案信息", "db": "db_enterprise_other",   "table": "t_cases",              "db_num": 0, "t_num": 0},
        {"type": "qxb",   "name": "立案信息", "db": "db_ent_relations",      "table": "t_cases_relations",    "db_num": 15, "t_num": 15},
        {"type": "qxb",   "name": "司法拍卖", "db": "db_enterprise_other",   "table": "t_auctions",           "db_num": 0, "t_num": 0},
        {"type": "qxb",   "name": "司法拍卖", "db": "db_ent_relations",      "table": "t_auctions_relations", "db_num": 15, "t_num": 15},
        #
        {"type": "qxb",   "name": "限制高消费",   "db": "db_business_reproduce",  "table": "t_restricted_consumer", "db_num": 0, "t_num": 0},
        {"type": "qxb",   "name": "终本案件",     "db": "db_business_reproduce", "table": "t_terminationcaseitem", "db_num": 0, "t_num": 0},

        #1.2 patents.py 迁移用表  and 2  ##20220714
        {"type": "qxb",   "name": "专利信息",        "db": "db_intellectual_property", "table": "t_patents_new",             "db_num": 0, "t_num": 15},
        {"type": "qxb",   "name": "专利信息关系",     "db": "db_intellectual_property", "table": "t_patents_relations_new",   "db_num": 0, "t_num": 15},

        #1.3 and 3 ssqy.py 迁移用表
        {"type": "qxb",   "name": "失信被执行企业",      "db": "db_enterprise_other",   "table": "t_executions",          "db_num": 0, "t_num": 0},
        {"type": "qxb",   "name": "被执行企业",         "db": "db_enterprise_other",   "table": "t_executedpersons",     "db_num": 0, "t_num": 0},
        {"type": "qxb",   "name": "股权冻结（工商公示）", "db": "db_enterprise",         "table": "t_judicial_freezes",    "db_num": 15, "t_num": 15},
        {"type": "qxb",   "name": "严重违法（工商公示）", "db": "db_enterprise",         "table": "t_serious_illegal",     "db_num": 15, "t_num": 15},
        {"type": "qxb",   "name": "裁判文书（不含正文）", "db": "db_df_lawsuits_v1",     "table": "t_lawsuits_rolerelations", "db_num": 15,"t_num": 15},
        #
        # ## 第二批数据  1+3 + 20
        # # 20220630


        ##20220714
        {"type": "qxb",   "name": "企业行业信息",              "db": "db_sub_enterprises",     "table": "t_last_industry", "db_num": 15, "t_num": 15},
        {"type": "qxb",   "name": "企业股东信息（工商公示）",    "db": "db_enterprise",          "table": "t_partners_alls", "db_num": 15, "t_num": 15},
        {"type": "qxb",   "name": "企业对外投资",              "db": "db_sub_enterprises",     "table": "t_enterprise_investment", "db_num": 15, "t_num": 15},
        {"type": "qxb",   "name": "企业变更记录（工商公示）",    "db": "db_enterprise",          "table": "t_change_records", "db_num": 15, "t_num": 15},
        ##20240227 增加
        {"type": "qxb",   "name": "工商变更记录结构化表",                "db": "db_df_enterprisef",             "table": "t_changerec_format_alls",         "db_num": 15,       "t_num": 15},

        {"type": "qxb",   "name": "企业地址（工商公示）",       "db": "db_enterprise",          "table": "t_address", "db_num": 15, "t_num": 15},

        {"type": "qxb",   "name": "行政处罚多源综合表",   "db": "db_business",  "table": "t_administrative_punishment", "db_num": 0, "t_num": 0},

        {"type": "qxb",   "name": "经营异常（工商公示）", "db": "db_enterprise",  "table": "t_abnormal", "db_num": 15, "t_num": 15},
        #
        {"type": "qxb",   "name": "海关登记信息",      "db": "db_business",       "table": "t_creditimportexport_data", "db_num": 0, "t_num": 0},
        {"type": "qxb",   "name": "著作权/软件著作权",  "db": "db_ent_relations",  "table": "t_copyrights_relations", "db_num": 15, "t_num": 15},

        ##20220714
        {"type": "qxb",   "name": "商标信息表",        "db": "db_df_trademark", "table": "t_trademark_info", "db_num": 15, "t_num": 15},
        {"type": "qxb",   "name": "商标商品服务表",     "db": "db_df_trademark", "table": "t_trademark_product", "db_num": 15, "t_num": 15},
        {"type": "qxb",   "name": "商标流程表",        "db": "db_df_trademark", "table": "t_trademark_step", "db_num": 15, "t_num": 15},
        {"type": "qxb",   "name": "商标公告表",        "db": "db_df_trademark_other", "table": "t_trademark_notice", "db_num": 0, "t_num": 0},
        {"type": "qxb",   "name": "商标企业查询表",     "db": "db_df_trademark_other", "table": "t_trademark_relation", "db_num": 0, "t_num": 15},

        {"type": "qxb",   "name": "一般纳税人",   "db": "db_business", "table": "t_general_taxpayer", "db_num": 0, "t_num": 0},
        {"type": "qxb",   "name": "非正常户",    "db": "db_business",  "table": "t_abnormal_enterprises", "db_num": 0, "t_num": 0},
        {"type": "qxb",   "name": "欠税信息",    "db": "db_enterprise_other", "table": "t_overduetaxs", "db_num": 0, "t_num": 0},
        {"type": "qxb",   "name": "重大税收违法", "db": "db_business", "table": "t_huge_tax_punishment", "db_num": 0, "t_num": 0},

        {"type": "qxb",   "name": "环保处罚表",   "db": "db_df_credit", "table": "t_huanbaochufas", "db_num": 0, "t_num": 0},
        ##20231008 新增
        {"type": "qxb",   "name": "环保处罚表_新",   "db": "db_enterprise_other", "table": "t_huanbaochufas", "db_num": 0, "t_num": 0},

        # # 3 ssqy.py 迁移用表 20220719  16 +7+1
        {"type": "qxb",  "name": "企业邮箱（工商公示）",                "db": "db_enterprise",                  "table": "t_emails",    "db_num": 15,   "t_num": 15},
        {"type": "qxb",  "name": "企业电话（工商公示）",                "db": "db_enterprise",                  "table": "t_telephones","db_num": 15,   "t_num": 15},
        {"type": "qxb",  "name": "企业网址（工商公示）",                "db": "db_enterprise",                  "table": "t_websites",  "db_num": 15,   "t_num": 15},
        {"type": "qxb",  "name": "企业年报（工商公示）",                "db": "db_enterprise_reports",  "table": "t_report_details",    "db_num": 15,   "t_num": 15},
        {"type": "qxb",  "name": "清算组成员信息（工商公示）",   "db": "db_enterprise",             "table": "t_clear_account",         "db_num": 15,   "t_num": 15},
        {"type": "qxb",  "name": "纳税A级",                         "db": "db_business",                    "table": "t_pay_taxes",                     "db_num": 0,    "t_num": 0},
        # {"type": "qxb",  "name": "基础属性标签表",                        "db": "db_zlr_xiaowei",                     "table": "t_mining_tags_scale", "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "基础属性标签表",                          "db": "db_df_miningdata",                   "table": "t_mining_tags_scale", "db_num": 0,    "t_num": 0},

        #######其他
        ##工商基础信息 3 20220726
        {"type": "qxb",  "name": "企业主要人员（工商公示）",    "db": "db_enterprise",          "table": "t_employees_alls",            "db_num": 15,   "t_num": 15},
        {"type": "qxb",  "name": "企业分支机构",                            "db": "db_enterprise",              "table": "t_branches",                          "db_num": 15,   "t_num": 15},
        {"type": "qxb",  "name": "企业社保信息（工商公示）",    "db": "db_enterprise",          "table": "t_social_security",       "db_num": 15,       "t_num": 15},

        ##工商其他信息 6 20220726
        {"type": "qxb",  "name": "行政许可（工商公示）",                "db": "db_enterprise",          "table": "t_license_info",                  "db_num": 15,       "t_num": 15},
        {"type": "qxb",  "name": "知识产权出质（工商公示）",    "db": "db_enterprise",          "table": "t_knowledge_properties",      "db_num": 15,   "t_num": 15},
        {"type": "qxb",  "name": "动产抵押（工商公示）",                "db": "db_enterprise",          "table": "t_mortgages",                         "db_num": 15,   "t_num": 15},
        {"type": "qxb",  "name": "抽查检查（工商公示）",                "db": "db_enterprise",      "table": "t_checkups",                      "db_num": 15,   "t_num": 15},
        {"type": "qxb",  "name": "双随机抽查结果（工商公示）",  "db": "db_enterprise",          "table": "t_double_checkups",   "db_num": 15,   "t_num": 15},
        {"type": "qxb",  "name": "简易注销公告（工商公示）",    "db": "db_enterprise",      "table": "t_simple_cancellation_announcement",      "db_num": 15,   "t_num": 15},
        #
        # ##招投标 2+3 5
        # # 20220725
        {"type": "qxb",   "name": "招投标内容表",    "db": "db_df_bidding", "table": "t_bidding_content", "db_num": 0, "t_num": 0},
        {"type": "qxb",   "name": "招投标基本信息表", "db": "db_df_bidding", "table": "t_bidding_info",    "db_num": 0, "t_num": 0},
        #
        # # 20220726
        {"type": "qxb",   "name": "招投标企业关系表",   "db": "db_df_bidding", "table": "t_bidding_related", "db_num": 0, "t_num": 0},
        {"type": "qxb",   "name": "招聘信息",          "db": "db_enterprise_other", "table": "t_new_jobs", "db_num": 0, "t_num": 15},
        {"type": "qxb",   "name": "购地数据",          "db": "db_business", "table": "t_goudi_information", "db_num": 0, "t_num": 0},

        ##诚信数据库 1 20220726
        {"type": "qxb",   "name": "诚信大数据",   "db": "db_business_reproduce", "table": "t_credit_info", "db_num": 0, "t_num": 15},

        ###历史信息 2 20220726
        {"type": "qxb",   "name": "企业历史名称",       "db": "db_enterprise", "table": "t_history_oper_names", "db_num": 15, "t_num": 15},
        {"type": "qxb",   "name": "企业历史注册资本",    "db": "db_enterprise", "table": "t_history_regist_capis", "db_num": 15, "t_num": 15},

        ##知识产权 2+35
        # #20220726
        {"type": "qxb",   "name": "域名信息",         "db": "db_business_reproduce", "table": "t_domains_alls", "db_num": 0, "t_num": 15},
        {"type": "qxb",   "name": "资质证书",         "db": "db_qualification_certificate", "table": "t_certificate_main", "db_num": 0, "t_num": 15},

        # #20220727
        {"type": "qxb",  "name": "建筑类资质",                          "db": "db_qualification_certificate",   "table": "t_building",                  "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "CCC产品认证",                     "db": "db_qualification_certificate",       "table": "t_ccc",                               "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "CCC自我声明表",                       "db": "db_qualification_certificate",   "table": "t_ccc_self_declaration",      "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "CESI产品认证",                        "db": "db_qualification_certificate",   "table": "t_cesi_certification",        "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "计算机信息系统集成项目经理资质","db": "db_qualification_certificate",  "table": "t_computer_project_manager", "db_num": 0, "t_num": 0},
        {"type": "qxb",  "name": "化妆品生产许可信息",          "db": "db_qualification_certificate",   "table": "t_cosmetic_produce_license",  "db_num": 0, "t_num": 0},
        {"type": "qxb",  "name": "药品经营企业",                                "db": "db_qualification_certificate",   "table": "t_drug_business",             "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "国产药品批准文号",                    "db": "db_qualification_certificate",   "table": "t_drug_permit_cn",    "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "药品生产企业",                                "db": "db_qualification_certificate",   "table": "t_drug_produce",              "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "电子认证服务机构许可证",          "db": "db_qualification_certificate",       "table": "t_electronic_certification_agency","db_num": 0,"t_num": 0},
        {"type": "qxb",  "name": "房地产开发企业资质",          "db": "db_qualification_certificate",   "table": "t_estate_qualification",      "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "灭火系统",                            "db": "db_qualification_certificate",   "table": "t_firefighting_system",       "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "食品添加剂生产许可证",                "db": "db_qualification_certificate",   "table": "t_food_additives",            "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "食品经营许可证",                      "db": "db_qualification_certificate",   "table": "t_food_business_license",     "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "食品农产品认证",                      "db": "db_qualification_certificate",   "table": "t_food_license",                      "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "出口食品生产企业备案",                "db": "db_qualification_certificate",   "table": "t_food_product_ent",          "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "食品生产许可证",                      "db": "db_qualification_certificate",   "table": "t_food_product_license",      "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "工业产品生产许可证",          "db": "db_qualification_certificate",   "table": "t_industry_produce",          "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "自愿性工业产品认证",          "db": "db_qualification_certificate",   "table": "t_industry_volunteer",        "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "GMP,GSP认证",                     "db": "db_qualification_certificate",       "table": "t_license_drug",                      "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "管理体系",                            "db": "db_qualification_certificate",   "table": "t_management_system",         "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "医疗器械经营",                        "db": "db_qualification_certificate",   "table": "t_medical_instruments_business",      "db_num": 0, "t_num": 0},
        {"type": "qxb",  "name": "进口医疗器械",                        "db": "db_qualification_certificate",   "table": "t_medical_instruments_import",        "db_num": 0, "t_num": 0},
        {"type": "qxb",  "name": "医疗器械生产企业",            "db": "db_qualification_certificate",   "table": "t_medical_instruments_produce",       "db_num": 0, "t_num": 0},
        {"type": "qxb",  "name": "国产医疗器械注册",            "db": "db_qualification_certificate",   "table": "t_medical_instruments_registered","db_num": 0, "t_num": 0},
        {"type": "qxb",  "name": "探矿权",                              "db": "db_qualification_certificate",   "table": "t_mining_exploration",        "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "采矿权",                              "db": "db_qualification_certificate",   "table": "t_mining_license",    "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "电信设备进网许可",            "db": "db_qualification_certificate",   "table": "t_network_license",   "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "安全生产许可证",              "db": "db_qualification_certificate",   "table": "t_product_safe_license",      "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "无线电发射设备进关核准",      "db": "db_qualification_certificate",   "table": "t_radio_customs_approve",     "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "无线电发射设备型号核准",      "db": "db_qualification_certificate",   "table": "t_radio_model_approve",       "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "服务认证",                    "db": "db_qualification_certificate",   "table": "t_service",           "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "排污许可",                    "db": "db_qualification_certificate",   "table": "t_sewage_permit",     "db_num": 0,    "t_num": 0},
        {"type": "qxb",  "name": "电信许可证书",                        "db": "db_qualification_certificate",   "table": "t_telecommunications_license", "db_num": 0, "t_num": 0},



    ]