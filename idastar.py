from Project.node import Node


class IDAstar:
    def __init__(self, file):
        self.Node = Node(file)
        self.Node.insertGraph()
        self.h = {}
        self.expands = 0
        self.path = []

    def run(self, s=None):
        if s is None:
            s = self.Node.Source
        self.makeheuristics()
        bound = self.h[s]
        while 1:
            t = self.search(s, 0, bound)
            if t == 'FOUND':
                return bound
            if t == 999999999:
                return 'NOT FOUND'
            bound = t

    def search(self, node, g, bound):
        self.expands += 1
        f = g + self.h[node]
        if f > bound:
            return f
        if node == self.Node.Dest:
            return 'FOUND'
        minimum = 999999999
        for element in self.Node.Nodes[node]:
            t = self.search(element[2], g+int(element[1]), bound)
            if t == 'FOUND':
                self.path.append([element[0], element[1]])
                return 'FOUND'
            if t < minimum:
                minimum = t
        return minimum

    def makeheuristics(self):
        start = self.Node.Source

    def returnPath(self):
        self.path.reverse()
        return self.path