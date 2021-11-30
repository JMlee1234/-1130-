# DemoLoop.py
value = 5
while value > 0:
    print(value)
    value -= 1

print("---for in루프---")
lst = [100, "apple", 3.14]
for item in lst:
    print(item, type(item))


d={"apple":100, "kiwi":200}
for item in d.items():
    print(item)

print("---키만 출력---")
for k in d.keys():
    print(k)

print("---값만 출력---")
#디버깅 모드로 실행할 때 만나면 멈추는 중단점(Break Point)
for v in d.values():
    print(v)

#구구단 출력
#outer에 해당되는 for in루프
for x in [2,3,4,5,6,7,8,9]:
    print("---{0}단 출력---".format(x))
    # inner에 해당되는 for in루프
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(x,y,x*y))


