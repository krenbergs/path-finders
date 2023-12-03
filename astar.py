import heapq
import math

def heuristic(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2)

def astar(start, goal, walls):

    start = tuple(start)
    goal = tuple(goal)
    walls = set(map(tuple, walls))

    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        for dx, dy, dz in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1), 
                            (1,1,0), (-1,-1,0), (1,-1,0), (-1,1,0), 
                            (1,0,1), (-1,0,-1), (1,0,-1), (-1,0,1), 
                            (0,1,1), (0,-1,-1), (0,1,-1), (0,-1,1), 
                            (1,1,1), (-1,-1,-1), (1,1,-1), (-1,-1,1), (1,-1,1), (-1,1,-1)]:
            next_cube = (current[0] + dx, current[1] + dy, current[2] + dz)
            if next_cube in walls:
                continue
            new_cost = cost_so_far[current] + 1
            if next_cube not in cost_so_far or new_cost < cost_so_far[next_cube]:
                cost_so_far[next_cube] = new_cost
                priority = new_cost + heuristic(goal, next_cube)
                heapq.heappush(frontier, (priority, next_cube))
                came_from[next_cube] = current

    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path
