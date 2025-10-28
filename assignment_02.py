 ## Suleman Khokhar 
 
# Importing both classes
import re
from AVL_tree import AVL
from binary_tree import BST

# Optional: to use your essay text
with open("informative_essay_AI.txt", "r") as file:
    essay_text = file.read()






# with open("informative_essay_AI.txt", "r") as file:

#     text = file.read()

    

cleaned_text = re.sub(r'[^\w\s]', '', essay_text)



cleaned_text=cleaned_text.strip().split()



L=[i.lower() for i in cleaned_text]



for I in L:

    AVL.insert(I)

    BST.insert(I)

    

def query_frequency(word):

    a=AVL.search(word)

    b=BST.search(word)

    if a is None:
        return 0
    return a.value

a = AVL.inorder()
with open("out.txt","w") as file :
    for i in a :
        file.write(f"{i[0],i[1]}")

        

    

    

# cleaned_text = re.sub(r'\p{Punct}', '', text, flags=re.UNICODE)

# print(cleaned_text)














