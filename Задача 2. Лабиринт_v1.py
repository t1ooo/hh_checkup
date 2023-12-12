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


def gen_graph(grid):
    graph = defaultdict(list)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                continue
            for yd, xd in DIRECTIONS:
                y2 = y + yd
                x2 = x + xd
                if (
                    (0 <= y2 < len(grid))
                    and (0 <= x2 < len(grid[y]))
                    and grid[y2][x2] == 0
                ):
                    graph[(y, x)].append((y2, x2))
    return dict(graph)


def min_dist(queue, dist):
    min_v = float("inf")
    min_i = -1
    for i in range(len(queue)):
        if min_v > dist[queue[i]]:
            min_v = dist[queue[i]]
            min_i = i
    return min_i


def dijkstra(graph, init, goal):
    dist = {}
    queue = []
    for v in graph.keys():
        dist[v] = float("inf")
        queue.append(v)
    dist[init] = 0

    while len(queue) != 0:
        i = min_dist(queue, dist)
        u = queue[i]
        if u == goal:
            break
        del queue[i]

        for v in graph[u]:
            if v in queue:
                alt = dist[u] + 1
                if alt < dist[v]:
                    dist[v] = alt

    if dist[goal] == float("inf"):
        return 0
    return dist[goal]


N, M = [int(n) for n in input().split(" ")]
init = tuple([int(n) for n in reversed(input().split(" "))])
goal = tuple([int(n) for n in reversed(input().split(" "))])
grid = []
for _ in range(N):
    grid.append([int(n) for n in input().split(" ")])


graph = gen_graph(grid)
answer = dijkstra(graph, init, goal)
print(answer)
