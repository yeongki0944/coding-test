a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]

a.remove(1)
print(a)
a.remove(1)
print(a)
a.remove(1)
print(a)

# 파이썬에서 한번에 중복된 값을 삭제해 주는 함수가 없다

# 리스트 컴프리헨션으로 처리 가능하다
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result)

