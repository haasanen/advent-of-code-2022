debug = False
debug_large = True
def debug_print_small(rope):
    debug_print(rope, 0, 6, 0, 5)

def debug_print_large(rope):
    debug_print(rope, -12, 15, -5, 16)

def debug_print(rope, min_x, max_x, min_y, max_y):
    head = rope[0]
    tail = rope[-1]
    for y in range(max_y -1, min_y -1, -1):
        for x in range(min_x, max_x, 1):
            marker = "."
            if x == 0 and y == 0:
                marker = "s"
            if tail[0] == x and tail[1] == y:
                marker = "T"
            for index in range(len(rope) - 2, 0, -1):
                knot = rope[index]
                if knot[0] == x and knot[1] == y:
                    marker = str(index)
            if head[0] == x and head[1] == y:
                marker = "H"
            print(marker, end="")
        print()
    print()

def move_knot(previous, current, visited: set[(int, int)]):
    dx = previous[0] - current[0] # difference in x
    dy = previous[1] - current[1] # difference in y
    adx = abs(dx) # absolute difference in x
    ady = abs(dy) # absolute difference in y
    if adx <= 1 and ady <= 1:
        # Adjacent
        return
    if dy > 0:
        current[1] += 1
    if dy < 0:
        current[1] -= 1
    if dx > 0:
        current[0] += 1
    if dx < 0:
        current[0] -= 1
    if None is not visited:
        visited.add((current[0], current[1]))

def move_rope(line: str, rope, visited):
    splits = line.split()
    direction, moves = splits[0], int(splits[1])
    if debug:
        print("Line:", line)

    head = rope[0]
    for _ in range(moves):
        if direction == "U": # up
            head[1] += 1
        elif direction == "D": # down
            head[1] -= 1
        elif direction == "L": # left
            head[0] -= 1
        elif direction == "R": # right
            head[0] += 1
        for index in range(len(rope) - 1):
            add_to = None
            is_tail = index + 1 == len(rope) - 1
            if is_tail:
                add_to = visited
            move_knot(rope[index], rope[index + 1], add_to)
        if debug:
            if debug_large:
                debug_print_large(rope)
            else:
                debug_print_small(rope)

rope2 = list([[0, 0] for _ in range(2)])
rope10 = list([[0,0] for _ in range(10)])
visited2 = {(0, 0)}
visited10 = {(0, 0)}
if debug:
    if debug_large:
        debug_print_large(rope10)
    else:
        debug_print_small(rope10)

with open("day9/input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if len(line) > 0:
            move_rope(line, rope2, visited2)
            move_rope(line, rope10, visited10)

print("Answer 1:", len(visited2))
print("Answer 2:", len(visited10))