def read_in_file(filename):
    with open(filename, "r") as file:
        lines = file.read().strip().split("\n")
    return [int(line) for line in lines]


def part_1(lines,times):
    def mix(a,b):
        return a ^ b
    def prune(a):
        return a % 16777216
    def steps(a):
        b = a * 64
        a = prune(mix(a,b))
        b = a // 32
        a = prune(mix(a,b))
        b = a * 2048
        a = prune(mix(a,b))
        return a


    summer = 0
    for line in lines:
        x = line
        for y in range(times):
            x = steps(x)
        summer += x
    return summer

def main():
    lines = read_in_file("input.txt")
    times = 2000
    result = part_1(lines,times)
    print(f"Part 1 results: {result}")


if __name__ == "__main__":
    main()