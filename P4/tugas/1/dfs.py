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
visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(visited, graph, neighbor)


print("Hasil penulusuran grapf menggunakan DFS:")
dfs(visited, graph, 'A')
