##########################################
#_______________DSA______________________#
##########################################

## Node class :
class Node:
 
    def __init__(self,data = None,node_next = None, prev_node = None):       
        self.data = data
        self.next = node_next
        self.prev = prev_node 
        
## Linkedlist class :
class LL:
    
    def __init__(self,head = None):
        self.head = head
        
#   Adding the node to the linkedist 

   # insert to the start  
    def inserting_new_node(self,data):       
        # 1st create a new node 
        new_node = Node(data)       
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    # Insert a node after a given node 
    def insert_after_given_node(self,given_node,new_value):
        temp = self.head
        while(temp):
            if temp.data == given_node:
                new_node = Node(new_value)
                new_node.next = temp.next
                new_node.prev = temp
                if temp.next :
                    temp.next.prev  = new_node
                temp.next = new_node
                return
            temp = temp.next    

    # Insert a node at the end 
    def insert_at_the_end(self,value):
        
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last =  last.next
        last.next = new_node
        new_node.prev = last
        
#   printing linkedlist
    def printing_linkedlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

#   def backword printing 
    def backword_prinitng(self):
        temp = self.head
        while temp.next:
            temp =  temp.next
        while temp:
            print(temp.data)
            temp = temp.prev

#   counting the lenght of linkedlist 
    def counting_lenght(self):
        temp = self.head
        count = 0 
        while(temp):
            count+=1
            temp = temp.next
        return count

#   To get next node of linkedlist
    def next_node_in_linkedlist(self,node_value):
        temp = self.head
        while(temp):
            if temp.data == node_value:
                return temp.next.data
            temp = temp.next
        return None

#   Searching in linkedlist
    def search(self,value):
        temp = self.head
        find = False
        while(temp):
            if temp.data == value:
                find = True
                return find 
            temp = temp.next
        return find

            
Linkedlist = LL()
print("____________START the linkedlist classes_______________")
print()

print("________________Add the node at start _____________")

# value = int(input("How many nodes you waanna add to the start : "))
# for i in range(value):
#     node = int(input("Enter the node value to add it to the start : "))
#     Linkedlist.inserting_new_node(node)
    
# Linkedlist.inserting_new_node(15)
# Linkedlist.inserting_new_node(10)

# print("________________Printing the linkedlist ____________")
# Linkedlist.printing_linkedlist()

# print("________________Next node to given node _____________")
# next__ = int(input("Enter the value of node to find the next node value : "))
# print(Linkedlist.next_node_in_linkedlist(next__))

# # print(Linkedlist.next_node_in_linkedlist(15))

# print("________________Counting the lenght ___________________")
# print(Linkedlist.counting_lenght())


# print("________________Inserting after given Node _____________")
# Linkedlist.insert_after_given_node(4,5)

# print("________________Backward traversal ______________________")
# Linkedlist.backword_prinitng()

# print("________ Printing the linkedlist ________-")
# Linkedlist.printing_linkedlist()

value = int(input("How many nodes you waanna add to the linkedlist : "))
for i in range(value):
    node = int(input("Enter the node value to add it to the liskedlist : "))
    Linkedlist.insert_at_the_end(node)

Linkedlist.printing_linkedlist()


print("_______________Searching from linkedlist __________________")
print(Linkedlist.search(6)) 
 