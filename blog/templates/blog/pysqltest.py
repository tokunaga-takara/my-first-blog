import MySQLdb
import traceback

try: 
    conn = MySQLdb.connect(
    user='root',
    passwd='root',
    host='localhost',
    db='mysql',
    use_unicode=True,
    charset="utf8"
    )

    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS test")

    cursor.execute('''
    CREATE TABLE test(
    test_id int(11) NOT NULL PRIMARY KEY,
    test_text varchar(64),
    )'''
    )
    
    query = "insert into test values('2','あああ')"

    cursor.execute(query)

except:
    cursor.close()
    conn.close()
    print(traceback.format_exc()) 

cursor.close()
conn.commit()
conn.close()