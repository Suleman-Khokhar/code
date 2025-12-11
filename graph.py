

########################################################################3
class Graph():
    def __init__(self,no_nodes):
        self.graph=[]
        for i in range(no_nodes):
            L=[]
            for j in range(no_nodes):
                L.append(0)
            self.graph.append(L)
    def add_edge(self,node1,node2):
        self.graph[node1][node2]=1
        self.graph[node2][node1]=1
        
    def remove_edge(self,node1,node2):
        self.graph[node1][node2]=0
        self.graph[node2][node1]=0
        
    def add_vertex(self):
        L=[]
        for j in range(len(self.graph)):
            L.append(0)
        self.graph.append(L)
        for i in self.graph:
            i.append(0)
    # def remove_vertex(self,node):
    #     self.graph.pop(node)
    #     for i in self.graph:
    #         i.pop(node)
        
        
print("ADJ_matrix")                      

g=Graph(4)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(0,1)
g.add_edge(0,3)
# g.remove_vertex(3)
# g.remove_vertex(3)
# g.add_vertex()
# g.remove_edge(2,3)
for i in g.graph:
    print(i)
    
    
#######################################################
class Graph():
    def __init__(self,node_nodes):
        self.nodes=node_nodes
        self.graph=[[] for i in range(self.nodes)]
        
    def add_edge(self,node1,node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)
    
    def remove_edge(self,node1,node2):
        self.graph[node1].remove(node2)
        self.graph[node2].remove(node1)
        
    def add_vertex(self):
        self.graph.append([])
    
    # def remove_vertex(self,node):
    #     for i in self.graph:
    #         if node in i:
    #             i.remove(node)
    #     if node!=self.graph[-1]:       
    #         for i in range(len(self.graph)):
    #             for j in range(len(self.graph[i])):
    #                 if self.graph[i][j]!=0:
    #                     self.graph[i][j]-=1
                    
    #     self.graph.pop(node)
                    
  
  
print("ADJ_list")                      
g=Graph(6)
g.add_edge(0,4)
g.add_edge(0,3)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(2,5)
g.add_edge(5,1)

for i in g.graph:
    print(i)
# g.remove_vertex(5)
for i in g.graph:
    print(i)
#############################################################
class Graph():
    def __init__(self,no_nodes,nature):
        self.nature = nature
        self.no=no_nodes
        self.graph={i:[] for i in range(self.no)}
        
    def add_edge(self,node1,node2):
        
        if self.nature == "directed":
         self.graph[node1].append(node2)
        else:   
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
            
    def remove_edge(self,node1,node2):
        if self.nature == "directed":
            self.graph[node1].remove(node2)      
        else:
            self.graph[node1].remove(node2)
            self.graph[node2].remove(node1)
            
    def add_vertex(self):
        self.graph[len(self.graph)]=[]
        
    # def remove_vertex(self,node):
    #     for i in self.graph:
    #         if node in self.graph[i]:
    #             self.graph[i].remove(node)

    #     pass

print("ADJ_dict")                      

g=Graph(6,"directed")
# g.add_edge()
g.add_edge(2,4)
g.add_edge(0,5)
g.remove_edge(0,5)
g.add_vertex()
print(g.graph)
#######################################################################333
# Roll numbers : 
# Suleman Khokhar 281152801
# Harris Parvez 281133450


