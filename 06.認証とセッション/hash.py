from werkzeug.security import generate_password_hash as gph
from werkzeug.security import check_password_hash as cph

passwd = "hoge"

hashpass = gph(passwd)

print(cph(hashpass, passwd))