graph = {
    'A': ['B', 'E', 'F'],
    'B': ['F', 'G'],
    'C': ['D', 'G'],
    'D': ['C', 'H'],
    'E': ['F'],
    'F': ['B'],
    'G': ['C', 'H'],
    'H': [],
}

visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


print("Hasil penulusuran grapf menggunakan BFS:")
bfs(visited, graph, 'A')