class Graph:

    '''Should initialize the adjacency matrix and
    store number of nodes and if the graph is directed or not.'''

    def __init__(self, num_of_nodes, directed=True):
        self.num_of_nodes = num_of_nodes+1
        self.directed = directed
        self.graph  = [[0 for j in range(self.num_of_nodes)] for i in range(self.num_of_nodes)]
    
    #should add an edge between node1 and node2
    def add_edge(self, node1, node2, weight=1):
        if 0<=node1 < self.num_of_nodes and 0<=node2 < self.num_of_nodes:
            self.graph[node1][node2] = weight
            if  not self.directed :
                self.graph[node2][node1] = weight
        # else:
        #     print("invalid")

    #should print
    def print_adj_matrix(self):
        for i in self.graph:
            for j in i:
                print(f"{j} ",end="")
            print()
    #should remove an edge between node1 and node2
    def remove_edge(self, node1, node2, weight=1):
        if 0<=node1 < self.num_of_nodes and 0<=node2 < self.num_of_nodes:
            self.graph[node1][node2] = 0
            if  not self.directed :
                self.graph[node2][node1] = 0

    #should add a new node
    def addVertex(self, node):
        self.num_of_nodes+=1
        for row in self.graph:
            row.append(0)
        self.graph.append([0]*self.num_of_nodes)

    #should remove the node as well all edges incident with it.
    def removeVertex(self, node):
            if 0 <= node < self.num_of_nodes:
                self.graph.pop(node)
                for row in self.graph:
                    row.pop(node)
                self.num_of_nodes -= 1

    def printing(self):
        for i in self.graph:
            for j in i:
                print(f"{j} ",end="")
            print()
    def bfs(self, start_node):
        visited = []
        queue = []

        # Start from the given node
        visited.append(start_node)
        queue.append(start_node)

        while queue:
            # Pop the first element to simulate a queue (FIFO)
            current = queue.pop(0)

            # Visit all adjacent nodes
            for neighbor in range(self.num_of_nodes):
                if self.graph[current][neighbor] != 0 and neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

        return visited

        # DFS using stack (iterative)
    def dfs_stack(self, start_node):
        visited = []
        stack = [start_node]

        while stack:
            current = stack.pop()          # pop last (LIFO)

            if current not in visited:
                visited.append(current)

                # Push neighbors in reverse order to keep order correct
                for neighbor in range(self.num_of_nodes - 1, -1, -1):
                    if self.graph[current][neighbor] != 0 and neighbor not in visited:
                        stack.append(neighbor)

        return visited
    # DFS using recursion
    def dfs_recursive(self, start_node):
        visited = []
        self._dfs_helper(start_node, visited)
        return visited

    def _dfs_helper(self, node, visited):
        visited.append(node)

        for neighbor in range(self.num_of_nodes):
            if self.graph[node][neighbor] != 0 and neighbor not in visited:
                self._dfs_helper(neighbor, visited)


    def path_exists(self, node1, node2):
        '''Return True if there is a path from node1 to node2, False otherwise.'''

        if node1 < 0 or node1 >= self.num_of_nodes or node2 < 0 or node2 >= self.num_of_nodes:
            print("Invalid nodes.")
            return False
        visited = []
        queue = []
        visited.append(node1)
        queue.append(node1)
        while queue:
            current = queue.pop(0)
            if current == node2:
                return True
            for neighbor in range(self.num_of_nodes):
                if self.graph[current][neighbor] != 0 and neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
        return False


# number_of_egdes = int(input("Enter the number of edges : "))
# direct = bool(input("Enter type of graph : "))
graph = Graph(8,False)
# graph = Graph(number_of_egdes,direct)


# graph.printing()

print("_______________adding  edgdes _____________________")
graph.add_edge(0,1,3)
graph.add_edge(0,3,2)
graph.add_edge(0,8,4)
graph.add_edge(1,7,4)
graph.add_edge(2,7,2)
graph.add_edge(2,3,6)
graph.add_edge(2,5,1)
graph.add_edge(3,2,6)
graph.add_edge(3,4,1)
graph.add_edge(3,0,2)
graph.add_edge(4,3,1)
graph.add_edge(4,8,8)
graph.add_edge(5,2,1)
graph.add_edge(5,6,8)
graph.add_edge(6,5,8)
graph.add_edge(7,2,2)
graph.add_edge(7,1,4)
graph.add_edge(8,0,4)
graph.add_edge(8,4,8)

print("_______________printing edgdes _____________________")

graph.printing()

print("_______________________________________________________________________")

# # graph.addVertex(9)
# print("_______________printing edgdes _____________________")

# graph.printing()

# print("_______________________________________________________________________")
# print()
# print("Removing egde ")
# graph.removeVertex(3)

# print("_______________printing edgdes _____________________")

# graph.printing()

# print("_______________________________________________________________________")
#______________________________________________________________________________________________________________________________________

result = graph.bfs(0)
print("__________________________________________________________")
print(result)
print(graph.path_exists(4,3))

print("DFS (Stack):", graph.dfs_stack(0))
print("DFS (Recursive):", graph.dfs_recursive(0))
