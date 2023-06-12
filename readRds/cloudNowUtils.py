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

def nullToBrank(datas):
    """データ内のヌルを空文字に変換"""
    result=[]
    for record in datas:
        newRecord=[]
        for data in record:
            if data is None:
                data=""
            newRecord.append(data)
        result.append(newRecord)
    return result
    
def intToStr(datas):
    """データ内のヌルを空文字に変換"""
    result=[]
    for record in datas:
        newRecord=[]
        for data in record:
            if type(data)==int:
                data=str(data)
            newRecord.append(data)
        result.append(newRecord)
    return result

def listToJson(data):
    """ListDataとプロパティ名の配列をもとにJsondataを返す"""
    searchJson =[]
    for i in data:
        mergeJson = dict(zip(const.CNproperty,i))
        searchJson.append(mergeJson)
    return searchJson

def strToList(lists):
    listProperty=["cloud_service",'product_name','category','reference']
    result=[]
    for record in lists:
        resultRecord=[]
        for prop in listProperty:
            record[prop]=list(set(record[prop].split(",")))
    return lists
    
def dataFormat(data):
     # 検索結果のNULLを空文字に変換
    data=nullToBrank(data)
    
    # 検索結果の数値データを文字に変換
    data=intToStr(data)
    
    # 検索結果をJson化する
    JsonResult = listToJson(data)
    
    # 複数データを持つプロパティをリスト化する
    result=strToList(JsonResult)
    
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