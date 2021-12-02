# 클래스메서드.py
# 자바와 닷넷같은 경우 정적 메서드는 상속의 대상이 아님
# static methodA()
# 부모클래스
class CoeffVar(object):
    coefficient = 1 
    @classmethod
    def mul(cls, fact):
        return cls.coefficient * fact 

# 자식클래스
#파생형식을 정의
class MulFive(CoeffVar):
    coefficient = 5 

x = MulFive.mul(4)
print(x)


