#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb

# 接続する
conn = MySQLdb.connect(
user='root',
passwd='root',
host='localhost',
db='mysql',
# テーブル内部で日本語を扱うために追加
use_unicode=True,
charset='utf8'
)

# カーソルを取得する
cursor = conn.cursor()

# テーブルの初期化
cursor.execute("DROP TABLE IF EXISTS purchase")

cursor.execute('''
    CREATE TABLE purchase(
    id_p int unsigned NOT NULL auto_increment,
    id_c int unsigned NOT NULL,
    id_g int unsigned NOT NULL,
    quality tinyint unsigned,

    PRIMARY KEY(id_p)
)'''
)

cursor.execute('''
    INSERT purchase SET id_c=3, id_g=2, quality=1
'''
)
cursor.execute('''
    INSERT purchase SET id_c=1, id_g=1, quality=3
'''
)
cursor.execute('''
    INSERT purchase SET id_c=4, id_g=1, quality=2
'''
)
cursor.execute('''
    INSERT purchase SET id_c=2, id_g=4, quality=1
'''
)
cursor.execute('''
    INSERT purchase SET id_c=4, id_g=2, quality=1
'''
)
cursor.execute('''
    INSERT purchase SET id_c=2, id_g=1, quality=1
'''
)

cursor.execute("DROP TABLE IF EXISTS customer")
cursor.execute('''
    CREATE TABLE customer(
    id_c int unsigned NOT NULL auto_increment,
    fullname varchar(40) NOT NULL,
    age tinyint unsigned NOT NULL,
    sex tinyint unsigned NOT NULL,
    email varchar(50),

    PRIMARY KEY(id_c)
)
'''
)

cursor.execute('''
    INSERT customer SET fullname='aaa', age='48', sex='2', email='hanako.yamada@sample.ne.jp';
'''
)
cursor.execute('''
    INSERT customer SET fullname='bbb', age='35', sex='1', email='tomoson.micheal@sample.ne.jp'
'''
)
cursor.execute('''
    INSERT customer SET fullname='ccc', age='38', sex='1', email='dean.donald@sample.ne.jp'
'''
)
cursor.execute('''
    INSERT customer SET fullname='ddd', age='18', sex='1', email='masaru.sato@sample.ne.jp'
'''
)
cursor.execute('''
    INSERT customer SET fullname='eee', age='28', sex='2', email='yuko.sasaki@sample.ne.jp'
'''
)
cursor.execute('''
    INSERT customer SET fullname='fff', age='23', sex='2', email='rena.micheal@sample.ne.jp'
'''
)
cursor.execute('''
    INSERT customer SET fullname='ggg', age='58', sex='2', email='kanako.oshima@sample.ne.jp'
'''
)

cursor.execute("DROP TABLE IF EXISTS goods")
cursor.execute('''
    CREATE TABLE goods(
    id_g tinyint(3) unsigned NOT NULL auto_increment,
    name varchar(30),
    price decimal(9,0),

    PRIMARY KEY(id_g)
    )
'''
)


cursor.execute('''
    INSERT goods SET name='123', price='200'
'''
)
cursor.execute('''
    INSERT goods SET name='456', price='430'
'''
)
cursor.execute('''
    INSERT goods SET name='789', price='600'
'''
)
cursor.execute('''
    INSERT goods SET name='111', price='150'
'''
)
# 内部
cursor.execute('''
    SELECT id_p, fullname FROM purchase JOIN customer ON purchase.id_c=customer.id_c
'''
)
cursor.execute('''
    SELECT purchase.id_g, name FROM goods INNER JOIN purchase ON purchase.id_g=goods.id_g
'''
)
cursor.execute('''
    select id_p, customer.id_c, fullname FROM customer JOIN purchase ON purchase.id_c = customer.id_c
'''
)
# 外部結合
cursor.execute('''
    SELECT purchase.id_g,name FROM goods LEFT OUTER JOIN purchase ON purchase.id_g=goods.id_g
'''
)
cursor.execute('''
    SELECT purchase.id_g,name FROM goods RIGHT JOIN purchase ON purchase.id_g=goods.id_g
'''
)
cursor.execute('''
    SELECT MAX(age) FROM customer 
'''
)



rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()

cursor.close

# 接続を閉じる
conn.close


