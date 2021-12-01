# Function1.py
# 함수를 정의
def setValue(newValue):
    # 함수 내부에서 초기화하면 지역변수(Local variable)
    x = newValue
    print("힘수내부:", x)


# 함수를 호출
result = setValue(5)
print(result)

# 다중의 값을 리턴
def swap(x,y):
    return y,x

#호출
result = swap(5,6)
print(result)
print( result[0], result[1] )

# 디버깅연습(교집합문자를 리턴)
def union(prelist, postlist):
    # 교집합 문자를 저장하기 위한 지역 변수
    result = []
    # H(0) | A(1) | M(2)
    for x in prelist:
        # X라는 글자가 postlist에 있고 x가 result에 없으면
        if x in postlist and x not in result:
            # 리스트형식에 추가
            result.append(x)
    return result

# 호출
print( union("HAM", "SPAM") )
