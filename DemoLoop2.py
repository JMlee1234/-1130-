# DemoLoop2.py

lst=[1,2,3]

for i in lst:
    print(i)


print("---break구문---")
lst=[1,2,3,4,5,6,7,8,9,10]
#프리즌 브레이크(탈옥)
for item in lst:
    if item > 5:
        break
    print("Item:{0}".format(item))



lst = [1,2,3,4,5]
[i**2 for i in lst]

test = ("apple", "banana", "orage")
[len(i) for i in test]

d = {100:"apple", 200:"banana", 300:"orage"}
