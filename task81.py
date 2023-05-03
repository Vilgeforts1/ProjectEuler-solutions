# TASK 81 FROM projecteuler.net

# matrix = [[131, 673, 234, 103, 18],
#           [201, 96, 342, 965, 150],
#           [630, 803, 746, 422, 111],
#           [537, 699, 497, 121, 956],
#           [805, 732, 524, 37, 331]]


matrix = []
with open('p081_matrix.txt', 'r', encoding='utf-8') as file:
    for row in file.readlines():
        r = list(map(lambda x: int(x), row.split(',')))
        matrix.append(r)


def get_graph(massive, dictionary=None):
    n = len(massive)
    if dictionary is None:
        dictionary = {}
    for i in range(n):
        for j in range(n):
            if i < n - 1 and j < n - 1:
                dictionary[(i, j)] = [(i + 1, j), (i, j + 1)]
            elif i == n - 1 and j < n - 1:
                dictionary[(i, j)] = [(i, j + 1)]
            elif j == n - 1 and i < n - 1:
                dictionary[(i, j)] = [(i + 1, j)]
            else:
                break
    return dictionary


def costs_graph(massive, dictionary=None):
    infinity = float("inf")
    n = len(massive)
    if dictionary is None:
        dictionary = {}
    for i in range(n):
        for j in range(n):
            dictionary[(i, j)] = infinity

    dictionary[(0, 0)] = matrix[0][0]

    return dictionary


def arg_min(cos, vis):
    v_min = (-1, -1)
    m = float('inf')
    for k, v in cos.items():
        if v < m and k not in vis:
            m = v
            v_min = k

    return v_min


N = len(matrix)
start = (0, 0)  # start index
visited = {start}  # visited

graph = get_graph(matrix)
costs = costs_graph(matrix)

while start != (-1, -1):
    for vertex in graph[start]:
        if vertex not in visited:
            a, b = vertex
            weight = costs[start] + matrix[a][b]
            if weight < costs[vertex]:
                costs[vertex] = weight

    start = arg_min(costs, visited)
    if start[0] * start[1] >= 0:
        visited.add(start)
    if start == (N - 1, N - 1):
        break


print(costs[(N - 1, N - 1)])






