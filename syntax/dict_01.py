# 자료 묶음 문법: List, Tuple, Set, (Dictionary)
# Dictionary:
# - 중복이 허용되지 않는다
# - 변경이 가능하다
# - 순서가 없다
# - Key Value 쌍으로 구성된다.
# - 자바스크립트의 객체와 유사하다

a = {
  'name': 'marshall',
  'age': 20,
  'address': 'seoul',
  'gu': ['gangname', 'dobong', 'guro']
}

# print(a)
# print(type(a))

# 데이터 접근
# print(a['name'])
# print(a['gu'][0])

# get으로 접근
# print(a.get('name'))

# key값만 출력
# print(a.keys())

# 길이
# print(len(a))

# 생성자 사용
b = dict(name='marshall', age=20)
# print(b)

# 요소의 변경
a['age'] = 30
a.update({"name": "key"})

# 요소의 추가
a['color'] = ['red', 'green', 'blue']

# 반복문 사용
for x in a:
  print(a.get(x))

# print(a)