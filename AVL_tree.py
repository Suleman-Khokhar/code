
##         Simple AVL Tree Py file           ## 

class Node:
    def __init__(self,word = None,value = 1,balance = 0,left=None,right = None,parent = None):
        self.word = word
        self.value = value
        self.balance = balance
        self.left = left
        self.right = right
        self.parent = parent
        

class   AVL:

    def __init__(self,root=None):
        self.root = root
    
    def insert(self,word):        
        new_word = Node(word)
        if self.root == None:
            self.root = new_word
            self.root.value = 1        
        else:
            temp = self.root
            while(temp):
                if word < temp.word:
                    #     # Left side   
                    if temp.left == None:
                            temp.left = new_word
                            temp.left.parent = temp
                            # if 
                            break
                    else:
                            temp = temp.left
                elif word > temp.word:
                        # Right side                 
                    if temp.right == None:
                            temp.right = new_word
                            temp.right.parent = temp
                            break
                    else:
                            temp = temp.right
                else:
                    # Duplicate word
                        temp.value += 1
                        break
  
            while temp is not None:
                balance = self.balancing_value(temp) 
                # Left heavy
                if balance < -1:
                    if self.balancing_value(temp.left) <= 0:
                        self.LL_Rotation(temp)
                    else:
                        self.LR_Rotation(temp)
                # Right heavy
                elif balance > 1:
                    if self.balancing_value(temp.right) >= 0:
                        self.RR_Rotation(temp)
                    else:
                        self.RL_Rotation(temp)
                temp = temp.parent
  
                
               
                
    
    def height_value(self,node = None):
        if node is None:
                return 0
        return 1 + max(self.height_value(node.left),self.height_value(node.right))
    
    
    def balancing_value(self,node = None):
        return  ( self.height_value(node.right) - self.height_value(node.left))
    
    def demo(self,node=None):
        find = self.search_node(node)
        if find is None:
            return None
        else:
            return self.traveral_bottom_to_top_ll(find)
    # # def rotation_ll(self,)
            
    def traveral_bottom_to_top_ll(self, node=None):
        if node is None:
            return
        # Visit left subtree first
        self.traveral_bottom_to_top_ll(node.left)

        # print(node.word)
        # return self.balancing_value(node),node.word
        return self.balancing_value(node)
        
    
    def LL_Rotation(self,A = None):
        
                                #      A                      B
                                #     / \                   /   \
                                #    B   T3     -->        T1    A
                                #   / \                         / \
                                #  T1  T2                      T2  T3
                                        

        B = A.left      # Al 
        T2 = B.right    # Br
        
        ## Perform roatation
        B.right = A
        A.left = T2
        
        ## updating parent
        if T2 :
            T2.parent = A 
        B.parent = A.parent
        A.parent = B
        
        ##  B is root if 
        if B.parent is None:
            self.root = B
        ## grand father referrence update 
        else:
            if B.parent.left == A:
                B.parent.left = B
            else:
                B.parent.right = B
                
                    
        
    def RR_Rotation(self,A=None):
        B = A.right      # Ar
        T2 = B.left      # Bl
        
        ##    Perform Rotation 
        B.left = A
        A.right = T2
         
        ## Updating parent
        if T2 :
            T2.parent = A
        B.parent = A.parent
        A.parent = B
        
        ## If B is root if 
        if B.parent is None:
            self.root = B
        ## grandfather exisst so update its referrence 
        else:
            if B.parent.right == A:
                B.parent.right = B
            else:    
                B.parent.left = B
        

    def LR_Rotation(self, A=None):
       
        #     A                       A                     C
        #    / \                     / \                  /   \
        #   B   T4     --> (RR) -->  C   T4    --> (LL)  B     A
        #  / \                     / \                  / \   / \
        # T1  C                   B  T3                T1 T2 T3 T4
        #     / \                 / \
        #     T2 T3              T2 T3

        B = A.left
        C = B.right
        T2 = C.left
        T3 = C.right

        # Store original parent before any changes
        parent = A.parent

        # Step 1: Rotate left on B
        B.right = T2
        if T2:
            T2.parent = B
        C.left = B
        B.parent = C

        # Step 2: Rotate right on A
        A.left = T3
        if T3:
            T3.parent = A
        C.right = A
        A.parent = C

        # Step 3: Fix grandparent link
        C.parent = parent
        if parent is None:
            self.root = C
        else:
            if parent.left == A:
                parent.left = C
            else:
                parent.right = C


            
    def RL_Rotation(self, A=None):
        # """
        #     A                         A                        C
        #     / \                       / \                     /   \
        #     T1  B        --> (LL) -->  T1  C      --> (RR) --> A     B
        #     / \                       / \                 / \   / \
        #     C   T4                     T2  B              T1 T2 T3 T4
        #         / \                       / \
        #         T2 T3                     T3 T4
        # """

        B = A.right
        C = B.left
        T2 = C.left
        T3 = C.right

        # 🔹 Store original parent before any reassignments
        parent = A.parent

        # Step 1: Rotate right on B
        B.left = T3
        if T3:
            T3.parent = B
        C.right = B
        B.parent = C

        # Step 2: Rotate left on A
        A.right = T2
        if T2:
            T2.parent = A
        C.left = A
        A.parent = C

        # Step 3: Fix grandparent link
        C.parent = parent
        if parent is None:
            self.root = C
        else:
            if parent.right == A:
                parent.right = C
            else:
                parent.left = C


