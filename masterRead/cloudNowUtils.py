import datetime
import json
import const
def dateTranslate(tapuru):
    """引数にタプル　返り値はリスト　datetime.datetime型のデータを文字列に変換する"""
    result =[]
    for data in tapuru:
        if type(data)==datetime.datetime:
            result.append(data.strftime('%Y/%m/%d'))
        else:
            result.append(data)
    return result

def dataFormat(data):
    #  [['部署1'], ['部署10'], ['部署11']]=>[{ value:'部署1', label: '部署1' }]
    result = []
    for d in data:
        result.append({"value":d[0],"label":d[0]})
    return result

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