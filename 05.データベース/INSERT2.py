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

lists=[["鈴木","M","△△大学","教授",2],
       ["高橋","M","□□大学","講師",2],
       ["山田","F","◇◇大学","学生",3],
       ["松崎","M","▽▽高校","学生",3]]
for i in range(len(lists)):
    # データベースの接続
    con = connect()
    
    # カーソルの生成
    cur = con.cursor()
     
    # ここに実行したいコードを入力します
    cur.execute("""INSERT INTO list 
                (name,sex,school,post,admin) 
                VALUES (%(name)s,%(sex)s,%(school)s,%(post)s,%(admin)s)""",
                {"name":lists[i][0], "sex":lists[i][1], "school":lists[i][2],
                 "post":lists[i][3], "admin":lists[i][4]})
    
    # 保存を実行
    con.commit()
     
    # 接続を閉じる
    con.close()