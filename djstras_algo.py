class Graph:
    def __init__(self,adjacency_list):
        self.adj_list = adjacency_list
        
class Vertex:
    def __init__(self,value=None):
        self.value = None

class Edge:
    def __init__(self,distance=None,vertex=None):
        self.distance = distance
        self.vertex = vertex
        
class Queue:
    def __init__(self):
        # self.queues = [(2,"A"),(4,"B"),(5,"C")]
        self.queues = []
    def enqueue(self,dist,vertex):
        self.queues.append((dist,vertex))
        self.queues.sort(key=lambda x: x[0])
    def dequeue(self):
        result =  self.queues.pop(0)
        return result[0],result[1]
    def length_queue(self):
        return len(self.queues)
    
    def printing(self):
        return self.queues
# q = Queue()
# q.enqueue(1,"Z")
# print(q.printing())
# print(q.dequeue())
# print(q.printing())

def dijkstra_alog(graph,start):
    prev = { v:None for v in graph.adj_list.keys()}
    visited = { v:False for v in graph.adj_list.keys()}
    dist = { v:float("inf") for v in graph.adj_list.keys()}
    dist[start] = 0
    Queues = Queue()
    Queues.enqueue(0,start)
    while Queues.length_queue()>0:
        removed_dist , remove = Queues.dequeue()
        visited[remove] = True
        for edge  in graph.adj_list[remove]:
            if visited[edge.vertex] == True:
                continue
            new_distance = removed_dist+edge.distance
            if new_distance<dist[edge.vertex]:
                dist[edge.vertex] = new_distance
                prev[edge.vertex] = remove
                Queues.enqueue(new_distance, edge.vertex)
    return dist

vertices = [ Vertex("A"),
            Vertex("B"), 
            Vertex("C"), 
            Vertex("D"), 
            Vertex("E"),
            Vertex("F"), 
            Vertex("G"),
            Vertex("H")]
adj_list = {
    "A": [Edge(2, "B"), Edge(4, "C")],
    "B": [Edge(1, "C"), Edge(7, "D")],
    "C": [Edge(3, "E")],
    "D": [ Edge(1, "F")],
    "E": [Edge(2, "D"),  Edge(3, 'F')],
    "F": []
}

my_graph = Graph(adj_list)

g =dijkstra_alog(my_graph, start="A")
print(g)


# queues = [(2,"A"),(4,"B"),(5,"C")]        
# graph = {
#            "A" : ["B","C","D"],
#            "B" : ["A","C","E"],
#            "c" : ["A","B","E","F"],
#            "D" : ["A","F"],
#            "E" : ["B","C","F"],
#            "F" : ["C","D","E"]
#            }


# testing the algorithm
# vertices = [ Vertex("A"),
#             Vertex("B"), 
#             Vertex("C"), 
#             Vertex("D"), 
#             Vertex("E"),
#             Vertex("F"), 
#             Vertex("G"),
#             Vertex("H")]
# A, B, C, D, E, F, G, H = vertices
# adj_list = {
#     "A": [Edge(1.8, "B"), Edge(1.5, "C"), Edge(1.4, "D")],
#     "B": [Edge(1.8, "A"), Edge(1.6, "E")],
#     "C": [Edge(1.5, "A"), Edge(1.8, "E"), Edge(2.1, "F")],
#     "D": [Edge(1.4, "A"), Edge(2.7, "F"), Edge(2.4, "G")],
#     "E": [Edge(1.6, "B"), Edge(1.8, "C"), Edge(1.4, 'F'), Edge(1.6, "H")],
#     "F": [Edge(2.1, "C"), Edge(2.7, "D"), Edge(1.4, "E"), Edge(1.3, "G"), Edge(1.2, "H")],
#     "G": [Edge(2.4, "D"), Edge(1.3, "F"), Edge(1.5, "H")],
#     "H": [Edge(1.6, "E"), Edge(1.2, "F"), Edge(1.5, "G")],
# }
#0/1 Knapsack (Classic Beginner DP)
#_____________________________knapsack problems_______________________________________ 
P = [0,1,2,5,6]
Wt = [0,2,3,4,5]
m = 8 
n = 4
K = [[ 0 for j in range(m+1)]for i in range(n+1)]

for i in range(n+1):
    for w in range(m+1):
        if i == w == 0:
                K[i][w] = 0
        elif Wt[i]<=w:
            K[i][w] = max(P[i]+K[i-1][w-Wt[i]],K[i-1][w])
        else:
            K[i][w] =  K[i-1][w]
       


for i in K:
    print(i)
    
    
    
###########################################################################################
#                               Topological sort 
from collections import deque