#   Delete node from the tree :
    def delete_node(self,node = None):
        find = self.search_node(node)
        if find is None:
            return False
        else:    
    ## _____________Cases__________________
        
        ## ______________ : 0 child case : ___________________
            parent_find = find.parent
            
            if find.left is None and find.right is None:
               if find is self.root :
                   self.root = None
                   self.root.parent = None
               elif find is parent_find.left:
                   parent_find.left = None
               else: #find is parent_find.right:
                   parent_find.right = None
               
               find.parent = None
               return True          
        
        ## ______________ : 1 child case :  ___________________
    
             # ______________________________________________________________________ #
            
            ## If No grandfather exist but right 1 child
             
                 ## Checking for Right side child only 
            
            elif find.left is None:
                child = find.right
                if find is self.root :
                    self.root = child
                    self.root.right = None
                    child.parent = None
                    self.root.parent = None
                    
                ## If grandfather exist but left 1 child 
            
                elif find is parent_find.left:
                    parent_find.left = child
                    child.parent = parent_find
 
                ## If grandfather exist but right 1 child 
                    
                else: # find is parent_find.right:
                    parent_find.right = child
                    child.parent = parent_find
                return True
                
                # ______________________________________________________________________ #
            
                ## If No grandfather exist but right 1 child

                     ## Checking for Right side child only 
            
            elif find.right is None:
                child = find.left
                if find is self.root :
                    self.root = child
                    self.root.left = None
                    child.parent = None
                    self.root.parent = None
                    
                ## If grandfather exist but left 1 child 
            
                elif find is parent_find.left:
                    parent_find.left = child
                    child.parent = parent_find
 
                ## If grandfather exist but right 1 child 
                    
                else: # find is parent_find.right:
                    parent_find.right = child
                    child.parent = parent_find
                return True
                    
        ## ______________ : 2 child case :  ___________________ ##
            
            elif find.left is not None and  find.right is not None:
                
                ### Finding the maximum value from the left sub tree 
                max_value = self.max_value(find.left)
                
                ## storing the parent of maximum value 
                max_vale_parent = max_value.parent
                
                ## Copying the max value in targeted node 
                find.word = max_value.word
                find.value = max_value.value
                
                ## Storing the child of max_value if its left child exist 
                max_value_child = max_value.left
                
                ## Deleting the node maximum value referrence
                if max_value is max_vale_parent.left:
                    max_vale_parent.left = max_value_child
                
                else: # max_value is max_vale_parent.right
                    max_vale_parent.right = max_value_child
                
                if max_value_child is not None:
                    max_value_child.parent =  max_vale_parent
                    return True
            else:
                return False     
              
        while temp is not None:
            balance = self.balancing_value(temp) 
            # Left heavy
            if balance < -1:
                if self.balancing_value(temp.left) <= 0:
                    self.LL_Rotation(temp)
                else:
                    self.LR_Rotation(temp)
            # Right heavy
            elif balance > 1:
                if self.balancing_value(temp.right) >= 0:
                    self.RR_Rotation(temp)
                else:
                    self.RL_Rotation(temp)
            temp = temp.parent

                    
#   Maximum node value in left sub tree :
    def max_value(self,node = None):
        if node.right is None:
            return node
        return self.max_value(node.right)

#   Minimum node value in right sub tree :
    def min_value(self,node = None):
        if node.left is None:
            return node
        return self.min_value(node.left)


#   Searching the node 
    def search_node(self,node = None):
        if node == self.root.word:
            return self.root
        else:
            temp = self.root
            while(temp):
                if node < temp.word:
                    if temp.left.word == node:
                        return temp.left
                    else:
                        temp = temp.left
                        
                elif  node > temp.word:
                    if temp.right.word == node:
                        return temp.right
                    else:
                        temp = temp.right
        return None    
    
    def inorderH(self, node, lists=None):
        if lists is None:
            lists = []
        if node is None:
            return lists
        self.inorderH(node.left, lists)
        lists.append(f"Key: {node.word}, Value: {node.value}")
        self.inorderH(node.right, lists)
        return lists

    def inorder(self):
        return self.inorderH(self.root)
                             
    
    # def inorderH(self,node):
    #     if node is None:
    #         return 
    #     self.inorderH(node.left)
    #     print(f"Key: {node.word} , Value: {node.value}")
    #     self.inorderH(node.right)
    
    # def inorder(self):
    #     self.inorderH(self.root)
       
# AVL_tree = AVL()
# AVL_tree.insert("100")
# AVL_tree.insert("110")
# AVL_tree.insert("90")
# AVL_tree.insert("120")
# print(AVL_tree.inorder())
# print(AVL_tree.height_value(AVL_tree.root))
# print("____________ Balancing values __________________") 
# print(AVL_tree.balancing_value(AVL_tree.root))
# print("_____________________-")
# AVL_tree.delete_node("90")  
# print(AVL_tree.inorder())
      
# AVL_tree.insert("cat")
# AVL_tree.insert("cat")
# AVL_tree.insert("bat")
# AVL_tree.insert("eat")

# AVL_tree.insert("fat")
        
# print(AVL_tree.traveral_bottom_to_top_ll(AVL_tree.root))
# print("_______demo ___________")
# print(AVL_tree.demo("bat"))        
# print(AVL_tree.demo("cat"))        
# print("_______________ LL Rotation ______________")
# AVL_tree.LL_Rotation(AVL_tree.root)
# AVL_tree.inorder()
# print("_______________ RR Rotation ______________")
# AVL_tree.RR_Rotation(AVL_tree.root)
# AVL_tree.inorder()
# print("_______________ RL Rotation ______________")
# AVL_tree.LR_Rotation(AVL_tree.root)
# AVL_tree.RL_Rotation(AVL_tree.root)






