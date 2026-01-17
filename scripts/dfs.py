def dfs(start_node, graph):

    visited = {}
    def visit(node):
        visited[node] = True

        for v in graph[node]:
            if v not in visited:
                visit(v)

    visit(start_node)
