import Maze
import sys

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Error numero de argumentos")
		exit()

	file = open(sys.argv[1], "r")
	m = Maze.Maze(1, 1)
	text = file.readlines()
	m.grid.get_grid(text)
	m.redefine_start_end()
	m.find_shortest_solution()
	print(m)
