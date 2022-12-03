def is_rock(value):
    return value == "A" or value == "X"
def is_paper(value):
    return value == "B" or value == "Y"
def is_scissors(value):
    return value == "C" or value == "Z"

def should_lose(value):
    return value == "X"
def should_draw(value):
    return value == "Y"
def should_win(value):
    return value == "Z"

def get_item_value(value):
    if is_rock(value):
        return 1
    if is_paper(value):
        return 2
    if is_scissors(value):
        return 3
    print("unknown item type")
    exit()

def get_win_item(value):
    if is_rock(value):
        return "B" # Paper
    if is_paper(value):
        return "C" # Scissors
    if is_scissors(value):
        return "A" # Rock
    print("unknown win item")
    exit()

def get_draw_item(value):
    return value

def get_lose_item(value):
    if is_rock(value):
        return "C" # Scissors
    if is_paper(value):
        return "A" # Rock
    if is_scissors(value):
        return "B" # Paper
    print("unknown lose item")
    exit()

def is_win(them, me):
    if is_rock(them) and is_paper(me):
        return True
    if is_paper(them) and is_scissors(me):
        return True
    if is_scissors(them) and is_rock(me):
        return True
    return False

def is_draw(them, me):
    if is_rock(them) and is_rock(me):
        return True
    if is_paper(them) and is_paper(me):
        return True
    if is_scissors(them) and is_scissors(me):
        return True
    return False

def get_win_value(them, me):
    if is_win(them, me):
        return 6
    elif is_draw(them, me):
        return 3
    else:
        return 0

def get_should_win_value(them, me):
    if should_win(me):
        return 6 + get_item_value(get_win_item(them))
    if should_draw(me):
        return 3 + get_item_value(get_draw_item(them))
    if should_lose(me):
        return 0 + get_item_value(get_lose_item(them))
    print("unknown win type")
    exit()

def get_score(them, me):
    value = get_item_value(me)
    value += get_win_value(them, me)
    return value

value = 0
value2 = 0
with open("day2/input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if len(line) > 0:
            them = line[0]
            me = line[2]
            
            value += get_score(them, me)
            value2 += get_should_win_value(them, me)
        
print("Answer 1:", value)
print("Answer 2:", value2)