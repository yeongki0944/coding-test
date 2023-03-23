array = [i for i in range(20) if i%2 == 1]
print(array)


array2 = []
for i in range(20):
    if i%2 == 1:
        array2.append(i)

print(array2)

array3 = [i*i for i in range(1, 10)]
print(array3)

# 코테에 활용
# N x M 크기의 2차원 리스트 초기화시
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)


# N x M 잘못된 초기화 방법
n = 3
m = 4
array = [[0] * m] * n
print(array)
array[1][1] = 5
print(array)
'''
3개의 리스트가 모두 동일한 객체를 레퍼런스하기 때문

2차원 리스트 초기화시 리스트 컴프리핸션 이용하기
'''


'''
언더바(_)는 어떤 역할일까?

반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때
https://losskatsu.github.io/programming/py-underscore/#

'''