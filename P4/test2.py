graph = {
    'A': set(['B']),
    'B': set(['G', 'F']),
    'C': set(['D']),
    'D': set(['H']),
    'E': set([]),
    'F': set(['E']),
    'G': set(['C']),
    'H': set([]),
}

# visited = set()


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start, end=" ")

    for next in graph[start] - visited:
        print(next)
        dfs(graph, next, visited)
    return visited


dfs(graph, 'A')
