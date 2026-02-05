# 자료 묶음 문법: List, Tuple, (Set), Dictionary
# Set:
# - 인덱로 접근할 수 없다
# - 내부 요소를 수정할 수 없다
# - 중복된 요소가 포함될 수 없다. - 중복 데이터가 있을 경우 오류가 나지는 않지만 중복 데이터는 표현되지 않는다.
# - 순서가 없어서 매번 바뀐다
# - 중괄호를 사용한다

a = {1, 2, 3, 4, 5} # 숫자는 순서가 바뀌지 않는다
# print(a)

b = {'사과', '바나나', '체리', '파인애플'}
# print(b)

c = {True, 1, 2, 3} # True는 1, False는 0으로 인식. True와 1은 중복되어 하나만 표시
# print(c)

# 생성자 사용
d = set(('a', 'b', 'c'))
# print(d)
# print(type(d))

# 존재 여부
e = '사과' in b
# print(e)

# 요소 추가: add()
b.add('포도') # 추가 위치는 정해지지 않는다
# print(b)

# 여러 요소 추가: update()
b.update(a)
# print(b)

# 요소 삭제: remove(), discard(), pop()
# b.remove('망고') # 에러
# print(b)

b.discard('망고') # 에러가 나지 않는다
# print(b)

b.pop() # 임의의 요소 삭제
print(b)