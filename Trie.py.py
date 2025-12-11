#####################################################################
#             Trie                                           #
#####################################################################

class  TrieNode():
    def __init__(self):
        self.childnode = {
            'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None,
            'g': None, 'h': None, 'i': None, 'j': None, 'k': None, 'l': None,
            'm': None, 'n': None, 'o': None, 'p': None, 'q': None, 'r': None,
            's': None, 't': None, 'u': None, 'v': None, 'w': None, 'x': None,
            'y': None, 'z': None
                          }
        self.is_word = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        temp = self.root 
        for char in  word:
            if temp.childnode[char] is None:
                temp.childnode[char] = TrieNode()
            temp = temp.childnode[char]
        temp.is_word = True
    
    def search(self,word):
        temp = self.root
        for char in word :
            # if char not in temp.childnode:
            if temp.childnode[char] is None:
                return False
            temp =  temp.childnode[char]
        return temp.is_word
    def delete(self,word):
                temp = self.root
                for char in word :
                    # if char not in temp.childnode:
                    if temp.childnode[char] is None:
                        return 
                    temp =  temp.childnode[char]
                temp.is_word = False

# Sample Usage 
trie = Trie() 
# Insert words into the trie 
trie.insert("apple") 
trie.insert("app") 
trie.insert("apricot") 
trie.insert("banana") 
# Search for words in the trie 
print(trie.search("apple"))    
print(trie.search("app"))       
 # Output: True 
# Output: True 
print(trie.search("apricot"))   # Output: True 
print(trie.search("banana"))    # Output: True 
print(trie.search("orange"))    # Output: False 
trie.delete("app") 
print(trie.search("app"))       
# Grading Criteria 
# Output: False 
        
    
