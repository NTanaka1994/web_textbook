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
        charset="utf8")
    return con

# データベースの接続
con = connect()

# カーソルの生成
cur = con.cursor()
 
# ここに実行したいコードを入力します
cur.execute("""INSERT INTO list 
            (name,sex,school,post,admin) 
            VALUES ('田中','F','○○大学','学生',3)""")

# 保存を実行
con.commit()
 
# 接続を閉じる
con.close()