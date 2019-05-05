
class Neighbours(object):
    def __init__(self):
        self.north = None
        self.south = None
        self.west = None
        self.east = None

    def get_neighbours(self):
        return [self.north, self.south, self.east, self.west]

    def get_not_null_neighbours(self):
        n = [self.north, self.south, self.east, self.west]
        n = [x for x in n if x is not None]
        return n


class Cell:
    def __init__(self, x=-1, y=-1):
        self.pos = (x, y)
        self.neighbours = Neighbours()
        self.visit = False
        self._fill = False

    def build(self):
        self.visit = True

    def not_built(self):
        return self.visit

    def fill_pos(self):
        self._fill = str(self.pos[1]) + "," + str(self.pos[0])

    def fill(self):
        self._fill = " * "

    def connect(self, con):
        if (con.pos[0] == self.pos[0] + 1 and
                con.pos[1] == self.pos[1]):
            self.neighbours.south = con
            con.neighbours.north = self

        elif (con.pos[0] == self.pos[0] - 1 and
              con.pos[1] == self.pos[1]):
            self.neighbours.north = con
            con.neighbours.south = self

        elif (con.pos[0] == self.pos[0] and
              con.pos[1] == self.pos[1] + 1):
            self.neighbours.east = con
            con.neighbours.west = self

        elif (con.pos[0] == self.pos[0] and
              con.pos[1] == self.pos[1] - 1):
            self.neighbours.west = con
            con.neighbours.east = self

    def make_wall(self,con):
        if con == self.neighbours.north:
            self.neighbours.north = None
            con.neighbours.sout = None

        if con == self.neighbours.south:
            self.neighbours.south = None
            con.neighbours.north = None

        if con == self.neighbours.west:
            self.neighbours.west = None
            con.neighbours.east = None

        if con == self.neighbours.east:
            self.neighbours.east = None
            con.neighbours.west = None

        return

    def get_pos(self):
        return self.pos

    def __str__(self):
        if not self._fill:
            return '   '
        return self._fill