# default parameter

def my_function(country='korea'):
  print(f'I am from {country}')

# my_function()
# my_function('usa')

# collection parameter
def my_function_01(param):
  for x in param:
    print(x)

# my_function_01([1, 2, 3, 4])
# my_function_01((1, 2, 3, 4))

# prevent default parameter
def my_function_02(aaa, /):
  print(aaa)

# my_function_02(1)
# my_function_02(aaa=1)

# keyword only parameter
def my_function_03(*, bbb):
  print(bbb)

# my_function_03(1)
my_function_03(bbb=2)