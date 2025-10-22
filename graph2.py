#Digraph Problem 2
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Create the directed graph from the first dataset
G2 = nx.DiGraph()
nodes_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
G2.add_nodes_from(nodes_2)

edges_2 = [(1,3), (3,5), (3,2), (2,1), (4,2), (4,1), (4,12),
           (5,8), (5,6), (6,7), (6,10), (6,8), (7,10), (8,10),
           (8,9), (9,5), (9,11), (10,9), (10,11), (11,12)]
G2.add_edges_from(edges_2)

def analyze_scc(graph):
    scc = list(nx.strongly_connected_components(graph))
    print("Strongly Cnnected Components: ")
    for i, component in enumerate(scc):
        print(f"Component {i+1}: {component}")
        
    condensation = nx.condensation(graph)
    
    print(f"\nMeta Graph nodes: {list(condensation.nodes())}")
    print(f"Meta Graph Edges: {list(condensation.edges())}")
    
    try:
        topo_order = list(nx.topological_sort(condensation))
        print(f"Topological order: {topo_order}")
    except nx.NetworkXError:
        print("Graph has cycles, cannot perform topological sort on original graph")
    
    return scc, condensation

print("\nPart 2: Directed Graph - Strongly Connected Components")
print("=" * 60)
scc_components, meta_graph = analyze_scc(G2)