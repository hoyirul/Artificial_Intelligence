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

visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)

        for neighbour in graph[node]:
            if node == 'D':
                print('==============================')
                break
            else:
                dfs(visited, graph, neighbour)


print("Hasil penulusuran grapf menggunakan DFS:")
dfs(visited, graph, 'A')
