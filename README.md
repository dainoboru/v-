## 開発プロセス
- クラウド９のデフォルトのpython ver 3.7で開発
- 開発前にgithubから最新のプログラムを取得＋自動テストが成功することの確認
- クラウド9で開発したプログラムをlambdaにアップ　（クラウド９のGUIから可能）
- 開発後は自動テストが通ることを確認した後で、githubにpushする

## 開発環境
- pip install pytest
- pip install boto3（AWSのライブラリ）
  
## 自動テストの実行方法
- python ver 3.7
- testsの階層で　'python -m pytest' コマンドを打つ
  
## 自動テストの作成方法
- testsのフォルダ内部にtest_(lambdaのファイル名)のテスト用ファイルを作成
- 事前処理事後処理の部分で、invokeSQLFunctionをつかってテスト用のテーブルを作成・データの挿入
- 他のテストファイルを参考にテストの作成

  
