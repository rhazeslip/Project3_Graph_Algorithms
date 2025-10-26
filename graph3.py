# Undirected Weighted Graph Problem 3

import collections
import heapq

# Class to represent an undirected weighted graph
class Graph:
    def __init__(self):
        self.nodes = set() 
        self.edges = collections.defaultdict(list)  
        self.distances = {} 

    def add_node(self, value):
        """Add a node to the graph"""
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

# Using Dijkstra's algorithm to find the shortest path tree
def dijkstra(graph, initial):
    visited = {initial: 0}  
    path = {}  
    nodes = set(graph.nodes) 

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

# Uses Prim's algorithm to find the Minimum Spanning Tree
def prims_mst(graph):
    """Prim's algorithm to find minimum spanning tree"""
    if not graph.nodes:
        return [], 0
    
    start_node = next(iter(graph.nodes))
    visited = {start_node}  
    mst_edges = []  
    total_weight = 0  
    pq = []  
    
    for neighbor in graph.edges[start_node]:
        weight = graph.distances[(start_node, neighbor)]
        heapq.heappush(pq, (weight, start_node, neighbor))
    
    while pq and len(visited) < len(graph.nodes):
        weight, from_node, to_node = heapq.heappop(pq)
        
        if to_node in visited:
            continue
        
        visited.add(to_node)
        mst_edges.append((from_node, to_node, weight))
        total_weight += weight
        
        for neighbor in graph.edges[to_node]:
            if neighbor not in visited:
                edge_weight = graph.distances[(to_node, neighbor)]
                heapq.heappush(pq, (edge_weight, to_node, neighbor))
    
    return mst_edges, total_weight

# Main function to run all parts of question 3
def main():
    graph = Graph()
    
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for node in nodes:
        graph.add_node(node)
    
    edges = [
        ('A', 'B', 22), ('A', 'C', 9), ('A', 'D', 12),
        ('B', 'C', 35), ('B', 'E', 36), ('B', 'F', 34), ('B', 'H', 24),
        ('C', 'D', 4), ('C', 'F', 42), ('C', 'G', 65),
        ('D', 'G', 33),
        ('E', 'F', 18), ('E', 'H', 39), ('E', 'I', 25),
        ('F', 'G', 23), ('F', 'H', 19),
        ('G', 'J', 21),
        ('H', 'I', 19),
        ('I', 'J', 39),
    ]
    
    for from_node, to_node, weight in edges:
        graph.add_edge(from_node, to_node, weight)
    
    print("Part 3: Weighted Graph - Shortest Path Tree and MST")
    print("="*60)
    
    # Part 3A
    visited, path = dijkstra(graph, 'A')
    print(f"Shortest path tree from A: {dict(sorted(visited.items()))}")
    
    # Part 3B
    mst_edges, mst_weight = prims_mst(graph)
    mst_display = [(f, t) for f, t, w in mst_edges]

    # Part 3C
    print(f"Minimum spanning tree edges: {mst_display}")
    print(f"Total MST weight: {mst_weight}")
    print(f"\nSPT and MST usually the same: False")
    
    # Part 3D
    has_negative = any(w < 0 for w in graph.distances.values())
    print(f"Graph has negative weights: {has_negative}")
    print(f"Can apply Dijkstra with negative weights: False")


if __name__ == "__main__":
    main()
