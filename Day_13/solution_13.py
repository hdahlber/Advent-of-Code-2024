
def read_in_file(filename):
    machines = []
    with open(filename, "r") as file:
        lines = file.readlines()
    current_machine = {"buttons": [], "prize": None}
    for line in lines:
        line = line.strip()
        if line.startswith("Button A:"):
            parts = line.split(", ")
            dx, dy = int(parts[0].split("+")[1]), int(parts[1].split("+")[1])
            current_machine["buttons"].append((dx, dy, 3))
        elif line.startswith("Button B:"):
            parts = line.split(", ")
            dx, dy = int(parts[0].split("+")[1]), int(parts[1].split("+")[1])
            current_machine["buttons"].append((dx, dy, 1))
        elif line.startswith("Prize:"):
            parts = line.split(", ")
            px, py = int(parts[0].split("=")[1]), int(parts[1].split("=")[1])
            current_machine["prize"] = (px, py)
            machines.append(current_machine)
            current_machine = {"buttons": [], "prize": None}


    print(machines)
    return machines

def min_max_machine(buttons, prize):
    dx1, dy1, cost1 = buttons[0]
    dx2, dy2, cost2 = buttons[1]
    px, py = prize
    min_tokens = 1000000000

    found_solution = False
    for a_presses in range(1,101):
        for b_presses in range(1,101):
            x = a_presses * dx1 + b_presses * dx2
            y = a_presses * dy1 + b_presses * dy2
            if x == px and y == py:
                found_solution = True
                tokens = a_presses * cost1 + b_presses * cost2
                min_tokens = min(min_tokens, tokens)
    return min_tokens if found_solution else 0

def linear_programming(buttons,prize):
    ax, ay, cost1 = buttons[0] # a button
    bx, by, cost2 = buttons[1] # b button
    extra = 10000000000000
    px, py = prize
    px = px + extra
    py = py + extra
    i = (px * by - bx * py)//(by * ax - bx * ay)
    j = (py - ay * i) // by
    if i < 0 or j < 0:
        return 0
    elif ax * i + bx * j == px and ay * i + by * j == py:
        return cost1 * int(i) + int(j) * cost2
    else:
        return 0


def part_1(machines):

    total_tokens = 0
    total_tokens2 = 0
    for machine in machines:
        result = min_max_machine(machine['buttons'], machine['prize'])
        result2 = linear_programming(machine['buttons'], machine['prize'])
        total_tokens += result
        total_tokens2 += result2

    return total_tokens, total_tokens2




def main():
    machines = read_in_file("input.txt")
    result , result2 = part_1(machines)
    print(f"Part 1 results: {result}")
    print(f"Part 2 results: {result2}")


if __name__ == "__main__":
    main()