file_path="day2.1.json"
with open(file_path, 'r') as file:
    lines = file.readlines()
count=0

def safe(line):
    nlist= list(map(int,line.split()))
    differs=[a-b for a,b in zip(nlist,nlist[1:])]
    is_monotonic= all(i > 0 for i in differs) or all(i < 0 for i in differs)
    is_in_range = all(0 < abs(i) <= 3 for i in differs)
    if is_monotonic and is_in_range:
        return True
    return False

def safe2(line):
    nlist= list(map(int,line.split()))
    for i in range(len(nlist)):
        tolerated_levels = nlist[:i] + nlist[i + 1 :]
        tolerated_line = " ".join(map(str, tolerated_levels))
        if safe(tolerated_line):
            return True
            break
    return False

for line in lines:
    if(safe(line)):
        count+=1
print(count)

print("part 2")
for line in lines:
    if(safe(line)):
        count+=1
    elif(safe2(line)):
        count+=1
    else:
        pass
print(count)