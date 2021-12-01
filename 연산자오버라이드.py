#연산자 오버라이드 
class NumBox:
	def __init__(self, num):
		self.Num = num
	def __add__(self, num):
		self.Num += num
	def __sub__(self, num):
		self.Num -= num

#인스턴스 생성
n = NumBox(40)
n + 100 
print(n.Num)
n - 110 
print(n.Num)
