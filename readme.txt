---------------------------------- INSTRUCTIONS -------------------------------------

In order to access the decoded message follow the steps geven below

1) import src\tree_constructor.py in your python file 
2) import pickle
3) load the file(x).pkl located in Files folder in an object
4) use the get_preorder() method to access the preorder traversal of Huffman Encoded Tree
5) use the get_inorder() method to access the preorder traversal of Huffman Encoded Tree

6) construct the Huffman Tree from the inorder and preorder traversals
7) follow the rules to encode the message ->

8) start from the root node of the tree
9) go left if the current digit of encoded message is 0
10) go right is the current digit of encoded message is 1
11) stop when you reach leaf node and note the character
12) start from step 8 again.

----------------------------------- ----BYE -------------------------------------------