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

def bfs(node):
    result = []
    queue = [node]
    seen = set()
    while queue:
        curr = queue.pop(0)
        if curr not in seen:
            seen.add(curr)
            result.append(curr.val)
        for edge in curr.edges:
            if edge.to not in seen:
                queue.append(edge.to)
    return result
