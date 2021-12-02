# DemoFile2.py

# 서식지정
print("{0:b}".format(10))
print("{0:x}".format(10))
print("{0:,}".format(15000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))

# 파일에 읽기와 쓰기
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("한글\nabcd\n세번째\n")
f.close()

# 읽기
f = open("c:\\work\\demo.txt", "rt", encoding="utf-8")
# 처음부터 끝까지 읽어서 하나의 str 변수로 리턴
print(f.read())
print("어디쯤:", f.tell() )
# 처음으로 가기(리셋)
f.seek(0)
# 한번에 한줄씩 읽기
print(f.readline())
print(f.readline())
f.seek(0)
# 전체를 읽어서 리스트로 리턴
result = f.readlines()
print(result)
