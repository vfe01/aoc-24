INPUT_NAME = "input_test"
class ParseException:Exception

def parse_input(file_name):
    with open(file_name, 'r') as file:
        input = file.read()
        split_input = input.split()

        left_list = []
        right_list = [] 

        for i, number_string in enumerate(split_input):
            number = int(number_string)
            if i%2 == 0:
                left_list.append(number)
            else:
                right_list.append(number)
        
        if len(left_list) != len(right_list):
            raise Exception("The columns are of different length")
        
        list_length = len(left_list)

        return  left_list, right_list, list_length

input_file_names = ["input", "input_test"]


for file_name in input_file_names:
    print("Input file name: ", file_name)
    left_list, right_list, list_length = parse_input(file_name)

    left_list.sort()
    right_list.sort()

    part_one_sum = 0
    for i in range(list_length):
        part_one_sum += abs(left_list[i] - right_list[i])

    print(f"Part one answer: {part_one_sum}")


    #Part 2
    number_occurances = {}

    for number in right_list:
        number_string = str(number)
        if number_string in number_occurances:
            number_occurances[number_string] += 1
        else:
            number_occurances[number_string] = 1
    
    part_two_sum = 0
    for number in left_list:
        number_string = str(number)
        if number_string in number_occurances:
            occurances_in_right_list = number_occurances[str(number)]
        else:
            occurances_in_right_list = 0
        part_two_sum += number * occurances_in_right_list
    
    print(f"Part two answer: {part_two_sum}")
    print("\n")
