

def read_in_file(filename):
    with open(filename, "r") as file:
        line = file.read().strip()
        results = []
        id = 0
        is_value = True
        for char in line:
            number = int(char)
            if is_value:
                results += [id] * number
                id += 1
                is_value = False
            else:
                results += [False]* number
                is_value = True

        print(results)
        return results

def part_1(start_list):
    summer = 0
    ans = []
    index = 0
    back_index = len(start_list)-1
    #print(back_index)
    for i in start_list:
        #print(i)
        index += 1
        if i is not False and index <= back_index+1:
            ans.append(i)
            #print("ans append",i)
        if i is False:
            for j in range(back_index,index-1,-1):
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

def main():
   start_list =read_in_file("test.txt")
   result = part_1(start_list)
   print(f"Part 1 results: {result}")



if __name__ == "__main__":
    main()