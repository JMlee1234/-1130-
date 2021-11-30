# DemoLoop3.py

lst = [1,2,3,4,5,6,7,8,9,10]

for i in lst:
    if i > 5:
        break
    print("Item:{0}".format(i))

print("---continue---")
for i in lst:
    if i % 2 == 1:
        continue
    print("Item:{0}".format(i))

