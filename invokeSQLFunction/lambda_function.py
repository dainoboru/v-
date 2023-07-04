import json
import logic
import cloudNowUtils as util
import oracledb

def lambda_handler(event, context):
    sql = event["body"]
    try:
        # print(sql)
        logic.searchLogic(sql)
    

    except oracledb.Error as ex:
        error, = ex.args
        print(error.message)

        print("false at DB")
        return util.MKresponse({"message":"データベースでエラーが起きました"})
    except Exception as e:
        print("false at system")
        return util.MKresponse({"message":"aaa"})
    
    
    # 結果を作成する
    print("success")
    return util.MKresponse("success")
