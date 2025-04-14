
cost = {'S': 0, 'G': 0, '.': 1, '~': 3, '^': 5, '#': 9999}
print("Enter 10 rows of the grid (space-separated):")
grid = [input().split() for _ in range(10)]
for y in range(10):
    for x in range(10):
        if grid[y][x] == 'S': start = (x, y)
        if grid[y][x] == 'G': goal = (x, y)
def h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def path_finder(start, goal):
    start_list = [start]
    came_from = {}
    g_score = {start: 0}
    while start_list:
        current = min(start_list, key=lambda n: g_score[n] + h(n, goal))
        start_list.remove(current)
        if current == goal:
            break
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < 10 and 0 <= ny < 10:
                next = (nx, ny)
                tile = grid[ny][nx]
                tile_cost = cost[tile]
                if tile != '#':
                    new_cost = g_score[current] + tile_cost
                    if next not in g_score or new_cost < g_score[next]:
                        g_score[next] = new_cost
                        came_from[next] = current
                        if next not in start_list:
                            start_list.append(next)
    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()
    return path, g_score[goal]
path, total = path_finder(start, goal)
print("\nPath:")
for step in path:
    print(step)
print("Total Cost:", total)


#Logic of code-
#The code is designed to move a robot from a start point (S) to a goal point (G) on a 10×10 grid, where each cell has a movement cost depending on the terrain type. First, it takes the grid as input and identifies the coordinates of the start and goal. Then it explores different paths step by step, always choosing the next position based on two things:
#1)The total cost to reach that position from the start.
#2)An estimated distance from that position to the goal (called heuristic, using Manhattan distance).
#The algorithm stores the cost of reaching each position (g_score) and remembers where each cell was reached from (came_from) to later reconstruct the path. If a new path to a position is cheaper than the previously known one, it updates the cost and continues. Once the goal is reached, it traces back the path using the came_from dictionary and prints each step along with the total cost. The logic ensures the robot avoids walls (#) and chooses the path with the least total cost, not necessarily the shortest distance.
