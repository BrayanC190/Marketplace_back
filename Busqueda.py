from collections import deque

def breadth_first_search(graph, start, goal):
   
    queue = deque([[start]])
    
    visited = set()
    
    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return []
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H', 'I'],
    'F': [],
    'G': ['J'],
    'H': [],
    'I': [],
    'J': []
}

path = breadth_first_search(graph, 'A', 'J')
path