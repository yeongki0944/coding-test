
a = 0.3 + 0.6
print(a)

# 0.3 + 0.6 = 0.8999999999999999
# 값 비교시 round()함수를 사용해서 반올림하는 것이 안전하다.

if a == 0.9:
    print(True)
else:
    print(False)

# round( 실수값, 반올림하고자하는 위치 -1 )
print(round(a, 1))
if round(a, 1) == 0.9:
    print(True)
else:
    print(False)

a = 0.1234
print(round(a))
print(round(a, 1))
print(round(a, 2))
print(round(a, 3))
print(round(a, 4))