import re
from  typing import List, Pattern, Tuple

class Multiplication:
    def __init__(self, multiplication_string:str):

        self._left_factor = int(multiplication_string.split("(")[1].split(",")[0])
        self._right_factor = int(multiplication_string.split("(")[1].split(",")[1].split(")")[0])

    def product(self):
        return self._left_factor * self._right_factor

class Do:
    def __init__(self, do_string):
        if do_string != "do()":
            raise Exception("knas bror")
        
class Dont:
    def __init__(self, do_string):
        if do_string != "don't()":
            raise Exception("knas bror")
        
def match_and_find_positions(text, pattern:Pattern[str], constructor):
    matches = []
    for match in pattern.finditer(text):
        start, _ = match.span()
        matches.append((constructor(match.group()), start))

    return matches

def parse_input(file_name) -> List[Multiplication]:
    with open(file_name, 'r') as file:
        content = file.read()
    
    pattern_constructor_pairs:List[Tuple[Pattern[str],  object]] = [
        (re.compile(r"mul\(\d+,\d+\)"), Multiplication),
        (re.compile(r"do\(\)"), Do),
        (re.compile(r"don't\(\)"), Dont)
    ]
    all_matches = []
    for pattern, constructor in pattern_constructor_pairs:

        matches = match_and_find_positions(content, pattern, constructor)
        all_matches += matches
    
    
    return sorted(all_matches, key=lambda x: x[1])

def evaluate_memory(commands, conditionals_allowed):
    dont_previously = False

    if not conditionals_allowed:
        commands = [command for command in commands if isinstance(command[0], Multiplication)]
    sum = 0
    for command in commands:
        command_type = command[0]
        if isinstance(command_type, Multiplication) and not dont_previously:
            sum += command[0].product()
        elif isinstance(command_type, Do) and dont_previously:
            dont_previously = False
        elif isinstance(command_type, Dont) and not dont_previously:
            dont_previously = True
    
    return sum


file_names = ['test_input', 'input']

for file_name in file_names:
    print('File name: ',file_name)
    
    matches: List[Multiplication] = parse_input(file_name)
    
    print('Part 1 solution: ', evaluate_memory(matches, conditionals_allowed=False)) #Test: 161, actual: 161085926 (correct)

    print('Part 2 solution: ', evaluate_memory(matches, conditionals_allowed=True))  #Test: 48, actual: 82045421 (correct)