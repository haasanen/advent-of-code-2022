def is_subset(range1, range2):
    return range1[0] <= range2[0] and range1[1] >= range2[1]

def get_ranges(value):
    splits = value.split("-")
    first, second = splits[0], splits[1]
    return [int(first), int(second)]

def is_subset_or_superset(first, second):
    ranges1 = get_ranges(first)
    ranges2 = get_ranges(second)
    return is_subset(ranges1, ranges2) or is_subset(ranges2, ranges1)

def is_start_overlapping(ranges1, ranges2):
    return ranges1[0] >= ranges2[0] and ranges1[0] <= ranges2[1]

def is_end_overlapping(ranges1, ranges2):
    return ranges1[1] >= ranges2[0] and ranges1[1] <= ranges2[1]

def is_overlapping(first, second):
    ranges1 = get_ranges(first)
    ranges2 = get_ranges(second)
    return is_start_overlapping(ranges1, ranges2) or is_start_overlapping(ranges2, ranges1)\
        or is_end_overlapping(ranges1, ranges2) or is_end_overlapping(ranges2, ranges1)

value = 0
value2 = 0
with open("day4/input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if len(line) > 0:
            splits = line.split(",")
            first, second = splits[0], splits[1]
            if is_subset_or_superset(first, second):
                value += 1
            if is_overlapping(first, second):
                value2 += 1

print("Answer 1:", value)
print("Answer 2:", value2)