import pytest
import boto3
import json
import test_const
import time

# Lambda関数の名前とリージョン　ハードコード非推奨かもTODO
REGION_NAME = 'ap-northeast-1'
# Lambda関数を呼び出すヘルパー関数
def invoke_lambda_function_setup(payload):
    client = boto3.client('lambda', region_name=REGION_NAME)
    response = client.invoke(
        FunctionName='invokeSQLFunction',
        Payload=json.dumps({"body":payload}).encode('utf-8')
    )
    return json.loads(response['Payload'].read().decode('utf-8'))
    
def setup_module(module):
    print("\n*** setup_module ***")
    print(invoke_lambda_function_setup(test_const.READRDS_SETUP.split(";")))
    print("\n*** setup_module ***")
    

def teardown_module(moduloe):
    print("\n*** teardown_module ***")
    print(invoke_lambda_function_setup(test_const.READRDS_TEARDOWN.split(";")))
    print("\n*** teardown_module ***")
    

# Lambda関数の名前とリージョン　ハードコード非推奨かもTODO
FUNCTION_NAME = 'readRds'
REGION_NAME = 'ap-northeast-1'
# Lambda関数を呼び出すヘルパー関数
def invoke_lambda_function(payload):
    client = boto3.client('lambda', region_name=REGION_NAME)
    response = client.invoke(
        FunctionName=FUNCTION_NAME,
        Payload=json.dumps({"body":json.dumps(payload),"Environment":"test"}).encode('utf-8')
    )
    return json.loads(response['Payload'].read().decode('utf-8'))
    
# 全検索　
@pytest.mark.parametrize("input_data, expected", [
    ({'key': []}, {'len':11,'statusCode': 200})
])
def test_lambda_function(input_data, expected):
    response_payload = invoke_lambda_function(input_data)
    # print(response_payload)
    assert response_payload['statusCode'] == expected['statusCode']  
    assert len(json.loads(response_payload['body'])) == expected['len']


# 正常系のテスト
@pytest.mark.parametrize("input_data, expected", [
    ({'key': ['セキュリティ']}, {'statusCode': 200, 'column':['title']}),
    ({'key': ['AWS']}, {'statusCode': 200, 'column':['cloud_service']}),
    ({'key': ['接続']}, {'statusCode': 200, 'column':['detail']}),
    ({'key': ['EC2']}, {'statusCode': 200, 'column':['product_name']}),
    ({'key': ['SyntaxError']}, {'statusCode': 200, 'column':['error_message']}),
    ({'key': ['セキュリティ','AWS']}, {'statusCode': 200, 'column':['title','cloud_service']}),
    ({'key': ['接続','EC2']}, {'statusCode': 200, 'column':['detail','product_name']}),
    ({'key': ['SyntaxError','EC2']}, {'statusCode': 200, 'column':['error_message','product_name']}),
    ({'key': ['セキュリティ','接続','AWS']}, {'statusCode': 200, 'column':['title','detail','cloud_service']}),
    ({'key': ['SyntaxError','EC2','接続']}, {'statusCode': 200, 'column':['error_message','product_name','detail']}),
    ({'key': ['セキュリティ','接続','AWS','lambda']}, {'statusCode': 200, 'column':['title','detail','cloud_service','product_name']}),
    ({'key': ['SyntaxError','セキュリティ','接続','AWS','lambda']}, {'statusCode': 200, 'column':['error_message','title','detail','cloud_service','product_name']})
])
def test_lambda_function2(input_data, expected):
    response_payload = invoke_lambda_function(input_data)
    assert response_payload['statusCode'] == expected['statusCode']  
    for data in json.loads(response_payload['body']):
        for key in input_data['key']:
            assert any(key in data[column] for column in expected['column'])
    
# バリデーションチェックのテスト
@pytest.mark.parametrize("input_data, expected", [
    ({'key': ["12345678901234567890123456789012345678901"]}, {'body': '入力値が不正です', 'statusCode': 400}),
    ({'key':None}, {'body': '入力値が不正です', 'statusCode': 400})
])
def test_validation(input_data, expected):
    response_payload = invoke_lambda_function(input_data)
    assert response_payload == expected
    
