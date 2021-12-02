# 메모리관리.py 

class MyClass:
    # 생성자(초기화 담당)
    def __init__(self, value):
        self.value = value 
        print("Instance is created! value=", value)
    # 소멸자메서드(마지막에 정리 작업)
    def __del__(self):
        print("Instance is deleted!")

# 인스턴스 생성
d = MyClass(5)
#del d 

print("코드 실행 종료")

