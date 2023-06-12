import os
import oracledb
import cloudNowUtils
import const

un = os.environ.get('PYTHON_USERNAME')
pw = os.environ.get('PYTHON_PASSWORD')
cs = os.environ.get('PYTHON_CONNECTSTRING')

# 検索キーワードから検索条件のテキストデータを作成
# 引数：[key1,key2]
# 戻り値：where ((title like '%AWS%') or (error_message like '%AWS%') or (detail like '%AWS%') or (PGTable.product_name like '%AWS%') or (PGTable.cloud_service like '%AWS%')) and ((title like '%aaa%') or (error_message like '%aaa%') or (detail like '%aaa%') or (PGTable.product_name like '%aaa%') or (PGTable.cloud_service like '%aaa%'))
def searchCondition(keys):
    result="where "
    if len(keys)==0:
        return ""
    for key in keys:
        result+="((searchtable.title like '%{}%') or (searchtable.error_message like '%{}%') or (searchtable.detail like '%{}%') or (searchtable.product_name like '%{}%') or (searchtable.cloud_service like '%{}%')) ".format(key,key,key,key,key)
        result+="and "
    return result[:-4]
    
def searchLogic(SQL):
    """検索ロジック　SQLをもとに検索を行う"""
    result=[]
    with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
        with connection.cursor() as cursor:
            for r in cursor.execute(SQL):
                result.append(cloudNowUtils.dateTranslate(r))
    return result


# 複数検索　ex: keys = ["AWS","Lambda"] 
def searchMulti(keys):
    sql=const.SQL_FIRST+searchCondition(keys)+const.SQL_SECOND
    print(sql)
    return searchLogic(sql)