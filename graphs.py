'''
The Graph class below is implemented as an adjency list as, relative to an adjency
matrix, the adjency list takes up less space when using a sparse graph (which is
more common). The Graph class maps a vertex's id to its Vertex object (i.e. a node).
The Vertex class uses a dictionary to represent a (to) Vertex's edges by mapping the
"from" Vertex to the weight of the edge between the "to" and "from" Vertex objects.
'''

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connections = {}

    def addEdge(self, key, weight=0):
        self.connections[key] = weight

    def getID(self):
        return self.id

    def getConnections(self):
        return self.connections.keys()

    def getConnectionWeight(self, key):
        return self.connections[key]

class Graph:
    def __init__(self):
        self.vertices = {}

    def length(self):
        return len(self.vertices.keys())

    def contains(self, id):
        return id in self.vertices

    def addVertex(self, id):
        new = Vertex(id)
        self.vertices[id] = new

    def getVertex(self, id):
        if id in self.vertices:
            return self.vertices[id]
        else:
            return None

    def addEdge(self, from, to, weight):
        if from not in vertices:
            self.addVertex(from)
        if to not in vertices:
            self.addVertex(to)
        self.vertices[from].addEdge(self.vertices[to], weight)
