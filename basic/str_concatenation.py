# 문자열 연결
a = "hello"
b = " world"
print(a + b)

# 문자열 포멧팅
name = 'Alice'
age = 20
txt = "내 이름은 {1}이고, 나이는 {0}살 입니다.".format(age, name)
print(txt)

# f-string
print(f'내 이름은 {name}이고, 나이는 {age}살 입니다.')

# escape: https://zzozzomin08.tistory.com/39
# 1. 내부 특수문자
hello = "hello. my age is \\\"20\\\" years old."
print(hello)

# 2. 문자열 개행
hello = "hello \nmy age is 20 years old."
print(hello)

# 3. 문자열 탭
hello = "hello\tmy age is 20 years old."
print(hello)

# 4. 백스페이스
hello = "hello\bmy age is 20 years old."
print(hello)