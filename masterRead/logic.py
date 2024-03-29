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
def searchCondition(key):
    result = ""
    result = const.divSQL if key=="div" else result
    result = const.sysSQL if key=="sys" else result
    result = const.proSQL if key=="pro" else result
    result = const.cateSQL if key=="cate" else result
    result = const.envSQL if key=="env" else result
    result = const.serSQL if key=="ser" else result
    return result
    
def searchLogic(SQL):
    """検索ロジック　SQLをもとに検索を行う"""
    result=[]
    with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
        with connection.cursor() as cursor:
            for r in cursor.execute(SQL):
                result.append(cloudNowUtils.dateTranslate(r))
    return result

