A, B, C = 0, 0, 0
x = 0
part1_list = []
def read_in_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    program = []
    global A,B,C
    for line in lines:
        line = line.strip()
        if line.startswith("Register A"):
            A = int(line.split(":")[1].strip())
        elif line.startswith("Register B"):
            B = int(line.split(":")[1].strip())
        elif line.startswith("Register C"):
            C = int(line.split(":")[1].strip())
        elif line.startswith("Program:"):
            program = [int(x.strip()) for x in line.split(":")[1].split(",")]


    return program

def adv(operation_num,literal):
    global A
    A = A // (2**operation_num)

def bxl(operation_num,literal):
    global B
    B = B ^ literal

def bst(operation_num,literal):
    global B
    B = operation_num % 8

def jnz(operation_num,literal):
    global A,x
    if A != 0:
        x = literal
    else:
        x += 2


def bxc(operation_num,literal):
    global B,C
    B = B ^ C

def out(operation_num,literal):
    global part1_list
    part1_list.append(operation_num % 8)

def bdv(operation_num,literal):
    global A,B
    B = A // (2 ** operation_num)

def cdv(operation_num,literal):
    global A, C
    C = A // (2 ** operation_num)



function_list = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
def get_operand_value(operand):
    if operand <= 3:
        return operand
    elif operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C

def part_1(program):
    global A, B, C, x
    while 0 <= x < len(program):
        opcode = program[x]
        literal = program[x + 1]
        operand_value = get_operand_value(literal)
        function_list[opcode](operand_value, literal)
        print(opcode,literal,x)
        if opcode != 3:
            x += 2
    result = ','.join(map(str, part1_list))
    return result

def main():
    program = read_in_file("input.txt")
    result = part_1(program)
    print("part 1",result)







if __name__ == "__main__":
    main()