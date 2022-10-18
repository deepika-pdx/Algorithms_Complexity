# Create test data
class Node:
    def __init__(self, data):
        self.children = []
        self.data = data
        self.visited = False

    def add_child(self, obj):
        self.children.append(obj)


def generateTestData():
    testGraph = []
    node1 = Node(100)
    node2 = Node(200)
    node3 = Node(300)
    node4 = Node(400)
    node5 = Node(500)

    node2.add_child(node4)
    node2.add_child(node3)

    node3.add_child(node2)
    node3.add_child(node5)

    node4.add_child(node2)
    node4.add_child(node5)

    node5.add_child(node4)
    node5.add_child(node3)

    testGraph.append(node1)
    testGraph.append(node2)
    testGraph.append(node3)
    testGraph.append(node4)
    testGraph.append(node5)

    return testGraph


def generateAdjacencyList(G):
    adjList = dict()
    graph_node_list = []
    for graph in G:
        if len(graph.children) > 0:
            adjList.update({graph.data: graph.children})
        graph_node_list.append(graph)
    return adjList, graph_node_list


def BFSBipartiteGraphTest(graph):
    graph_adj_list, graph_node_list = generateAdjacencyList(graph)

    isBipartiteGraph = True

    node_v = graph[0]
    queue = [node_v]

    while len(queue) != 0:
        node_v = queue.pop()
        if not node_v.visited:
            node_v.visited = True
            nodeAdjList = graph_adj_list.get(node_v.data)
            if nodeAdjList is None or len(nodeAdjList) <= 1:
                index = graph_node_list.index(node_v)
                if (index + 1) != len(graph_node_list):
                    node_next = graph_node_list[index + 1]
                    queue.append(node_next)
                graph_node_list.remove(node_v)
                continue
            else:
                for i in range(len(nodeAdjList)):
                    queue.append(nodeAdjList[i])
                    for j in range(i + 1, len(nodeAdjList), 1):
                        currentNodeData = nodeAdjList[i].data
                        isConnected = any(child.data == currentNodeData for child in nodeAdjList[j].children)
                        if isConnected:
                            isBipartiteGraph = False
                            return isBipartiteGraph
    return isBipartiteGraph


graph_to_be_tested = generateTestData()
isBipartite = BFSBipartiteGraphTest(graph_to_be_tested)
print(isBipartite)
