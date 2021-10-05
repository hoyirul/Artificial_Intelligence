graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['H'],
    'G': ['H'],
    'H': ['G'],
}

visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(visited, graph, neighbor)
# penjelasan dari program tersebut adalah
# pembuatan funsi DFS yang berparameter
# dan ada kondisi jika node tidak di variable visited
# maka akan print(node) dan menambahkan node -> add(node)
# perulangan neighbor in graph[node]
# jika neighbor tidak di visited maka akan di paggil lagi fungsi DFS


print("Hasil penulusuran grapf menggunakan DFS:")
dfs(visited, graph, 'A')
