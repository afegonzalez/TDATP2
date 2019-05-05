import Grid
import Stack
import random
from collections import deque


class Maze:
	def __init__(self, width, height):
		self.grid = Grid.Grid(width, height)
		self.start = self.grid.matrix[0][0]
		self.finish = self.grid.matrix[width-1][height-1]

	def redefine_start_end(self):
		self.start = self.grid.matrix[0][0]
		self.finish = self.grid.matrix[self.grid.get_height()-1][self.grid.get_width()-1]

	def build_dfs(self):
		s = Stack.Stack(self.start)
		visited_cells = set()
		while len(s.stack):   # len() es O(1), while O(n)
			current_cell = s.get_next()  # O(1)
			if current_cell not in visited_cells:
				visited_cells.add(current_cell)
				possible_paths = self.grid.get_adjacent_cells(current_cell)
				potentials = [x for x in possible_paths if x not in visited_cells]  # O(E)? reviso si estan en visitados
				if potentials:
					next_cell = random.choice(potentials)  # O(1)
					current_cell.connect(next_cell)  # O(1)
				s.add(potentials)  # O(1)

	def __solve_maze_bfs(self):
		parent = {self.start: None}
		dist = {self.start: 0}

		visited_cells = set()
		q = deque()
		q.append(self.start) # O(1)
		visited_cells.add(self.start)  # O(1) en gral, O(n) por caso con hash colpasado
									   # add mas lento pero ver si contiene va a ser generalemnte mas rapido que lista
		while len(q):
			current_cell = q.popleft()  # O(1)
			n = current_cell.neighbours.get_not_null_neighbours()
			for each in n:  # O(E)? o O(1) con el mismo criterio que arriba?
				if each not in visited_cells:  # O(1) en gral, O(n) peor caso con hash colpasado
					visited_cells.add(each)  # O(1) en gral, O(n) peor caso
					parent[each] = current_cell  # O(1) en gral, O(n) peor caso
					dist[each] = dist[current_cell] + 1  # O(1) en gral, O(n) peor caso
					q.append(each)  #O(1)
		return parent, dist

	def find_shortest_solution(self):
		parent, distance = self.__solve_maze_bfs()
		cell = self.finish

		print("Longitud: " + str(distance[self.finish]))
		while parent[cell] is not None:
			cell.fill()
			cell = parent[cell]  # esto me garca la referencia en self.finish tambien no? Me importa eso? Creo que no
		cell.fill()

	def __str__(self):
		return str(self.grid)

	def join_grid(self):
		for row in self.grid.matrix:
			for elem in row:
				pos = elem.get_pos()
				adjacents = self.grid.get_adjacent_cells(elem)
				for adjacent in adjacents:
					adj_pos = adjacent.get_pos()
					self.grid.matrix[pos[0]][pos[1]].connect(self.grid.matrix[adj_pos[0]][adj_pos[1]])

	def _recursive_generation(self, y0, x0, yf, xf, cut = 0): #1 for vertical, 0 for horizontal cut
		if ((((xf-x0)<1)|((yf-y0)<1)) | ((xf-x0 == 1) | (yf-y0 ==1))):
		    return

		if (not cut) & (xf-x0 < 2):
			cut = 1

		if cut:
			if(yf-y0 >= 2):
				xw = random.randrange(x0,xf) #busca corte
				while(xw == x0):
					xw = random.randrange(x0,xf) #busca corte
				yh = random.randrange(y0,yf) #elige agujero
				for yy in range(y0,yf):
					if (yy != yh):
						self.grid.matrix[yy][xw].make_wall(self.grid.matrix[yy][xw-1])
				next_cut = 0
				self._recursive_generation(y0, x0, yf, xw, next_cut)
				self._recursive_generation(y0, xw, yf, xf, next_cut)

		elif not cut:
			if(xf-x0 >= 2):
				yw = random.randrange(y0,yf) #buscar corte
				while(yw == y0):
					yw = random.randrange(y0,yf) #busca corte
				xh = random.randrange(x0,xf) #elige agujero
				for xx in range(x0,xf):
					if(xx != xh):
						self.grid.matrix[yw-1][xx].make_wall(self.grid.matrix[yw][xx])
				next_cut = 1
				self._recursive_generation(y0, x0, yw, xf, next_cut)
				self._recursive_generation(yw, x0, yf, xf, next_cut)

		return

	def recursive_generation(self):
		width = self.grid.get_width()
		height = self.grid.get_height()
		cut = random.randrange(0,2)
		self._recursive_generation(0, 0, height, width, cut)
		return