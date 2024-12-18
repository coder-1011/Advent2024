import re0
file_path="day3_1input.txt"
with open(file_path, 'r') as file:
    lines = file.readlines()



pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, "".join(lines))
result = sum(int(x) * int(y) for x, y in matches)
print(result)