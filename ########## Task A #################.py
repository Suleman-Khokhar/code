########## Task A #################
# Implementing Doubly link list #######

class Node:
    def __init__(self,data,prev=None,nex=None):
        self.data=data
        self.prev=prev
        self.next=nex

class Doubly_link_list:
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail=tail
        
    def insert_at_head(self,data):
        n=Node(data)
        if self.head==None:
            self.head=n
            self.tail=n
        else:
            n.next=self.head
            self.head.prev=n
            self.head=n
            
            
    def delete_from_head(self):
            if self.head==self.tail:
                self.head=None
                self.tail=None
            else:
                self.head=self.head.next
                self.head.prev=None
                
    
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print('None')
    
    
    
    def is_empty(self):
        return self.head==None
            
#################### Task B #####################
# Implementing Stack Class ######################

class Stack:
    def __init__(self,stack=Doubly_link_list()):
        self.stack=stack
        
    def push(self,data):
        self.stack.insert_at_head(data)
        
    def peek(self):
        if self.stack.is_empty():
            return None
        return self.stack.head.data
    
    def pop(self):
        if self.stack.is_empty():
            return None
        else:
            temp=self.stack.head
            self.stack.delete_from_head()
            return temp.data
        
    def is_empty(self):
        return self.stack.is_empty()
    
    def display(self):
        self.stack.display_forward()
        

L=["(",5,"+",3,"*",2,")","-",9]


                                                   # (5 + 3 * 2) - 9  ==> L=["(","+",3,"*",2,")","-",9]
d = {"-": 1, "+": 1, "*": 2, "/": 2, "^": 3, "(": 0}

def infix_to_postfix(L):
    out_list = []
    hol_stack = Stack()

    for token in L:
        if isinstance(token, int):
            out_list.append(token)

        elif token in "({[":
            hol_stack.push(token)

        elif token in "+-*/^":
            while not hol_stack.is_empty():
                top = hol_stack.peek()
                if top in d and d[top] >= d[token]:
                    out_list.append(hol_stack.pop())
                else:
                    break
            hol_stack.push(token)

        elif token in ")}]":
            matching = {")": "(", "}": "{", "]": "["}
            while not hol_stack.is_empty() and hol_stack.peek() != matching[token]:
                out_list.append(hol_stack.pop())
            hol_stack.pop()  # Pop the matching opening bracket

    while not hol_stack.is_empty():
        out_list.append(hol_stack.pop())

    return out_list

print(infix_to_postfix(L))