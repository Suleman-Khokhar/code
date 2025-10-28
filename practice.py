
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
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node    



#   delete from head of dll 

    def delete_from_head(self):
        if self.head == None:
            return

        # if self.head != None:
        #     temp = self.head 

        elif self.head.next != None:
            self.head = self.head.next
            self.head.prev = None
            
        elif self.head.next == None:
            self.head =None
            self.tail = None


#   Counting the lenght

    def counting_the_lenght(self):
        temp = self.head
        count = 0
        while(temp):
            count+=1
            temp = temp.next
        return count == 0

#   Priniting the stack 
    def priniting_the_dll(self):
        temp = self.head
        while(temp):
            print(temp.data,end=", ")
            temp = temp.next

class Stack:
    def __init__(self,stack=DLL()):
        self.stack=stack
        
    def push(self,data):
        self.stack.insert_at_head(data)
        
    def peek(self):
        if self.stack.head is None:
            return None
        return self.stack.head.data
    
    def pop(self):
        temp = self.stack.head.data
        self.stack.delete_from_head()
        return temp
    
    def printing(self):
        self.stack.priniting_the_dll()
    
    def is_empty(self):
        return self.stack.counting_the_lenght()
d = {"-": 1, "+": 1, "*": 2, "/": 2, "^": 3, "(": 0}


def infixed(expression):
    
        Outpt_stack = []
        Holding_stack = Stack()

        for i in expression:
            if isinstance(i, int):
                Outpt_stack.append(i)

            elif i in "({[":
                Holding_stack.push(i)

            elif i in "+-*/^":
                while not Holding_stack.is_empty():
                    top = Holding_stack.peek()
                    if top in d and d[top] >= d[i]:
                        Outpt_stack.append(Holding_stack.pop())
                    else:
                        break
                Holding_stack.push(i)

            elif i in ")}]":
                matching = {")": "(", "}": "{", "]": "["}
                while not Holding_stack.is_empty() and Holding_stack.peek() != matching[i]:
                    Outpt_stack.append(Holding_stack.pop())
                Holding_stack.pop()  # Pop the matching opening bracket

        while not Holding_stack.is_empty():
            Outpt_stack.append(Holding_stack.pop())

        return Outpt_stack

def  post_fix_execution(expression):                    
    new_stack = Stack()
    for i in expression:
        if isinstance(i,int):
            new_stack.push(i)
        else:
            result = 0
            if i in "/-+*^":
                num_1 = new_stack.pop()
                num_2 = new_stack.pop()
                if i == "+":
                    result = num_2+num_1
                elif i == "-":
                    result = num_2-num_1
                elif i == "/":
                    result = num_2/num_1
                elif i == "-":
                    result = num_2-num_1
                elif i == "*":
                    result = num_2*num_1
                elif i == "^":
                    result = num_2**num_1
                new_stack.push(result)
                return new_stack.peek()
                    
        
Holding_stack = Stack()        
Outpt_stack = Stack()
expression = str(input("Enter a expression : "))
lists=expression.split(" ")

finalexpression  = [int(i) if i.isnumeric() else i for i in lists]

# lists = []
# for i in expression:
#     if isinstance(i,int):
#         lists.append(int(i))
#     elif i in "/-+*^":
#         lists.append(i)
#     else:
#         continue

# post_fix_execution(expression)
# Outpt_stack.printing()

print(finalexpression)
expression = [1,"+",2,"+",3,"*",5,"-",1]
print(*infixed(finalexpression)) 
print(post_fix_execution(finalexpression))













