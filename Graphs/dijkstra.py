'''
Assume implementation of these classes: Graph, Vertex (e.g. start), Edge, Heap (aka Priority Queue ADT)
Also: Initialization of distance at each vertex except start is infinity
-> When traversing graph, I can set the vertex's distance to infinity the first time I encounter it.
'''

def dijkstra(graph, start):
    pq = Heap()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in graph])
    while pq:
        curr = pq.delMin()
        for new in curr.getConnections():
            newDist = curr.getDistance() + curr.getWeight(new)
            if newDist < new.getDistance():
                new.setDistance(newDist)
                new.setPred(curr)
                pq.decreaseKey(new,newDist)
