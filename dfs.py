from Project.node import Node

class DFS:
    def __init__(self, file, s=None, d=None):
        self.Node = Node(file)
        self.Node.insertGraph()
        self.discovered = []
        self.expands = 0
        self.path = []
        #self.run(s,d)

    def run(self, s=None, d=None):
        if s is None:
            s = self.Node.Source
        if d is None:
            d = self.Node.Dest
        print('\nNode', s, 'starting to expand')
        self.discovered.append(s)
        self.expands += 1
        print(self.expands, 'expands in total')
        for element in self.Node.Nodes[s]:
            print('Checking', element[2], 'for expansion')
            if element[2] not in self.discovered:
                if s == d:
                    print('Found Destination!')
                    return 'Fin'
                print(element[2], 'not visited, Road:', element[0], 'value:', element[1])
                print('Moving to', element[2])
                if self.run(element[2]) is 'Fin':
                    self.path.append([element[0], element[1]])
                    return 'Fin'
            else:
                print(element[2], 'has been visited')

    def returnPath(self):
        self.path.reverse()
        return self.path

    def printCostofPath(self):
        roads = 0
        val = 0
        for list in self.path:
            roads += 1
            val += int(list[1])
        print('\nUsed', roads, 'roads, total value is:', val)