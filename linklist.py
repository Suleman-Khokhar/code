#""""""""""""""""""""""""""""""""""""""""""""""""""""

"               DSA practice                       "

#""""""""""""""""""""""""""""""""""""""""""""""""""""

#                 LINKLIST DETAILS 












"""So linklist is the linear collection of data elements .....
   .....These data elemets are called Node and they are pointing to other node next_node """
#                        ___     ___     ___
##              head--> |___|-->|___|-->|___|--x
#
#  Elements are data and next node 
#                                   __ Next 
#                                  |
#                             _____|_
#       NODE ==     Head  ---|___|___|----None                         _
#                              |
#                              |__Data



















# Example ::
##       _____________ Node class: ____________

"""
    The new created node has two parts Data and Next_node (address)......
        1.  so initally the data and next_node is none
                                                     """
class Node():
    def __init__(self,data = None,next_node = None):
        self.data = data
        self.next_node = next_node


##       _____________ linkedlist class: ____________

"""Linkedlist head is initally none . """

class Linkedlist():
    def __init__(self,head=None):
        self.head = head
        
        
        
        
        
        
        
        
        
# ____________Print the linkedlist ______________
      # only if the linkedlist is not empty 
    def print_linkedlist(self):
        temp = self.head
        while(temp):
            print(f" {temp}  -->" ,end="")
            temp = temp.next_node
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
# __________Calculating the lenght:____________

    def size(self):
        
        current = self.head  
        count = 0
        while (current):
            count+=1
            current=current.next_node
        return count
























# __________Inserting a new node on the head of linkedlist______________
        """
        Head -> [10] -> [20] -> [30] -> None
        
    NewNode                     ------[25] -->
                                |    ^     |
                                |    |     |
                                v    |     ^
        Head -> [5] -> [10] -> [20] --    [30] -> None
        
        Head -> [5] -> [10] -> [20] -> [30] -> None
        """








    def insert_at_head(self,data):
     # First of all we have to design a new node 
        new_node = Node(data)
     # secondly we have to head the direction of new node head 
        new_node.next_node = self.head
     # now change the direction of head 
        self.head = new_node
        
# Get Next node in a linkdlist 
    # corresponding data 
    def  get_next_node(self,node):
        return node.next_node.data

#   ___________Inserting a node in linkedlist___________

    def insert_begin(self,new_data):
        new_node = Node(new_data)
        new_data.next = self.head
        self.head = new_node

#   ___________Inserting a node AFTER given node in linkedlist___________







         
        
# ______Create and append node in a linked  list________ 

# obj for llist class 
llist = Linkedlist()

# llist head initalizing 
llist.head = Node(2)

# s containing data 3
s=  Node(3)

# t containing data 4
t=  Node(4)

llist.head.next_node = s
s.next_node = t









# ______________ Calling function ________________
     
llist.Display()
print(llist.size)
llist.insert_at_head(6)

         