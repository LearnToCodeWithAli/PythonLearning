


#dfs: pre-order, in-order, post-order traversal


def recursive_dfs(tree, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node)

    for child in tree[node]:
        if child not in visited:
            recursive_dfs(tree, node, visited)


graph = {"A": ["B","C"],
         "B": ["D", "E"],
         "C": ["F", "G"],
         "F": ["H"]}

recursive_dfs(graph)