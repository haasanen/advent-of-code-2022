def find_unique_substring(line, length):
    index = 0
    while index < len(line) - length:
        substring = line[index:index + length]
        if len(set(substring)) == length:
            return index + length # Answer is after the substring
        index += 1
    return -1 # Not found!

line = None # type: str
with open("day6/input.txt") as f:
    line = f.readline().strip()

print("Answer 1:", find_unique_substring(line, 4))
print("Answer 2:", find_unique_substring(line, 14))