# DemoFile.py
# import sys

# print("hello", "python", sep="~", end="!", file=sys.stderr)

# # 파일을 다루는 객체를 생성
# f = open("c:\\work\\demo.txt", "wt")
# print("파일에 쓰는 작업", file=f)
# f.close()

# 문자열을 결합하는 경우
ur1 = "http://www.naver.com/?page=" + str(1)
print(ur1)

#문자열 정렬
for x in range(1,6):
    print(x, "*", x, "=", x*x)

print("---오른쪽 정렬---")
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).rjust(3))


print("---0으로 채우기---")
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).zfill(3) )




