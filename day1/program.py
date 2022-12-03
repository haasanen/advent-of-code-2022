value = 0
values = list()
with open("day1/input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if len(line) > 0:
            value += int(line)
        else:
            values.append(value)
            value = 0

values.sort()

print("Answer 1:", values[-1])
print("Answer 2:", values[-1] + values[-2] + values[-3])