class Cat:
    def __init__(self):
        self.symbols = ['_'] * 9
        self.state = []
        self.impossible = False
        self.coord = []
        self.coord_board = []
        self.keep_game = True
        self.coord_numbers = [[6, 3, 0],
                              [7, 4, 1],
                              [8, 5, 2]]

    def input_symbols(self):
        self.coord_board = [[self.symbols[6], self.symbols[3], self.symbols[0]],
                            [self.symbols[7], self.symbols[4], self.symbols[1]],
                            [self.symbols[8], self.symbols[5], self.symbols[2]]]

    def show_game(self):
        print(f'''
        ---------
        | {self.symbols[0]} {self.symbols[1]} {self.symbols[2]} |
        | {self.symbols[3]} {self.symbols[4]} {self.symbols[5]} |
        | {self.symbols[6]} {self.symbols[7]} {self.symbols[8]} |
        ---------
        ''')

    def analyze(self):
        gato_sign = ['O', 'X']
        if self.symbols[0] == self.symbols[1] == self.symbols[2] and self.symbols[1] in gato_sign:
            self.state.append(f'{self.symbols[1]} wins')
        if self.symbols[3] == self.symbols[4] == self.symbols[5] and self.symbols[4] in gato_sign:
            self.state.append(f'{self.symbols[4]} wins')
        if self.symbols[6] == self.symbols[7] == self.symbols[8] and self.symbols[7] in gato_sign:
            self.state.append(f'{self.symbols[7]} wins')
        if self.symbols[0] == self.symbols[3] == self.symbols[6] and self.symbols[3] in gato_sign:
            self.state.append(f'{self.symbols[3]} wins')
        if self.symbols[1] == self.symbols[4] == self.symbols[7] and self.symbols[4] in gato_sign:
            self.state.append(f'{self.symbols[4]} wins')
        if self.symbols[2] == self.symbols[5] == self.symbols[8] and self.symbols[5] in gato_sign:
            self.state.append(f'{self.symbols[5]} wins')
        if self.symbols[0] == self.symbols[4] == self.symbols[8] and self.symbols[4] in gato_sign:
            self.state.append(f'{self.symbols[4]} wins')
        if self.symbols[2] == self.symbols[4] == self.symbols[6] and self.symbols[4] in gato_sign:
            self.state.append(f'{self.symbols[4]} wins')

        if self.symbols.count('X') > self.symbols.count('O') + 1 \
                or self.symbols.count('O') > self.symbols.count('X') + 1:
            self.impossible = True

    def result(self):
        if len(self.state) == 1:
            print(self.state[0])
            self.keep_game = False
        elif len(self.state) == 0:
            if "_" in self.symbols:
                print('Game not finished')
            else:
                print('Draw')
                self.keep_game = False

    def input_coordinates(self, symbol):
        values = [1, 2, 3]
        while True:
            self.coord = input('Enter the coordinates: ').split()
            if self.coord[0].isdigit() and self.coord[1].isdigit():
                if int(self.coord[0]) in values and int(self.coord[1]) in values:
                    column = int(self.coord[0]) - 1
                    row = int(self.coord[1]) - 1
                    ind = self.coord_numbers[column][row]
                    if self.symbols[ind] == '_':
                        self.symbols[ind] = symbol
                        self.show_game()
                        break
                    else:
                        print('This cell is occupied! Choose another one!')
                        continue
                elif 0 < int(self.coord[0]) > 4 or 0 < int(self.coord[1]) > 4:
                    print('Coordinates should be from 1 to 3!')
                    continue
            else:
                print('You should enter numbers!')
                continue

    def play(self):
        self.input_symbols()
        self.show_game()
        symbol = 'O'
        while self.keep_game:
            if symbol == 'O':
                symbol = 'X'
            else:
                symbol = 'O'
            self.input_coordinates(symbol)
            self.analyze()
            self.result()


cat = Cat()
cat.play()
