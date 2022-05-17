from Graph import Graph

graph = Graph()

graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "E")
graph.add_edge("E", "F")

print(graph.getNode("C"))


def test_addNode():
    assert graph.add_node("G") == True


def test_addEdge():
    assert graph.add_edge("F", "G") == True


def test_getNode():
    node = graph.getNode("F")
    assert node[0] == "G"
