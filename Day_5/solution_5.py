import functools
from collections import defaultdict

def read_in_file(filename):
    with open(filename, "r") as file:
        data = file.read()

    start_rules, start_updates = data.split("\n\n")

    rules = defaultdict(set)
    updates = []


    for line in start_rules.splitlines():
        before, after = line.split("|")
        rules[int(after)].add(int(before))


    for line in start_updates.splitlines():
        update = [int(d) for d in line.split(",")]
        updates.append(update)

    return rules, updates





def part12(rules, updates):
    summer = 0
    summer2 = 0

    def mycmp(a, b):
        #print(a,b)
        if b in rules[a]:
            return 1
        elif a in rules[b]:
            return -1
        else:
            return 0


    for update in updates:

        is_valid = True

        for i in range(len(update)):
            x = update[i]
            if x in rules:
                for y in rules[x]:

                    if y in update:
                        x_position = update.index(x)
                        y_position = update.index(y)

                        if x_position <= y_position:
                            is_valid = False
                            break

        if is_valid:
            summer += update[len(update)//2]

        #part 2
        else:
            arranged = sorted(update, key=functools.cmp_to_key(mycmp))
            #print(arranged)
            middle = int((len(arranged) - 1) / 2)
            summer2 += arranged[middle]

    return summer, summer2


def main():
    rules, updates = read_in_file("input.txt")
    #print(rules)
    #print(updates)

    result1, result2 = part12(rules, updates)
    print(f"Part 1 results: {result1}")
    print(f"Part 2 results: {result2}")



if __name__ == "__main__":
    main()
