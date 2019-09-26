import time
from Project.parser import Parser
from Project.node import Node
from Project.dfs import DFS
from Project.idastar import IDAstar

testfile = 'sampleGraph1.txt'

db = Parser()
start_time = time.time()
db.parse(testfile)
print("\n---Parsing took %s seconds---\n" % (time.time() - start_time))

start_time = time.time()
nd = Node(testfile)
nd.insertGraph()
print("\n---Making the Graph took %s seconds---\n" % (time.time() - start_time))

print('Starting DFS...')
start_time = time.time()
df = DFS(testfile)
df.run(nd.Source, nd.Dest)
print('Path:', df.returnPath())
df.printCostofPath()
print("\n---DFS took %s seconds---\n" % (time.time() - start_time))

start_time = time.time()
ida = IDAstar(testfile)
print(ida.run())
print('Expands:', ida.expands)
print(ida.returnPath())
print("\n---IDA* took %s seconds---\n" % (time.time() - start_time))