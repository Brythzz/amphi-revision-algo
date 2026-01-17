def bfs(start_node, graph):
    visited = {start_node: True}
    queue = deque([start_node])

    while queue:
        node = queue.popleft()

        for v in graph[node]:
            if v not in visited:
                visited[v] = True
                queue.append(v)
