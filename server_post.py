from flask import Flask, jsonify, request
import json

# アプリケーションのインスタンス作成
# (インスタンス生成時の引数にはアプリケーション名を指定する)
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

db_data = [
    {'title': 'テスト1', 'body': '本文1本文1本文1'},
    {'title': 'テスト2', 'body': '本文2本文2本文2'},
    {'title': 'テスト3', 'body': '本文3本文3本文3'},
    {'title': 'テスト4', 'body': '本文4本文4本文4'},
    {'title': 'テスト5', 'body': '本文5本文5本文5'},
]

# ルーティング
# http://localhost/
@app.route('/', methods=['GET'])
def index():
    return 'hello'

@app.route('/posts', methods=['GET'])
def posts_index():
    # クエリの受け取りかた
    limit = request.args['limit']
    print(limit)
    res = db_data[:int(limit)]
    return jsonify(res)

@app.route('/posts/<id>', methods=['GET'])
def post(id):
    res = db_data[int(id)]
    return jsonify(res)


# ==================================

@app.route('/posts/add', methods=['POST'])
def add_post():
    post = request.json
    db_data.append(post)
    print(db_data)
    return jsonify(db_data)

@app.route('/posts/update/<id>', methods=['PUT'])
def update_post(id):
    post = request.json
    db_data[int(id)] = post
    print(db_data)
    return jsonify(db_data)

@app.route('/posts/delete/<id>', methods=['DELETE'])
def delete_post(id):
    db_data.pop(int(id))
    return jsonify(db_data)

# POSTリクエストのテスト
# curl -X POST -H "Content-Type: application/json" -d '{"title":"test", "body":"body"}' localhost:5000/posts/add


# 起動(コマンドラインから flask run する場合は不要)
if __name__ == "__main__":
    # app.debug = True
    app.run(host='localhost')