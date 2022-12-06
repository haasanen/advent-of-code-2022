stacks = list() # type: list[list[str]]
stacks2 = None # type: list[list[str]]

def initialise_stacks(line):
    # Each column takes 4 space. Last column's last character is \n
    for _ in range(len(line) // 4):
        stacks.append(list())

def fill_stacks(line) -> bool:
    for i, stack in enumerate(stacks):
        position = i * 4 + 1 # Stacks width is 4 and interested character is at offset 1.
        character = line[position]
        character = character.strip() # Remove white space, i.e. the space character.
        if len(character) > 0:
            if i == 0:
                try:
                    int(character) # If we found an integer, we are done processing.
                    return True
                except ValueError:
                    pass
            stack.insert(0, character) # Very inefficient, but doesn't matter for these small lists.
    return False

def duplicate_stacks():
    stacks_copy = list()
    for stack in stacks:
        stack_copy = list()
        for item in stack:
            stack_copy.append(item)
        stacks_copy.append(stack_copy)
    return stacks_copy

def parse_move_line(line: str) -> tuple[int, int, int]:
    splits = line.split(" ")
    return int(splits[1]), int(splits[3]) - 1, int(splits[5]) - 1 # Re-index to start from 0 instead of 1

def move_items_9000(count, source, target):
    for _ in range(count):
        stacks[target].append(stacks[source].pop())

def move_items_9001(count, source, target):
    stack = stacks2[source]
    split =  stack[-count:]
    stacks2[source] = stack[:-count]
    stacks2[target].extend(split)

with open("day5/input.txt") as f:
    filled_stacks = False
    for line in f.readlines():
        if len(stacks) == 0:
            initialise_stacks(line)
        if not filled_stacks:
            filled_stacks = fill_stacks(line)
            if filled_stacks:
                stacks2 = duplicate_stacks()
            continue
        line = line.strip()
        if len(line) > 0:
            count, source, target = parse_move_line(line)
            move_items_9000(count, source, target)
            move_items_9001(count, source, target)

print("Answer 1:", "".join([stack[-1] for stack in stacks]))
print("Answer 2:", "".join([stack[-1] for stack in stacks2]))