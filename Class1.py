# Class1.py
# 1) 클래스 형식을 정의(원본):쿠키틀
class Person:
    #생성자(초기화) 메서드
    num_person = 0
    def __init__(self):
        #인스턴스의 멤버 변수를 초기화
        self.name = "default name"
        Person.num_person += 1
    def print(self):
        print("My name is {0}".format(self.name))

# 2)이스턴스 생성(복사본):쿠키
# 디버깅할 때 멈춤(Break Point)
p1 = Person()
p1.print()
p2 = Person()
p2.name = "전우치"
p2.print()

# 런타임(코드가 실행될 때) 변수를 추가할 수 있는
# 동적 형식의 언어
# 디자인타임(코드를 개발중)
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)

print("숫자:{0}".format(Person.num_person))
