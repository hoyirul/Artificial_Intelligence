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


def dfs(graph, start, goal):
    stack = [[start]]
    visited = []

    while stack:
        path = stack.pop(0)
        node = path[-1]
        if node == goal:
            return print("This is the path : ", path)

        children = graph[node]
        for child in children:
            if child not in visited:
                newPath = path + [child]
                stack.insert(0, newPath)
                visited.append(child)


dfs(graph, 'A', 'D')
