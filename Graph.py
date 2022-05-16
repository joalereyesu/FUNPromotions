class Graph():
    def __init__(self):
        self.adjacency_lst = {}
        self.list = []

    def add_node(self, node):
        if node not in self.list:
            self.list.append(node)
        else:
            return "The given node does not exist"

    def add_edge(self, node1, node2):
        temp = []
        if node1 in self.list and node2 in self.list:
            if node1 not in self.adjacency_lst:
                temp.append(node2)
                self.adjacency_lst[node1] = temp

            elif node1 in self.adjacency_lst:
                temp.extend(self.adjacency_lst[node1])
                temp.append(node2)
                self.adjacency_lst[node1] = temp

            else:
                print("The given node does not exist")

    def getNode(self, node):
        if node in self.list:
            return self.adjacency_lst[node]
        else:
            return False

    def getAllInfo(self):
        return self.adjacency_lst

    def disp_graph(self):
        for node in self.adjacency_lst:
            print(node, "->", [i for i in self.adjacency_lst[node]])
