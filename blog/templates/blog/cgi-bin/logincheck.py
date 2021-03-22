#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import MySQLdb

form = cgi.FieldStorage() # cgiオブジェクト作成
username = form.getfirst('username')
password = form.getfirst('password')

# 接続する
conn = MySQLdb.connect(
user='root',
passwd='root',
host='localhost',
db='mysql',
# テーブル内部で日本語を扱うために追加
charset='utf8'
)
# カーソルを取得する
cursor = conn.cursor()
# テーブルの初期化
cursor.execute("DROP TABLE IF EXISTS userdata")
# テーブルの作成
cursor.execute("""CREATE TABLE userdata(
    id INT(11) AUTO_INCREMENT NOT NULL, 
    username VARCHAR(30) NOT NULL COLLATE utf8mb4_unicode_ci, 
    password VARCHAR(30) NOT NULL,
    PRIMARY KEY (id)
    )""")
#データの追加
cursor.execute("""INSERT INTO userdata (username, password)
    VALUES ('taro', '12345678'),
    ('jiro', 'abcdefgh'),
    ('saburo', '1234abcd')
    """)

# パスワードチェック
cursor.execute(f'SELECT * FROM userdata WHERE username = "{username}" AND password = "{password}"')

loginname = ""
if len(cursor.fetchall()) != 0:
    msg = "成功"
    loginname = cursor.fetchone()
    cursor.execute(f'UPDATE userdata SET username = "ichiro" WHERE username = "{loginname}"')
else:
    msg = "失敗"


# 更新
# 削除
#cursor.execute(f'DELETE FROM userdata WHERE username = "jiro"')
# 検索
cursor.execute(f'SELECT * FROM userdata')
users = []
rows = cursor.fetchall()
for row in rows:
    users.append(row)


# ブラウザに戻すHTMLのデータ
print("Content-Type: text/html")
print()
htmlText = f'''
<!DOCTYPE html>
<html>
    <head><meta charset="shift-jis" /></head>
<body>
    <p>{loginname}ログインに{msg}しました。<br/></p>
    <div>{users}</div><br/>
    <a href="../login.html">戻る</a>　
</body>
</html>
'''
print( htmlText.encode("cp932", 'ignore').decode('cp932') )