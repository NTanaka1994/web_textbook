def fizzbuzz(start=0, end=50):
    fizz = []
    buzz = []
    fizzbuzz = []
    for i in range(start, end+1, 1):
        if (i % 3)==0 and (i % 5)==0 and i != 0:
            print("FizzBuzz")
            fizzbuzz.append(i)
        elif (i % 3)==0 and i != 0:
            print("Fizz")
            fizz.append(i)
        elif (i % 5)==0 and i != 0:
            print("Buzz")
            buzz.append(i)
        else:
            print(i)
    return fizz, buzz, fizzbuzz

def odd(ary):
    for i in range(len(ary)):
        if (ary[i] % 2) == 0:
            print(ary[i])
    pass

print("FizzBussの実行")
fizz, buzz, fzbz = fizzbuzz(1, 30)
print("3の倍数で偶数")
odd(fizz)
print("5の倍数で偶数")
odd(buzz)
print("3の倍数かつ5の倍数で偶数")
odd(fzbz)