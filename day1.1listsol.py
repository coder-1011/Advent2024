import json

l1 =[]
l2 =[]
file_path="day1numlist.json"
with open(file_path, 'r') as file:
    lines = file.readlines()

for line in lines:
    num1, num2 = map(int, line.split())
    l1.append(num1)
    l2.append(num2)

l1.sort()
l2.sort()

sum=0
for num,num2 in zip(l1,l2):
    print(num,num2,abs(num-num2))
    sum+=abs(num-num2)

similarity =0
for num in l1:
    occ=0
    for num2 in l2:
        if num==num2:
            occ+=1
        elif num<num2:
            break
    similarity+=num*occ
print(sum,similarity)
