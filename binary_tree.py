
##         Simple Binary Tree Py file           ## 

class Node:
    def __init__(self,word = None,value = 1,left=None,right = None,parent = None):
        self.word = word
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

class BST:

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
            
             
                 ## Checking for Right side child only 
            
            elif find.left is None:
               
                child = find.right
            ## If No grandfather exist but right 1 child
               # is root 
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

Binary_Search_Tree = BST()
Binary_Search_Tree.insert("8")
Binary_Search_Tree.insert("4")
Binary_Search_Tree.insert("9")
Binary_Search_Tree.insert("3")
Binary_Search_Tree.insert("5")
Binary_Search_Tree.insert("6")


# print(Binary_Search_Tree.inorder())
# print(Binary_Search_Tree.max_value(Binary_Search_Tree.root).word)
# print(Binary_Search_Tree.max_value(Binary_Search_Tree.search_node("4")).word)
Binary_Search_Tree.delete_node("8")
# print("_____________ After Deleting the Node _______________")
# print(Binary_Search_Tree.inorder())
        
        