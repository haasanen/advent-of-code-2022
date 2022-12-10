debug = False
def update_cpu_cycles(clock, cycles: list[int]):
    if clock > 20:
        cycles_index = ((clock - 20) // 40) + 1
        if cycles_index >= len(cycles):
            cycles.append(cycles[-1]) # Add new cycle!

def process_cpu_instruction(line: str, clock, cycles):
    if line == "noop":
        update_cpu_cycles(clock + 1, cycles)
        return 1
    splits = line.split()
    instruction, value = splits[0], int(splits[1])
    if instruction == "addx":
        update_cpu_cycles(clock + 2, cycles)
        if debug:
            marker = "+"
            if value < 0:
                marker = "-"
            print(f"[{clock + 2}]: {cycles[-1]} {marker} {abs(value)} = {cycles[-1] + value}")
        cycles[-1] += value
        return 2

def draw_crt_cycles(clock, cycles: list[int], crt_pointer):
    marker = "."
    if abs(((clock - 1) % 40) - crt_pointer) <= 1:
        marker = "#"
    cycles[-1] += marker
    cycles_index = (clock // 40)
    if cycles_index >= len(cycles):
        cycles.append("")

def process_crt_instruction(line: str, clock, cycles, crt_pointer):
    if line == "noop":
        draw_crt_cycles(clock + 1, cycles, crt_pointer)
        return crt_pointer
    splits = line.split()
    instruction, value = splits[0], int(splits[1])
    if instruction == "addx":
        draw_crt_cycles(clock + 1, cycles, crt_pointer)
        draw_crt_cycles(clock + 2, cycles, crt_pointer)
        return crt_pointer + value

cpu_cycles = [1]
clock = 0
crt_cycles = [""]
crt_pointer = 1
clock = 0
with open("day10/input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if len(line) > 0:
            add_to_clock = process_cpu_instruction(line, clock, cpu_cycles)
            crt_pointer = process_crt_instruction(line, clock, crt_cycles, crt_pointer)
            clock += add_to_clock

print("Answer 1:", sum([cpu_cycles[index] * value for index, value in enumerate([20, 60, 100, 140, 180, 220])]))
print("Answer 2:")
print("\n".join(crt_cycles))