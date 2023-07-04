import json
import logic
import const
import cloudNowUtils as util
import oracledb
def lambda_handler(event, context):
    result={}
    try:
        # 検索のロジック
        result["env"] = util.dataFormat(logic.searchLogic(const.envSQL))
        result["div"] = util.dataFormat(logic.searchLogic(const.divSQL))
        result["pro"] = util.dataFormat(logic.searchLogic(const.proSQL))
        result["cate"] = util.dataFormat(logic.searchLogic(const.cateSQL))
        result["sys"] = util.dataFormat(logic.searchLogic(const.sysSQL))
        result["ser"] = util.dataFormat(logic.searchLogic(const.serSQL))
    except oracledb.Error as e:
        print("false at ")
        return util.MKresponse({"message":"データベースでエラーが起きました"})
    except Exception as e:
        print("false at system")
        return util.MKresponse({"message":"システムエラーが起きました"})
    
    
    # 結果を作成する
    print("success")
    return util.MKresponse(result)