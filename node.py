from operator import itemgetter


class Node:
    def __init__(self, file):
        from Project.parser import Parser
        self.parser = Parser()
        self.parser.parse(file)
        self.Nodes = {}
        self.Source = self.parser.Source
        self.Dest = self.parser.Dest

    def insertGraph(self):
        for node in self.parser.Node:
            for road in self.parser.Node[node]:
                self.Nodes.setdefault(node, []).append([road, self.parser.Road_val[road], [other for other in self.parser.Road_ends[road] if not other == node][0]])
            self.Nodes[node] = sorted(self.Nodes[node], key=itemgetter(1))