## 開発プロセス
- クラウド９のデフォルトのpython ver 3.7で開発
- 開発前にgithubから最新のデータを取得＋自動テストが成功することの確認
- クラウド9で開発したデータをlambdaにアップ
- 開発後は自動テストが通ることを確認した後で、githubにpushする
## 自動テストの実行方法方法
- python ver 3.7
- python -m pytest testsの階層で
- pip install pytest
- AWSのライブラリ
- pip install boto3
