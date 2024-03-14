import MySQLdb

def connect():
    con = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="abc",
        db="sample",
        use_unicode=True,
        charset="utf8")
    return con

con = connect()
cur = con.cursor()
cur.execute("""
            CREATE TABLE users
            (id MEDIUMINT NOT NULL AUTO_INCREMENT,
            name VARCHAR(50),
            email VARCHAR(200),
            tel VARCHAR(50),
            passwd VARCHAR(300),
            PRIMARY KEY(id))
            """)
con.commit()
con.close()