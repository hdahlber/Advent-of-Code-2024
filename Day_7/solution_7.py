from itertools import product


def part_12(filename, possible):
    with open(filename, "r") as file:
        summer = 0
        lines = file.read().splitlines()
        for line in lines:
            ans, rest = line.split(":")
            ans = int(ans)
            values = list(map(int, rest.split()))
            #print(values)

            def check_if_ok(ops):
                number = int(values[0])
                for i in range(1, len(values)):

                    if ops[i - 1] == "+":
                        number += values[i]
                    elif ops[i - 1] == "*":
                        number *= values[i]
                    else:
                        number = int(f"{number}{values[i]}")

                return number

            for ops in product(possible, repeat=len(values) - 1):
                if check_if_ok(ops) == ans:
                   #print(summer)
                    summer += ans
                    break

    return summer


def main():
    result = part_12("input.txt", (["+", "*"]))
    print(f"Part 1 results: {result}")
    result2 = part_12("input.txt", (["+", "||", "*"]))
    print(f"Part 2 results: {result2}")


if __name__ == "__main__":
    main()
