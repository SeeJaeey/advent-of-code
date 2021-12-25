import numpy as np
from time import perf_counter

input = """inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 15
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 9
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -7
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 14
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -7
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -8
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -7
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -5
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y"""

example = """"""

def parse_input(input_str):
    instructions = input_str.splitlines()
    digit_instructions = []
    current_instr = [instructions[0]]
    for i in range(1, len(instructions)):
        if 'inp' in instructions[i]:
            digit_instructions.append(current_instr.copy())
            current_instr.clear()
        current_instr.append(instructions[i])
    digit_instructions.append(current_instr.copy())
    return digit_instructions

def isint(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def valid_model_number(instructions, digit, variables):
    for instr in instructions:

        split = instr.split(" ")
        left = split[1]
        if not 'inp' in instr:
            right = split[2]

        if 'add' in instr:
            if isint(right):
                variables[left] += int(right)
            else:
                variables[left] += variables[right]

        elif 'mul' in instr:
            if isint(right):
                variables[left] *= int(right)
            else:
                variables[left] *= variables[right]

        elif 'mod' in instr:
            if variables[left] < 0 or (isint(right) and int(right) <= 0) or (not isint(right) and variables[right] <= 0):
                print(f"Modulo operation not possible with a = {left} and b = {right}")
            elif isint(right):
                variables[left] %= int(right)
            else:
                variables[left] %= variables[right]

        elif 'div' in instr:
            if (isint(right) and int(right) == 0) or (not isint(right) and variables[right] == 0):
                print("Division by zero is undefined..")
            elif isint(right):
                variables[left] //= int(right)
            else:
                variables[left] //= variables[right]

        elif 'eql' in instr:
            if isint(right):
                if variables[left] == int(right):
                    variables[left] = 1
                else:
                    variables[left] = 0
            else:
                if variables[left] == variables[right]:
                    variables[left] = 1
                else:
                    variables[left] = 0
        else:
            variables[left] = digit

    return variables

# More a reverse engineering task than a programming task..
def task1(input_str):
    instructions_per_digit = parse_input(input_str)
    result = '11911316711816'
    min_model_num3 = '11917919939999'
    min_model_num2 = '99917919934891'
    test = '19927819934849'
    min_model_num = '99999999934895'
    model_number = '99999999999999'
    start_model_number = result
    assert(len(start_model_number) == 14)
    min = (100000000000, '99999999999999')
    while(True):
        variables = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
        print(f"Model number: {start_model_number}")
        print(f"Minimum so far: {min}")
        for digit_count in range(len(instructions_per_digit)):
            variables = valid_model_number(instructions_per_digit[digit_count], int(start_model_number[digit_count]), variables)
        print(f"Z: {variables['z']}")
        if variables['z'] <= 8 or int(start_model_number) < 11111111111111:
            break
        else:
            if variables['z'] < min[0]:
                min = (variables['z'], start_model_number)
            start_model_number = str(int(start_model_number) - 10)
            while '0' in start_model_number:
                start_model_number = str(int(start_model_number) - 10)

    return start_model_number

def task2(input_str):
    return


start = perf_counter()
result1 = task1(input)
stop = perf_counter()
elapsed1 = stop - start
start = perf_counter()
result2 = task2(example)
stop = perf_counter()
elapsed2 = stop - start

print(f"Task 1: {result1}")
print(f"Execution time: {elapsed1}s")
print("")
print(f"Task 2: {result2}")
print(f"Execution time: {elapsed2}s")