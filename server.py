from flask import Flask, jsonify, request

# アプリケーションのインスタンス作成
# (インスタンス生成時の引数にはアプリケーション名を指定する)
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

db_data = [
    {'title': 'テスト1', 'body': '本文1本文1本文1'},
    {'title': 'テスト2', 'body': '本文2本文2本文2'},
    {'title': 'テスト3', 'body': '本文3本文3本文3'},
]

# ルーティング
# http://localhost/
@app.route('/', methods=['GET'])
def index():
    return 'hello'

@app.route('/posts', methods=['GET'])
def posts_index():
    res = db_data
    return jsonify(res)

@app.route('/posts/<id>', methods=['GET'])
def post(id):
    res = db_data[int(id)]
    return jsonify(res)


# 起動(コマンドラインから flask run する場合は不要)
if __name__ == "__main__":
    # app.debug = True
    app.run(host='localhost')