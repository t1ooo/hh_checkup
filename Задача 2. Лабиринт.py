# %%
# прямоугольник высотой N и шириной M
# проход 0 или стена 1
# На карте отмечен выход, и он находится в ячейке с координатами (x2,y2).
# найти длину кратчайшего пути из ячейки пробуждения в ячейку выхода. В случае, если такого пути нет – нужно вывести 0

from collections import defaultdict


DIRECTIONS = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
]

INF = float("inf")


def neighbors(y, x, grid):
    ns = []
    for yd, xd in DIRECTIONS:
        y2 = y + yd
        x2 = x + xd
        if (0 <= y2 < len(grid)) and (0 <= x2 < len(grid[y])) and grid[y2][x2] == 0:
            ns.append((y2, x2))
    return ns


def min_score(open_set, f_score):
    min_v = INF
    min_k = next(iter(open_set))
    for v in open_set:
        if min_v < f_score[v]:
            min_v = f_score[v]
            min_k = v
    return min_k


def reconstruct_path(came_from, current):
    total_path = [current]
    for current in came_from.keys():
        current = came_from[current]
        total_path.append(current)
    return total_path


def h(x):
    return 1


def inf():
    return INF


def a_star(grid, start, goal, h):
    open_set = set()
    open_set.add(start)

    came_from = {}

    g_score = defaultdict(inf)
    g_score[start] = 0

    f_score = defaultdict(inf)
    f_score[start] = h(start)

    while len(open_set) > 0:
        current = min_score(open_set, f_score)
        if current == goal:
            return len(set(reconstruct_path(came_from, current))) - 1

        open_set.remove(current)

        y, x = current
        for neighbor in neighbors(y, x, grid):
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor)
                if neighbor not in open_set:
                    open_set.add(neighbor)

    return 0


N, M = [3, 3]
init = (0, 0)
goal = (0, 2)

grid = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 0],
]

answer = a_star(grid, init, goal, h)
print(answer)
