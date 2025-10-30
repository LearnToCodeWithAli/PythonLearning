# dfs - depth first search
# binary trees only
# preorder, postorder, inorder

# preorder - root, left, right
# postorder - left, right, root
# inorder - left, root, right


tree = {"A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": ["G"],
        "E": [],
        "F": [],
        "G": []}



# how to use github for projects
def preorder_dfs(graph, node, visited):
    if not visited:
        visited = set()

    print(node)
    visited.add(node)
    check_left_child(graph, node, visited)
    check_right_child(graph, node, visited)

def postorder_dfs(graph, node, visited):
    if not visited:
        visited = set()

    check_left_child(graph, node, visited)
    check_right_child(graph, node, visited)

    print(node)
    visited.add(node)

def inorder_dfs(graph, node, visited):
    if not visited:
        visited = set()

    check_left_child(graph,node,visited)
    print(node)
    check_right_child(graph,node,visited)

def check_left_child(graph, node, visited):
    if len(graph[node]) > 0:
        preorder_dfs(graph, graph[node][0], visited)

def check_right_child(graph, node, visited):
    if len(graph[node]) > 1:
        preorder_dfs(graph, graph[node][1], visited)

# inorder_dfs(tree,"A",None)




def iterative_preorder_dfs(graph, node):

    stack = [] # last in first out
    stack.append(node)

    leaves = []
    parents = []
    result = []

    while len(stack) > 0:

        current = stack.pop()
        # do something with the current node

        if len(graph[current]) > 1:
            stack.append(graph[current][1])
        if len(graph[current]) > 0:
            stack.append(graph[current][0])

        if len(graph[current]) == 0:
            leaves.append(current)
        else:
            parents.append(current)

        result.append(current)

    # print(f"leaves: {leaves}")
    # print(f"parents: {parents}")

    return result

# def iterative_postorder_dfs(graph, node):
#
#     stack = [] # last in first out
#     stack.append(node)
#
#     while len(stack) > 0:
#
#         current = stack.pop()
#         # do something with the current node
#
#
#         if len(graph[current]) > 1:
#             stack.append(graph[current][1])
#         if len(graph[current]) > 0:
#             stack.append(graph[current][0])
#
#         print(current)


print(iterative_preorder_dfs(tree, "A"))
print()

# preorder_dfs(tree,"A", None)















































