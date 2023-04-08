from unicodedata import name


class Edge:
    def __init__(self,vertex1,vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight
    
    def getEdgeDetails(self):
        return "Edge: {} <-----{}-----> {}".format(self.vertex1,self.weight,self.vertex2)

class Graph:

    def __init__(self):
        self.vertices= {}

    def addEdge(self,edge, isDirected=False):
        if edge.vertex1 not in self.vertices:
            self.vertices[edge.vertex1]=[]

        if edge.vertex2 not in self.vertices:
            self.vertices[edge.vertex2]=[]

        self.vertices[edge.vertex1].apppend(edge.vertex2)

        if not isDirected:
            self.vertices[edge.vertex2].append(edge.vertex1)

    def printGraph(self):
        print("Number of Vertices in Graph:", len(self.vertices))

        keys = self.vertices.key()

        for key in keys:
            print(key,":", end="")
            print(self.vertices[key], end="")
            print()
            print("-----------------------------")

def main():

    edge0=Edge(0,1,4)
    edge1=Edge(0,2,4)
    edge2=Edge(0,3,6)
    edge3=Edge(0,4,6)
    edge4=Edge(1,2,2)
    edge5=Edge(2,3,8)
    edge6=Edge(3,4,9)

    edges=[edge0,edge1,edge2,edge3,edge4,edge5,edge6]

    for edge in edges:
        print(edge.getEdgeDeatils())
    
    graph=Graph()
    graph.printGraph()

    for edge in edges:
       graph.addEdge(edge)

    graph.printGraph()

    if __name__ == '__main__':
        main()
