#####################################################################
#________________________________ASSIGNMENT 01______________________#
#####################################################################

# Part A – Doubly Linked List

class Node:
    def __init__(self, data = None, prev = None, next_node = None):
        self.data = data
        self.prev = prev
        self.next = next_node

class DLL:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    
#   insert at head(data)

    def insert_at_head(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.head
            self.head.prev = new_node
            self.head = new_node    

#   delete from head of dll 

    def delete_from_head(self):
        if self.head == None:
            return 
        elif self.head.next != None:
            self.head = self.head.next
            self.head.next.prev = None

#   Counting the lenght

    def counting_the_lenght(self):
        temp = self.head
        count = 0
        while(temp):
            count+=1
            temp = temp.next
        return count

#   Priniting the stack 
    def priniting_the_dll(self):
        temp = self.head
        while(temp):
            print(temp.data,end=", ")
            temp = temp.next

class Stack:
    def __init__(self,head = None, tail = None):
        self.head = head
        self.tail = tail
    
    def push(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.head
            self.head.prev = new_node
            self.head = new_node    
    
    def pop(self):
        if self.head == None:
            return 
        elif self.head.next != None:
            self.head = self.head.next
            self.head.next.prev = None
    
    def is_empty(self):
        temp = self.head
        count = 0
        while(temp):
            count+=1
            temp = temp.next
        return count == 0
 
        
            
Doubly_Linked_List = DLL()
Doubly_Linked_List.insert_at_head(5)
Doubly_Linked_List.insert_at_head(4)
Doubly_Linked_List.insert_at_head(3)
Doubly_Linked_List.insert_at_head(2)
Doubly_Linked_List.insert_at_head(1)
Doubly_Linked_List.priniting_the_dll()  
print()  
print("___________Deleting from head _____________")
print()  

Doubly_Linked_List.delete_from_head()
Doubly_Linked_List.priniting_the_dll()    

        
        
        
        