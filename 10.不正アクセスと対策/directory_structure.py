dire = "static/public/"
file = "public.txt"
f = open(dire+file, mode="r", encoding="utf-8")
print("正常アクセス-----------------")
print("ファイルの中身")
print(f.read())
print()
print("ファイルのパス")
print(dire+file)
f.close()
print()
dire2 = "static/public/"
path = dire2 + "../private/"
file2 = "private.txt"
f = open(path+file2, mode="r", encoding="utf-8")
print("不正アクセス-----------------")
print("ファイルの中身")
print(f.read())
print()
print("ファイルのパス")
print(path+file2)
f.close()