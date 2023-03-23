'''
append()

sort()

reverse()

insert()

count()

remove()
'''


a = [1, 4, 3]
print("default list : ", a)

a.append(2)
print("append : ", a)

# 오름차순
a.sort(reverse=False)
print("sort : ", a)

# 내림차순
a.sort(reverse=True)
print("sort : ", a)

# 리스트 원소 뒤집기
a.reverse()
print("reverse list : ", a)

a.insert(2, 0)
print("insert 0 into index 2 : ", a)

print("count data with a value of 3 : ", a.count(3))

a.remove(1)
print("remove data with a value of 1 : ", a)
