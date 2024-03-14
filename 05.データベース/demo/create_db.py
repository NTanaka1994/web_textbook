# MySQLdbのインポート
import MySQLdb
 
# データベースへの接続関数
def connect():
    con = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="abc",
        db="sample")
    return con

# データベースの接続
con = connect()

# カーソルの生成
cur = con.cursor()
 
# ここに実行したいコードを入力します

cur.execute("""
            CREATE TABLE sample.thread
            (thread_id MEDIUMINT NOT NULL AUTO_INCREMENT,
            title VARCHAR(100) NOT NULL,
            intro VARCHAR(1000),
            create_date DATETIME NOT NULL,
            PRIMARY KEY(thread_id))
            """)

#cur.execute("""
#            CREATE TABLE sample.thread
#            (thread_id MEDIUMINT NOT NULL AUTO_INCREMENT,
#            title VARCHAR(100) NOT NULL,
#            intro VARCHAR(1000),
#            create_date DATETIME NOT NULL,
#            PRIMARY KEY(thread_id))
#            """)

# 保存を実行
con.commit()
 
# 接続を閉じる
con.close()