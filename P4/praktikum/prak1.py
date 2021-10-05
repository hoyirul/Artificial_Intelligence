graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F',  'G'],
    'F': ['H'],
    'G': ['H'],
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

# penjelasan dari program tersebut adalah
# pembuatan funsi dfs yang berparameter
# append digunakan pada akhir daftar untuk menambahkan objek baru.
# dan perulangan pada queue
# pop yang berfungsi sebagai mengeluarkan dan mengapus data FIFO
# dan ada kondisi perulangan for


print("Hasil penulusuran grapf menggunakan BFS:")
bfs(visited, graph, 'A')
