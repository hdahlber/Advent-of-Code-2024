def read_in_file(filename):
    with open(filename, "r") as file:
        line = file.read().strip()
        results = []
        id_num = 0
        is_value = True
        for char in line:
            number = int(char)
            if is_value:
                results += [id_num] * number
                id_num += 1
                is_value = False
            else:
                results += [False] * number
                is_value = True

        #print(results)
        return results


def part_1(start_list):
    summer = 0
    ans = []
    index = 0
    back_index = len(start_list) - 1
    #print(back_index)
    for i in start_list:
        #print(i)
        index += 1
        if i is not False and index <= back_index + 1:
            ans.append(i)
            #print("ans append",i)
        if i is False:
            for j in range(back_index, index - 1, -1):
                if start_list[j] is not False:

                    #print("ans append", start_list[j])
                    back_index -= 1
                    ans.append(start_list[j])

                    break
                else:
                    back_index -= 1

    for index in range(len(ans)):
        summer += ans[index] * index
    return summer


def part_2(filename):
    with open(filename, "r") as file:
        line = file.read().strip()
        results = []
        id_num = 0
        is_value = True
        for char in line:
            number = int(char)
            if is_value:

                results.append([id_num] * number)
                id_num += 1
                is_value = False
            else:
                results.append([None] * number)
                is_value = True

        back_index = len(results)
        for i in reversed(results):  # starta bakifrån
            back_index -= 1
            if None not in i:  # om ett värde utan None
                for j in results[:back_index]:  # börja från starten
                    if None in j:  # om en lista med none
                        if j.count(None) >= len(i):  # om listan har utrymme för alla
                            #print(j.count(None), i)
                            counter = len(i)
                            for index in range(len(j)):  # för varje värde j listan
                                if j[index] is None and counter != 0:  # om värdet är Non
                                    j[index] = i[counter - 1]  # ge värdet av index i andra listan

                                    counter -= 1
                            for index in range(len(i)):
                                i[index] = None

                            break

        total_sum = 0
        global_index = 0

        for sublist in results:
            if not sublist:
                continue

            for value in sublist:
                if value is None:
                    value = 0
                total_sum += value * global_index
                global_index += 1

        #print(f"Total Sum: {total_sum}")

        return total_sum


def main():
    start_list =read_in_file("input.txt")
    result = part_1(start_list)
    print(f"Part 1 results: {result}")
    result = part_2("input.txt")
    print(f"Part 2 results: {result}")


if __name__ == "__main__":
    main()
