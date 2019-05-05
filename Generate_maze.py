#!/usr/bin/python3

import Maze
import sys

if len(sys.argv) != 4:
	print("Error")
	exit()

if((int(sys.argv[2]) <= 0) | (int(sys.argv[3]) <= 0)):
	print("Error indice negativo")
	exit()

m = Maze.Maze(int(sys.argv[3]), int(sys.argv[2]))

if (str(sys.argv[1]) == "dfs"):
	m.build_dfs()

if (str(sys.argv[1]) == "dyv"):
	m.join_grid()
	m.recursive_generation()

else:
	print("Error funcion no reconocida")
	exit()

file = open("maze.txt","w")

file.write(str(m))