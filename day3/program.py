def get_value(value):
    number = ord(value)
    if number > 96:
        return number - 96
    if number > 64:
        return number - 64 + 26
    print("not a-z or A-Z value")
    exit()

value = 0
value2 = 0
group = list()
with open("day3/input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if len(line) > 0:
            # First answer
            half = len(line) // 2
            first = line[:half]
            second = line[half:]
            filtered = filter(lambda x: x in first, second)
            extracted = [s for s in filtered][0]
            value += get_value(extracted)
            
            # Second answer
            if len(group) >= 3:
                group.clear()
            group.append(line)
            if len(group) == 3:
                filtered = filter(lambda x: x in group[0] and x in group[1], group[2])
                extracted = [s for s in filtered][0]
                value2 += get_value(extracted)

print("Answer 1:", value)
print("Answer 2:", value2)