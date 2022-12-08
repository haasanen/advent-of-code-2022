debug = False
grid = list() # type: list[list[int]]

with open("day8/input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if len(line) > 0:
            while len(grid) < len(line):
                grid.append(list())
            for index, height in enumerate(line):
                grid[index].append(int(height))

rows = len(grid)
columns = len(grid[0])

# First occurrence:
left_heights = list([list([-1 for _ in range(10)]) for _ in range(columns)])
right_heights = list([list([-1 for _ in range(10)]) for _ in range(columns)])
top_heights = list([list([-1 for _ in range(10)]) for _ in range(rows)])
bottom_heights = list([list([-1 for _ in range(10)]) for _ in range(rows)])

# Figure visibility boundaries
for row in range(rows):
    top = top_heights[row]
    bottom = bottom_heights[row]
    for column in range(columns):
        height = grid[row][column]
        left = left_heights[column]
        right = right_heights[column]
        for test_height, location in enumerate(left):
            if test_height > height:
                break
            if location != -1:
                continue
            left[test_height] = row
        for test_height, _ in enumerate(right):
            # By going from left to right, the right is filled differently
            if test_height > height:
                break
            else:
                right[test_height] = row
        for test_height, location in enumerate(top):
            if test_height > height:
                break
            if location != -1:
                continue
            top[test_height] = column
        for test_height, _ in enumerate(bottom):
            # By going from top to bottom, the bottom is filled differently
            if test_height > height:
                break
            else:
                bottom[test_height] = column

if debug:
    def debug_print(heights):
        def printer(number):
            if number > -1:
                return str(number)
            else:
                return "-"

        print(",".join([str(i) for i in range(10)]))
        print("-------------------")
        for i in heights:
            print(",".join(map(printer, i)))
        print("###################")

    debug_print(left_heights)
    debug_print(right_heights)
    debug_print(top_heights)
    debug_print(bottom_heights)

def is_visible(row, column, height):
    left = left_heights[column]
    right = right_heights[column]
    top = top_heights[row]
    bottom = bottom_heights[row]
    visible = left[height] >= row or right[height] <= row or top[height] >= column or bottom[height] <= column
    return visible

visibility_count = 0
for row in range(rows):
    for column in range(columns):
        height = grid[row][column]
        if is_visible(row, column, height):
            visibility_count += 1

print("Answer 1:", visibility_count)

# Brute force scenic score
def get_scenic_score(row, column):
    height = grid[row][column]
    score = 1
    counter = 0
    for test_row in range(row - 1, -1, -1):
        counter += 1
        test_height = grid[test_row][column]
        if test_height >= height:
            break
    score *= counter
    if debug:
        print(f"{row},{column}:", counter, end=" * ")
    counter = 0
    for test_row in range(row + 1, rows):
        counter += 1
        test_height = grid[test_row][column]
        if test_height >= height:
            break
    score *= counter
    if debug:
        print(counter, end=" * ")
    counter = 0
    for test_column in range(column - 1, -1, -1):
        counter += 1
        test_height = grid[row][test_column]
        if test_height >= height:
            break
    score *= counter
    if debug:
        print(counter, end=" * ")
    counter = 0
    for test_column in range(column + 1, columns):
        counter += 1
        test_height = grid[row][test_column]
        if test_height >= height:
            break
    score *= counter
    if debug:
        print(counter, "=", score)
    return score

highest_scenic_score = 1
for row in range(1, rows - 1):
    for column in range(1, columns - 1):
        highest_scenic_score = max(highest_scenic_score, get_scenic_score(row, column))

print("Answer 2:", highest_scenic_score)