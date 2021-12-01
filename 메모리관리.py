# 메모리관리.py 

class MyClass:
    def __init__(self, value):
        self.value = value 
        print("Instance is created! value=", value)
    def __del__(self):
        print("Instance is deleted!")

d = MyClass(5)
del d 

