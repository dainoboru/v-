import os
import oracledb
import cloudNowUtils

un = os.environ.get('PYTHON_USERNAME')
pw = os.environ.get('PYTHON_PASSWORD')
cs = os.environ.get('PYTHON_CONNECTSTRING')

def searchLogic(SQL):
    """検索ロジック　SQLをもとに検索を行う"""
    with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
        with connection.cursor() as cursor:
            for sq in SQL:
                cursor.execute(sq)
            
            connection.commit()