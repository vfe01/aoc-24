class WordSearch:
    def __init__(self, word_search_string):
        self._word_search_array = word_search_string.split("\n")
        self._n_rows = len(self._word_search_array)

        self._n_columns = len(self._word_search_array[0])
        for row in self._word_search_array:
            if len(row) != self._n_columns:
                raise Exception("Column length varies")
            
        self._n_characters = self._n_rows * self._n_columns
            
    def _index_to_coordinates(self):
        column = self._index % self._n_columns
        row = self._index // self._n_columns
        return (row, column)
    
    def __iter__(self):
        self._index = -1
        return self
    
    def __next__(self):
        self._index += 1

        if self._index == self._n_characters:
            raise StopIteration

        row, column = self._index_to_coordinates()
        return self._word_search_array[row][column]
    
        
    


def parse_input(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return WordSearch(content)

file_names = ["test"]#['test_input', 'input']


for file_name in file_names:
    print('File name: ',file_name)
    word_search = parse_input(file_name)
    for c in word_search:
        print(c)
    exit()
    part_1_solution = 42
    print('Part 1 solution: ', part_1_solution)

    part_2_solution = 69
    print('Part 2 solution: ', part_2_solution)