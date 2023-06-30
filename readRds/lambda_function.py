import json
import logic
import cloudNowUtils as util
import validation
import oracledb
def lambda_handler(event, context):
    # 検索キーの取得  例：event={body:{key:["AWS","Lambda"]}}
    try:
        environment =  "_test" if event.get("headers", {}).get("Environment") is not None else ""
           
        event = json.loads(event["body"])
        searchKeys=event["key"]
        
        # 入力チェック
        if not(validation.searchWordCheck(searchKeys)):
            return {
                'statusCode': 400,
                "body":"入力値が不正です"}
        
    
    # 検索のロジック　検索キーワードない場合は全検索の結果を返す
        searchResult = logic.searchMulti(searchKeys,environment)
          # データベースから取り出したデータをレスポンス用のデータに加工
        result=util.dataFormat(searchResult)    
         # 結果を作成する
        return util.MKresponse(result)
    except oracledb.Error as e:
        return {
            'statusCode': 500,
            "body":"データベースでエラーが起きました"}
    except Exception as e:
        return {
            'statusCode': 500,
            "body":"システムエラーが起きました"}
    
  
    
   