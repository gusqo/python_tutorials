# compound interest calculator : Compound interest calculator는 원금(principal)과 이자가 누적되어 이자에 이자가 붙는 방식으로 계산되는 복리(Compound Interest)를 계산하는 도구입니다. 복리 계산은 다음과 같은 수식을 사용합니다:

# [ A = P * (1 + r / n)^t ]

# ( A )는 최종 금액 (원금 + 이자)
# ( P )는 초기 원금 (Principal)
# ( r )는 연이율 (Annual interest rate, 소수로 표현)
# ( n )는 연간 복리 계산 횟수 (Compounding frequency per year)
# ( t )는 시간 (연 단위, Time in years)



# while True:
#   principal = input('Enter the principal amount: ')
  
#   try:
#     principal = float(principal)
#   except ValueError:
#     print(f'{principal}은 유효한 입력값이 아닙니다.')
#     continue

#   if principal <= 0:
#     print('원금은 0보다 큰 값이어야 합니다.')
#     continue
#   else:
#     break

# while True:
#   rate = input('Enter the rate amount: ')
  
#   try:
#     rate = float(rate)
#   except ValueError:
#     print(f'{rate}은 유효한 입력값이 아닙니다.')
#     continue

#   if rate <= 0:
#     print('이자율은 0보다 큰 값이어야 합니다.')
#     continue
#   else:
#     break

principal = 0
rate = 0
time = 0

def get_compound_rate(prompt):
  while True:
    value = input(prompt)
    
    try:
      value = float(value)
    except ValueError:
      print(f'{value}은 유효한 입력값이 아닙니다.')
      continue

    if value <= 0:
      print('기간은 0보다 큰 값이어야 합니다.')
      continue
    else:
      break
  return value

principal = get_compound_rate('Enter the principal amount: ')
rate = get_compound_rate('Enter the rate amount: ')
time = get_compound_rate('Enter the time amount: ')

# pow(): pow(x, y) -> x의 y승
total = principal * pow((1 + rate / 100), time)

print(f'당신이 입력한 원금은 {principal}원이고, 연이율은 {rate}% 이며, {time}년 후에 받을 수 있는 총 금액은 {total}원 입니다.')