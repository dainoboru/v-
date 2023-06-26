import pytest
import boto3
import json
import test_const

# Lambda関数の名前とリージョン　ハードコード非推奨かもTODO
FUNCTION_NAME = 'masterRead'
REGION_NAME = 'ap-northeast-1'
# Lambda関数を呼び出すヘルパー関数
def invoke_lambda_function():
    client = boto3.client('lambda', region_name=REGION_NAME)
    response = client.invoke(
        FunctionName=FUNCTION_NAME,
    )
    return json.loads(response['Payload'].read().decode('utf-8'))
    
    
# テスト
@pytest.mark.parametrize("expected", [
    ({'statusCode': 200, "body": test_const.master}),
 
])
def test_lambda_function(expected):
    response_payload = invoke_lambda_function()
#   ステータスコードのテスト 
    assert response_payload['statusCode'] == expected['statusCode']  
    # bodyの中身をテスト
    assert response_payload['body'] == expected['body']  
