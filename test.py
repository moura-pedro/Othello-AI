list = [None for _ in range(8)]

maze = [list.copy for _ in range(8)]

maze[3][3] = 1
maze[3][4] = 0
maze[4][3] = 0
maze[4][4] = 1
print(maze)

