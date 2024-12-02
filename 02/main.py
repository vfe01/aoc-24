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
    def __str__(self):
        return str(self._levels_list())

    def _adjacent_differences(self):
        differences = []
        for i, level in enumerate(self._levels):
            if i == len(self._levels)-1:
                break
            current_value = level.value()
            following_value = self._levels[i+1].value()
            differences.append(abs(current_value - following_value))
        
        return differences
            
    def _levels_list(self):
        return [level.value() for level in self._levels]

    def _is_ascending_and_contains_allowed_differences_using_problem_dampener(self, descending=False, remove_element=None):
        levels_list =  self._levels_list()
        if remove_element != None:
            levels_list.pop(remove_element)

        for i in range(len(levels_list)):
            if i == len(levels_list)-1:
                return True
            
            current_value = levels_list[i]
            next_value = levels_list[i+1]
            if descending:
                has_incorrect_order = current_value <= next_value
            else:
                has_incorrect_order = current_value >= next_value

            difference = abs(current_value - next_value)
            difference_at_least_one = difference >= 1
            difference_at_most_three = difference <= 3
            allowed_difference = difference_at_least_one and difference_at_most_three

            if  has_incorrect_order or not allowed_difference:
                if remove_element != None:
                    return False
                else:
                    return self._is_ascending_and_contains_allowed_differences_using_problem_dampener(descending=descending, remove_element=i) or self._is_ascending_and_contains_allowed_differences_using_problem_dampener(descending=descending, remove_element=i+1)
        
        return True
        

    def is_safe(self):
        levels_list = self._levels_list()
        all_increasing = sorted(levels_list) == levels_list
        all_decreasing = sorted(levels_list, reverse=True) == levels_list

        adjacent_difference_at_least_one_and_at_most_three =  True if all(1 <= diff <= 3 for diff in self._adjacent_differences()) else None

        return (all_increasing or all_decreasing) and adjacent_difference_at_least_one_and_at_most_three

    def is_safe_using_problem_dampener(self):
        descending = self._is_ascending_and_contains_allowed_differences_using_problem_dampener(descending=True)
        ascending = self._is_ascending_and_contains_allowed_differences_using_problem_dampener(descending=False)
        return descending or ascending
def parse_input(file_name) -> List[Report]:
    with open(file_name, 'r') as file:
        content = file.read()
    report_strings = content.split("\n")

    reports = []
    for report_string in report_strings:
        reports.append(Report(report_string))
    return reports

file_names = ['input'] #'test_input', 

for file_name in file_names:
    print('File name: ',file_name)
    reports = parse_input(file_name)

    amount_of_safe_reports = 0

    part_1_safe_reports = []
    for report in reports:
        if report.is_safe():
            amount_of_safe_reports +=  1
            part_1_safe_reports.append(True)
        else:
            part_1_safe_reports.append(False)
            
    part_1_solution = amount_of_safe_reports
    print('Part 1 solution: ', part_1_solution) #Test: 2, Actual first attempt: 242 (correct)

    amount_of_safe_reports_problem_dampener = 0
    part_2_safe_reports = []

    for report in reports:
        if report.is_safe_using_problem_dampener():
            amount_of_safe_reports_problem_dampener +=  1
            part_2_safe_reports.append(True)
        else:
            part_2_safe_reports.append(False)

    part_2_solution = amount_of_safe_reports_problem_dampener
    print('Part 2 solution: ', part_2_solution) #Test: 4, Actual first attempt: 288 (too low), second attempt: 311 (correct)
