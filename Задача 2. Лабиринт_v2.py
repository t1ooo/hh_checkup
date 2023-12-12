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


INF = float("inf")


def minimum_distance(dist, visited):
    min_v = INF
    min_i = next(iter(dist))
    for v in dist.keys():
        if dist[v] < min_v and (v not in visited):
            min_v = dist[v]
            min_i = v
    return min_i


def dijkstra(graph, init, goal):
    dist = {}
    visited = set()
    for v in graph.keys():
        dist[v] = INF
    dist[init] = 0

    for _ in range(len(graph.keys())):
        u = minimum_distance(dist, visited)
        if u == goal:
            if dist.get(goal, INF) == INF:
                return 0
            return dist.get(goal, INF)
        visited.add(u)

        for v in graph[u]:
            alt = dist.get(u, INF) + 1
            if alt < dist.get(v, INF) and (v not in visited):
                dist[v] = alt

    return 0


N, M = [int(n) for n in input().split(" ")]
init = tuple([int(n) for n in reversed(input().split(" "))])
goal = tuple([int(n) for n in reversed(input().split(" "))])
grid = []
for _ in range(N):
    grid.append([int(n) for n in input().split(" ")])


graph = gen_graph(grid)
answer = dijkstra(graph, init, goal)
print(answer)
