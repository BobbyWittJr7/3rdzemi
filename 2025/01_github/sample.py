# Sample.py

# sysモジュールを読み込むことで、コマンドライン引数を取得できるようにする
import sys

# コマンドライン引数が2つ未満（＝メッセージが指定されていない）場合
if len(sys.argv) < 2:
    # 使い方の説明を表示する
    print("使い方: python Sample.py 表示したい文字列")
else:
    # 2番目の引数（1番目はファイル名）を取得してメッセージとして扱う
    message = sys.argv[1]

    # 取得したメッセージを表示する
    print(f"あなたのメッセージ: {message}")