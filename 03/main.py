import re
from  typing import List

class Multiplication:
    def __init__(self, multiplication_string:str):

        self._left_factor = int(multiplication_string.split("(")[1].split(",")[0])
        self._right_factor = int(multiplication_string.split("(")[1].split(",")[1].split(")")[0])

    def product(self):
        return self._left_factor * self._right_factor

def parse_input(file_name) -> List[Multiplication]:
    with open(file_name, 'r') as file:
        content = file.read()
    mul_pattern = re.compile(r"mul\(\d+,\d+\)")
    matches = mul_pattern.findall(content)
    multiplications = []
    for match in matches:
        multiplications.append(Multiplication(match))

    return multiplications
file_names = ['test_input', 'input']

for file_name in file_names:
    print('File name: ',file_name)
    
    multiplications: List[Multiplication] = parse_input(file_name)

    sum = 0
    for multi in multiplications:
        sum += multi.product()
    part_1_solution = sum
    print('Part 1 solution: ', part_1_solution) #Test: 161, actual: 161085926 (correct)

    part_2_solution = 69
    print('Part 2 solution: ', part_2_solution) 