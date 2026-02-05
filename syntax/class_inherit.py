# 클래스 기능 상속(확장)

class Person:
  # self는 객체 자신(defult)
  def __init__(self, fname, lname): 
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
    
y = Person('marshall', 'han')
y.printname()

class Student(Person): # Person 클래스 기능을 상속 받음
  def __init__(self, fname, lname, year):
    #super(): 부모 클래스의 생성자 호출 함수
    super().__init__(fname, lname) # self를 제외한 부모 클래스의 생성자 호출
    self.graduationyear = year

  def printname(self):
    print(self.firstname, self.lastname, self.graduationyear)

x = Student('marshall', 'han', 2020)
x.printname()