# DemoStr.py
# print(dir(str))

names = ["전우치", "홍길동","이순신"]
for name in names:
    print("안녕하세요 {0}님 추운 겨울입니다.".format(name))
    print("=" * 40)

strA = "Python is very powerful"
print(len(strA))
print(strA.capitalize())
print(strA.count("p"))
print(strA.count("p",7))
print("demo.ppt".endswith("ppt"))
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

strB = "<<<   spam and ham  >>>"
print(strB)
result = strB.strip("<> ")
print(result)
result=result.replace("spam","spam egg")
print(result)
lst = result.split()
print(lst)
print("---다시 하나로 합치기---")
print(" ".join(lst))
