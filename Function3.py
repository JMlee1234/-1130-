# # Function3.py
# # 함수의 기본값이 있는 경우
# def times(a=10, b=20):
#     return a*b

# # 호출
# print(times())
# print(times(5))
# print(times(5, 6))

# # 키워드 인자
# def userURI(server, port):
#     strURL = "http://" + server + ":" + port
#     return strURL

# # 호출
# print( userURI("credu.com", "80") )
# print( userURI(port="8080", server="credu.com") )

# # 가변인자는 입력되는 인자의 개수가 가변적인 경우
# # 인자에 *를 붙이면 가변인자(내부에서 Tuple)
# def union(*ar):
#     result = []
#     # HAM(0) | EGG(1) ==> ar이라는 가변인자
#     for item in ar:
#         # H(0) | A(1) | M(2)
#         # E(0) | G(1) | G(2)
#         for x in item:
#             # x라는 글자가 포함되어 있지 않다면 추가
#             if x not in result:
#                 result.append(x)
#     return result

# # 호출(중단점, Break Point)
# print( union("HAM","EGG") )
# print( union("HAM", "EGG", "SPAM") )

# 정의되지 않은 인자 처리
# def userURIBuilder(server, port, **user):
#     strURL = "http://" + server + ":" + port + "/?"
#     for key in user.keys():
#         strURL += key + "=" + user[key] + "&"
#     return strURL

# 호출
# print( userURIBuilder("naver.com", "80", id="kim", password="1234") )
# print( userURIBuilder("naver.com", "80", id="kim", password="1234", name="mike", age="30") )


# 람다 함수(간단하게 함수를 정의, 익명함수)
g = lambda x,y:x*y
print( g(3,4) )
print( g(5,6) )
