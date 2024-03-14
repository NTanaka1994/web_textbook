# MySQLdbのインポート
import MySQLdb
 
# データベースへの接続関数
def connect():
    con = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="abc",
        db="sample",
        use_unicode=True,
        charset="utf-8")
    return con

# データベースの接続
con = connect()

# カーソルの生成
cur = con.cursor()
 
# ここに実行したいコードを入力します
cur.execute("""
            CREATE TABLE sample.list2
            (id MEDIUMINT NOT NULL AUTO_INCREMENT,
            name VARCHAR(30),
            sex CHAR(1),
            school VARCHAR(30),
            post VARCHAR(10),
            admin int(1),
            PRIMARY KEY(id))
            """)

# 保存を実行
con.commit()
 
# 接続を閉じる
con.close()