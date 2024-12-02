from typing import List



        
class Level:
    def __init__(self, level_string):
        self._value = int(level_string)
    
    def value(self):
        return self._value
class Report:
    def __init__(self, report_string:str):
        self._levels: List[Level] = []
        level_strings = report_string.split(" ")
        for level_string in level_strings:
            self._levels.append(Level(level_string))

    def _adjacent_differences(self):
        differences = []
        for i, level in enumerate(self._levels):
            if i == len(self._levels)-1:
                break
            current_value = level.value()
            following_value = self._levels[i+1].value()
            differences.append(abs(current_value - following_value))
        
        return differences
            

    def is_safe(self):
        levels_list = [level.value() for level in self._levels]
        all_increasing = sorted(levels_list) == levels_list
        all_decreasing = sorted(levels_list, reverse=True) == levels_list

        adjacent_difference_at_least_one_and_at_most_three =  True if all(1 <= diff <= 3 for diff in self._adjacent_differences()) else None

        return (all_increasing or all_decreasing) and adjacent_difference_at_least_one_and_at_most_three

def parse_input(file_name) -> List[Report]:
    with open(file_name, 'r') as file:
        content = file.read()
    report_strings = content.split("\n")

    reports = []
    for report_string in report_strings:
        reports.append(Report(report_string))
    return reports

file_names = ['test_input', 'input']

for file_name in file_names:
    print('File name: ',file_name)
    reports = parse_input(file_name)

    amount_of_safe_reports = 0

    for report in reports:
        if report.is_safe():
            amount_of_safe_reports +=  1
            
            
    part_1_solution = amount_of_safe_reports
    print('Part 1 solution: ', part_1_solution) #Test: 2, Actual: 242

    part_2_solution = 69
    print('Part 2 solution: ', part_2_solution) #