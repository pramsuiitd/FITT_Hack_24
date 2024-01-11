from nodes import Node

def graph_discovery(adj_matrix):
    public_key = 'xxxx'
    network = []
    for each in len(adj_matrix):
        new_node = Node(each*225, each*255, public_key)
        network.append(new_node)
    