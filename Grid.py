import Cell


class Grid:
    def __init__(self, width, height):
        self.matrix = [[Cell.Cell(y, x) for x in range(height)] for y in range(width)]

    def get_width(self):
        return len(self.matrix[0])

    def get_height(self):
        return len(self.matrix)

    def get_north(self, pos):
        if pos[1]-1 < 0:  # out of range // len(matrix) = height; len(matrix[0]) = width
            return None
        return self.matrix[pos[0]][pos[1]-1]

    def get_south(self, pos):
        if pos[1]+1 >= len(self.matrix[0]):  # out of range // len(matrix) = height; len(matrix[0]) = width
            return None
        return self.matrix[pos[0]][pos[1]+1]

    def get_west(self, pos):
        if pos[0]-1 < 0:  # out of range // len(matrix) = height; len(matrix[0]) = width
            return None
        return self.matrix[pos[0]-1][pos[1]]

    def get_east(self, pos):
        if pos[0]+1 >= len(self.matrix):  # out of range // len(matrix) = height; len(matrix[0]) = width
            return None
        return self.matrix[pos[0]+1][pos[1]]

    def get_adjacent_cells(self, current_cell):
        neighs = ([self.get_north(current_cell.pos), self.get_south(current_cell.pos),
                  self.get_west(current_cell.pos), self.get_east(current_cell.pos)])
        return [x for x in neighs if x is not None]

    def __str__(self):
        s = ''
        for x in range(len(self.matrix[0])):
            if x == 0:
               s += '+' + '   '
            else: 
                s += '+' + "---"
        s += '+\n'
        for row in self.matrix:
            s += '|'
            for elem in row:
                s += str(elem)
                if not elem.neighbours.east:
                    s += '|'
                else:
                    s += ' '
            s += '\n'
            for elem in row:
                s += '+'
                if ((not elem.neighbours.south) & (elem.pos != ( len(self.matrix)-1,len(self.matrix[0])-1 ) ) ):
                    s += '---'
                else:
                    s += '   '
            s += '+\n'
        return s

    def get_grid(self, text):
        width = text[0].count('+')-1
        height = int((len(text)-1)/2)
        self.matrix = [[Cell.Cell(y, x) for x in range(width)] for y in range(height)]
        cx,cy = 0,0
        south = 1
        east = 2

        for y in range(1,len(text),2): #2steps
            for x in range(2,len(text[0]),4): #4 steps al siguiente
                if ((text[y+south][x] == ' ') & ( cy+1 < height)):
                    self.matrix[cy][cx].connect(self.matrix[cy+1][cx])

                if ((text[y][x+east] == ' ') & ( cx+1 < width)):
                    self.matrix[cy][cx].connect(self.matrix[cy][cx+1])
                cx += 1
            cy += 1
            cx = 0
        return
        #text[1][2] celda inicial, revisar todas direcciones