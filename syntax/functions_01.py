# function: def 키워드 사용

# def add(a, b):
#   return a + b

# print(add(1, 3))

# arbitary arguments
# def arb_func(*args):
#   # print('age is {}, name is {}'.format(args[0], args[1]))
#   print(args)
#   print(type(args)) # tuple

# arb_func('20', 'marshall')

# keyword arguments
def key_arg_func(**kwargs):
  print(kwargs)
  print(type(kwargs))
  print('age is {}, name is {}'.format(kwargs['age'], kwargs['name']))

key_arg_func(age='20', name='marshall')