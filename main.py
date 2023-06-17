class Cube:
    def __init__(self, code_text):
        self.matrix = self.cube_builder(code_text)

    def cube_builder(self, code_text):
        code_text = code_text.replace(" ", "0")
        if len(code_text) % 8 == 0:
            row = len(code_text) // 8
        else:
            row = len(code_text) // 8 + 1
        cube_matrix = [['0'] * 8 for _ in range(row)]  
        for i, char in enumerate(code_text):
            cube_matrix[i // 8][i % 8] = char.lower() 
        return cube_matrix

    def rotate(self, indices, row_indices):
        new_matrix = [row.copy() for row in self.matrix]
        for row_index in row_indices:
            for j, index in enumerate(indices):
                new_matrix[row_index][j] = self.matrix[row_index][index]
        self.matrix = new_matrix

    def right(self, row_index=None):
        if row_index is not None:
            indices = [4, 0, 3, 7, 5, 1, 2, 6]
            self.rotate(indices, [row_index])
        else:
            indices = [4, 0, 3, 7, 5, 1, 2, 6]
            self.rotate(indices, range(len(self.matrix)))

    def left(self, row_index=None):
        if row_index is not None:
            indices = [1, 5, 6, 2, 0, 4, 7, 3]
            self.rotate(indices, [row_index])
        else:
            indices = [1, 5, 6, 2, 0, 4, 7, 3]
            self.rotate(indices, range(len(self.matrix)))

    def up(self, row_index=None):
        if row_index is not None:
            indices = [3, 2, 6, 7, 0, 1, 5, 4]
            self.rotate(indices, [row_index])
        else:
            indices = [3, 2, 6, 7, 0, 1, 5, 4]
            self.rotate(indices, range(len(self.matrix)))

    def down(self, row_index=None):
        if row_index is not None:
            indices = [4, 5, 1, 0, 7, 6, 2, 3]
            self.rotate(indices, [row_index])
        else:
            indices = [4, 5, 1, 0, 7, 6, 2, 3]
            self.rotate(indices, range(len(self.matrix)))

    def print_matrix(self):
        for row in self.matrix:
            print(row)

class FixCode:
    def __init__(self):
        self.result = ''
        self.valid_words = []
        self.max_wrd_count = 0

    def word_getter(self):
        self.result = ""
        for row in cube.matrix:
            for char in row:
                if char == "0":
                    self.result += " "
                else:
                    self.result += char
        self.result = self.result.strip()


    def check_word_in_file(self, word):
        with open('words_alpha.txt', 'r') as file:
            return word.lower() in file.read().split()
 
    def fix(self):
        cases = [
            (0, 0),
            (4, 4), 
            (1, 4),  
            (2, 4), 
            (3, 4), 
        ]

        for left, up in cases:
            for _ in range(left):
                cube.left()
            for _ in range(up):
                cube.up()
                self.word_getter()
                words = self.result.split()
                for word in words:
                    if self.check_word_in_file(word) and word not in self.valid_words:
                        self.valid_words.append(word)
        my_list = self.result.split()
        self.max_wrd_count = len(my_list) - 1
        self.valid_words.sort(key=len, reverse=True)
        for word in self.valid_words[:self.max_wrd_count]:
            print(word, end=' ')




code_text = "Hello example world" 
cube = Cube(code_text)

#Rotate
for _ in range(3):
    cube.right()
cube.left()
cube.right()
cube.left()
cube.left()
cube.right()
cube.up()

#Fixing 
c = FixCode()
c.fix()