def topological_sort_kahn(graph):
    """
    Performs a topological sort on a Directed Acyclic Graph (DAG) 
    using Kahn's Algorithm (In-degree method), based on the provided steps.

    Args:
        graph (dict): A dictionary representing the graph where keys are vertices
                      and values are lists of adjacent vertices (neighbors).
                      Example: {0: [1, 2], 1: [3], 2: [3], 3: []}

    Returns:
        list: A topologically sorted list of vertices, or an empty list if a cycle is detected.
    """
    
    # 1. Store each vertex's In-Degree in an array D
    # Initialize in-degree for all vertices to 0.
    in_degree = {u: 0 for u in graph}
    
    # Calculate actual in-degrees
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
            
    # --- Initialization ---
    
    # 2. Initialize queue with all "in-degree=0" vertices
    queue = deque()
    for u in graph:
        if in_degree[u] == 0:
            queue.append(u)
            
    topological_order = []
    
    # 3. While there are vertices remaining in the queue
    while queue:
        # (a) Dequeue and output a vertex
        u = queue.popleft()
        topological_order.append(u)
        
        # Iterate over neighbors v
        for v in graph[u]:
            # (b) Reduce In-Degree of all vertices adjacent to it by 1
            in_degree[v] -= 1
            
            # (c) Enqueue any of these vertices whose In-Degree became zero
            if in_degree[v] == 0:
                queue.append(v)
                
    # --- Cycle Detection ---
    
    # 4. If all vertices are output then success, otherwise there is a cycle.
    if len(topological_order) == len(graph):
        return topological_order
    else:
        # A cycle exists if the number of sorted vertices is less than the total number of vertices.
        # Note: Depending on requirements, you might return None, an error message, or the partial sort.
        # Returning an empty list here to signify failure/cycle detection.
        print("Error: The graph contains a cycle. Topological sort is not possible.")
        return []

# --- Example Usage ---

# Example DAG (Directed Acyclic Graph): 
# A -> C, B -> C, B -> D, C -> E, D -> E
# Vertices: 5 (A, B, C, D, E)
# In-degrees: A:0, B:0, C:2, D:1, E:2
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['E'],
    'E': []
}

sorted_list = topological_sort_kahn(graph)
print(f"\nTopological Sort Order: {sorted_list}")

# Example Graph with a Cycle (for step 4 verification)
# # A -> B -> C -> A
# cycle_graph = {
#     1: [2],
#     2: [3],
#     3: [1]
# }

# sorted_list_cycle = topological_sort_kahn(cycle_graph)
# print(f"\nTopological Sort Order (Cycle Test): {sorted_list_cycle}")

#######################################################################################
#__________________________________________Bubble Sort_________________________________#
l = [9,8,7,6,5,4,3,2,1]
def Bubble_Sort(l):
    n = len(l)
    for i in range(n):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l
print("Bubble_Sort")
print(Bubble_Sort(l))

#############################################################
#__________________________________________Insertion Sort_________________________________#
l_insertion = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def Insertion_Sort(l):
    # Traverse from the second element (index 1) up to the end
    for i in range(1, len(l)):
        
        key = l[i]  # The element to be inserted
        j = i - 1   # Start comparing with the element just before 'key'
        
        # Move elements of the sorted part (l[0..i-1]) that are greater than key
        # to one position ahead of their current position
        while j >= 0 and key < l[j]:
            l[j + 1] = l[j]
            j -= 1
            
        # Place the key in its correct position
        l[j + 1] = key
        
    return l

print("\nSorting (Insertion Sort)")
print(Insertion_Sort(l_insertion))
#############################################################
#__________________________________________Merge Sort_________________________________#
l_merge = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def Merge_Sort(l):
    if len(l) > 1:
        
        mid = len(l) // 2  # Find the middle point
        L = l[:mid]        # Divide the elements into two halves
        R = l[mid:]
        
        # Recursively sort the first and second halves
        Merge_Sort(L)
        Merge_Sort(R)
        
        i = j = k = 0
        
        # Merge the two sorted halves (L and R) back into l[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                l[k] = L[i]
                i += 1
            else:
                l[k] = R[j]
                j += 1
            k += 1
        
        # Copy the remaining elements of L[], if any
        while i < len(L):
            l[k] = L[i]
            i += 1
            k += 1
            
        # Copy the remaining elements of R[], if any
        while j < len(R):
            l[k] = R[j]
            j += 1
            k += 1
            
    return l

print("\nSorting (Merge Sort)")
print(Merge_Sort(l_merge))
#######################################################################
#__________________________________________Quick Sort_________________________________#
l_quick = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def Quick_Sort(l):
    if len(l) <= 1:
        return l
    else:
        # Choose the first element as the pivot for simplicity
        pivot = l[0] 
        
        # Partition the list into three parts: less than pivot, equal to pivot, greater than pivot
        less = [x for x in l[1:] if x <= pivot]
        greater = [x for x in l[1:] if x > pivot]
        
        # Recursively sort the partitions and combine the result
        return Quick_Sort(less) + [pivot] + Quick_Sort(greater)

print("\nSorting (Quick Sort)")
print(Quick_Sort(l_quick))
##############################################################################

# ______________________Bucket sort_________________________#
def bucketsort(l):
    
    bucket = [[]for i in range(10)]
    
    for i in l:
        bucket[i].append(i)
    
    out = []
    for i in bucket:
        for j in i :
            out.append(j)
    
    return out 
print("__________bucketsort_________")
print(bucketsort(l))

################################################################################
#__________________________________radix_sort_____________________________#
def counting_sort(arr, place):
    size = len(arr)
    output = [0] * size       # temporary array
    count = [0] * 10          # digits 0–9

    # Count the occurrences of each digit
    for num in arr:
        digit = (num // place) % 10
        count[digit] += 1

    # Convert count[i] to actual positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array (stable)
    for i in range(size - 1, -1, -1):
        digit = (arr[i] // place) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    # Copy output back into original array
    for i in range(size):
        arr[i] = output[i]


def radix_sort(arr):
    # Find the maximum number to know number of digits
    max_num = max(arr)

    place = 1
    # Apply counting sort for each digit (units, tens, hundreds...)
    while max_num // place > 0:
        counting_sort(arr, place)
        place *= 10


# Example usage:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Sorted array:", arr)
