

## Huffman Tree Node
class Node:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.right = None
        self.left = None

    ## overloading comparison operator for min heap
    def __lt__(self, other):
        return self.freq < other.freq;



## Huffman Tree constructor for serialization
class TreeConstructor:
    def __init__(self, root:Node):
        self.root = root
        self.preorder_list = []
        self.inorder_list = []

    def preorder(self, root:Node):
        if root == None:
            return None
        self.preorder_list.append(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root:Node):
        if root == None:
            return None
        self.inorder(root.left)
        self.inorder_list.append(root.data)
        self.inorder(root.right)

    def initialize(self):
        self.preorder(self.root)
        self.inorder(self.root)

    def get_preorder(self)->[]:
        return self.preorder_list
    
    def get_inorder(self)->[]:
        return self.inorder_list
    
    # def construct(self, pre_start:int, pre_end:int, in_start:int, in_end:int, map:dict)->Node:
    #     if pre_start > pre_end or in_start > in_end:
    #         return None
    #     root = Node(self.preorder_list[pre_start], 0)
    #     inorder_index = map[self.preorder_list[pre_start]]
    #     left_subtree_size = inorder_index - pre_start

    #     root.left = self.construct(pre_start+1, pre_start+left_subtree_size, in_start, inorder_index-1, map)
    #     root.right = self.construct(pre_start+left_subtree_size+1, pre_end, inorder_index+1, in_end, map)
    #     return root


    # def construct_tree(self)->Node:
    #     map = {}
    #     for i in range(len(self.inorder_list)):
    #         map[self.inorder_list[i]] = i
    #     return self.construct(0, len(self.preorder_list)-1, 0, len(self.inorder_list)-1, map)