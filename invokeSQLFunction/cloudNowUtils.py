import datetime
import json

def MKresponse(jsonData):
    """引数にJsonデータを入れると、APIレスポンスに変換して返す"""
    response = {
        "statusCode": 200,
        "statusDescription": "200 OK",
        "isBase64Encoded": False,
        "headers": {
        "Content-Type": "Aplication/json; charset=utf-8"
        }
    }
    response['body'] = json.dumps(jsonData, ensure_ascii=False)
    return response