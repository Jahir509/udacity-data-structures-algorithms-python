class Vertex:
    def __init__(self, id, val):
        self.id = id
        self.val = val
        self.edges = []

class Edge:
    def __init__(self, to, from, weight):
        self.from = from
        self.to = to
        self.weight = weight

def dfs_recursive(graph, node, seen=set()):
    seen.add(node)
    print(node.val)
    for edge in node.edges:
        if edge.to not in seen:
            dfs_recursive(graph, edge.to, seen)

def dfs_iterative(node):
    result = []
    stack = [node]
    seen = set()
    while stack:
        curr = stack.pop()
        if curr not in seen:
            result.append(curr.val)
            seen.add(curr)
        for edge in curr.edges:
            if edge.to not in seen:
                stack.append(edge.to)
    return result
