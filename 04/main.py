import unittest

HORIZONTAL = "_"
VERTICAL = "|"
ASCENDING_DIAGONAL = "/"
DESCENDING_DIAGONAL = "\\"

class WordSearch:
    def __init__(self, word_search_string):
        self._word_search_array = word_search_string.split("\n")
        self._n_rows = len(self._word_search_array)

        self._n_columns = len(self._word_search_array[0])
        for row in self._word_search_array:
            if len(row) != self._n_columns:
                raise Exception("Column length varies")
            
        self._n_characters = self._n_rows * self._n_columns
            
    def _index_to_coordinates(self, index):
        column = index % self._n_columns
        row = index // self._n_columns
        return (row, column)
    
    def _lookup(self,x,y):
        if x < 0 or y < 0:
            return False
        try:
            return self._word_search_array[x][y]
        except:
            return False
        
    def _check_for_word_in_direction(self, index, word, reverse, direction_string):
        start_x, start_y = self._index_to_coordinates(index)
        
        if reverse:
            direction = -1
        else:
            direction = 1
        
        resulting_word = []
        for i in range(len(word)):
            if direction_string == HORIZONTAL:
                lookup = self._lookup(start_x, start_y+i*direction)
            elif direction_string == VERTICAL:
                lookup = self._lookup(start_x+i*direction, start_y)
            elif direction_string == ASCENDING_DIAGONAL:
                lookup = self._lookup(start_x+i*direction, start_y+i*direction)
            elif direction_string == DESCENDING_DIAGONAL:
                lookup = self._lookup(start_x+i*direction*-1, start_y+i*direction)

            if lookup == False:
                return False
            else:
                resulting_word.append(lookup)

        temp = ''.join(resulting_word)
        return  temp == word
    
    def amount_of_times_word_occurs(self, word):
        direction_strings = [HORIZONTAL, VERTICAL, ASCENDING_DIAGONAL, DESCENDING_DIAGONAL]
        sum = 0
        for i in range(self._n_characters):
            for direction in direction_strings:
                for reverse in [True, False]:
                    word_occurs = self._check_for_word_in_direction(i, word, reverse, direction)
                    if word_occurs:
                        sum += 1
        
        return sum
    
    def amount_of_times_x_mas_occurs(self): #i.e. part 2
        sum = 0

        for i in range(self._n_characters):
            down_cross_sam = self._check_for_word_in_direction(i, "SAM", False, DESCENDING_DIAGONAL)
            down_cross_mas = self._check_for_word_in_direction(i, "MAS", False, DESCENDING_DIAGONAL)

            up_cross_sam = self._check_for_word_in_direction(i+2, "SAM", True, ASCENDING_DIAGONAL)
            up_cross_mas = self._check_for_word_in_direction(i+2, "MAS", True, ASCENDING_DIAGONAL)

            if (down_cross_sam or down_cross_mas) and (up_cross_mas or up_cross_sam):
                sum += 1
        
        return sum
    

WORD = "XMAS"
class TestWordSearch(unittest.TestCase):
    
    def test_horizontal(self):
        input = "XMAS"
        ws = WordSearch(input)
        self.assertEqual(ws.amount_of_times_word_occurs(WORD), 1)



def parse_input(file_name) -> WordSearch:
    with open(file_name, 'r') as file:
        content = file.read()
    return WordSearch(content)

file_names = ['test_input', 'input']

#unittest.main()

for file_name in file_names:
    print('File name: ',file_name)
    word_search = parse_input(file_name)
    
    part_1_solution = word_search.amount_of_times_word_occurs("XMAS")
    print('Part 1 solution: ', part_1_solution) #Test:18, actual:2575 (correct)

    part_2_solution = word_search.amount_of_times_x_mas_occurs()#Test:9, actual: 2041 (correct)
    print('Part 2 solution: ', part_2_solution)