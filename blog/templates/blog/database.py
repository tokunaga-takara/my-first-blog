import MySQLdb

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
cursor.execute("DROP TABLE IF EXISTS name_age_list")

# テーブルの作成
cursor.execute("""CREATE TABLE name_age_list(
    id INT(11) AUTO_INCREMENT NOT NULL, 
    name VARCHAR(30) NOT NULL COLLATE utf8mb4_unicode_ci, 
    age INT(3) NOT NULL,
    PRIMARY KEY (id)
    )""")

# データの追加
cursor.execute("""INSERT INTO name_age_list (name, age)
    VALUES ('タロー', '25'),
    ('ジロー', '23'),
    ('サブロー', '21')
    """)
# 一覧の表示
cursor.execute("SELECT * FROM name_age_list")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()

cursor.close

# 接続を閉じる
conn.close