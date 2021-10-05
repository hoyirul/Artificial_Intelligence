graph = {
    'A': ['B'],
    'B': ['G', 'F'],
    'C': ['D'],
    'D': ['H'],
    'E': [],
    'F': ['E'],
    'G': ['C'],
    'H': [],
}

visited = []  # List to keep track of visited nodes
queue = []  # Initialize a queue


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if s == 'D':
                break
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print("Hasil penulusuran grapf menggunakan BFS:")
bfs(visited, graph, 'A')
