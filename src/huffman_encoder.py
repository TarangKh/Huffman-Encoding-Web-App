import heapq
from collections import defaultdict
from src.tree_constructor import Node
from src.tree_constructor import TreeConstructor
import pickle
import os
import src.utils


## utility function to store characters along with their huffman code in hash table
encoded_map = {}
def storeCode(root:Node, s:str):
    if root.left == None and root.right == None:
        encoded_map[root.data] = s
    else:
        storeCode(root.left, s+"0")
        storeCode(root.right, s+"1")



class HuffmanEncoder:
    def __init__(self):
        self.encodedMap = {}                # to map each character it's huffman value
        self.freqMap = defaultdict(int)     # to map each character with it's frequency from input
        self.rootnode = None 
        self.minHeap = []        
    
    ## utility function to print characters along with their huffman codes
    def printCode(self):
        for char in self.encodedMap.items():
            print(char[0],":",char[1])
    
    ## utility function to print characters along with their frequency in input data
    def printFrequency(self):
        for char in self.freqMap.items():
            print(char[0],":",char[1])


    ## function to build Huffman tree and store it into minheap
    def createHuffmanTree(self, s:str):
        self.freqMap.clear()
        self.initialize(s)
        for key in self.freqMap:
            new_node = Node(key, self.freqMap[key])
            self.minHeap.append(new_node)
        heapq.heapify(self.minHeap)

        while len(self.minHeap) != 1:
            left = heapq.heappop(self.minHeap)
            right = heapq.heappop(self.minHeap)
            top = Node(left.data + right.data, left.freq + right.freq)
            top.left = left
            top.right = right
            heapq.heappush(self.minHeap, top)
        
        self.rootnode = self.minHeap[0]
        global encoded_map
        self.encodedMap.clear()
        encoded_map.clear()
        storeCode(self.rootnode, "")
        self.encodedMap = encoded_map

    ## function to enocde the given string and return encoded string
    def encode(self, s:str)->str:
        self.createHuffmanTree(s)
        encodedString = ""
        for char in s:
            encodedString += self.encodedMap[char]
        return encodedString


    # utility function to initialize the frequency map
    def initialize(self, s:str):
        for char in s:
            self.freqMap[char] += 1;
    

    # function to get the root node of Huffman Tree
    def getRoot(self)->Node:
        return self.rootnode

    # function to get frequency of characters in list format
    def getFrequency(self)->[]:
        freq = []
        for char in self.freqMap.items():
            freq.append((char[0], char[1]))
        return freq
    
    # function to get codes of characters in list format
    def getCode(self)->[]:
        code = []
        for char in self.encodedMap.items():
            code.append(char)
        return code




## class to decode a Huffman string
class HuffmanDecoder:
    def __init__(self):
        pass
    
    def decode(self, root:Node, s:str)->str:
        decodedString = ""
        curr = root
        n = len(s)
        for i in range(n):
            if s[i] == "0":
                curr = curr.left
            else:
                curr = curr.right
            
            ## reached the leaf node
            if curr.left == None and curr.right == None:
                decodedString += curr.data
                curr = root
            
        return decodedString
    
    def generate(self, pre, p_start, p_end, ino, in_start, in_end, map)->Node:
        if (p_start  > p_end or in_start > in_end):
            return None
        root = Node(pre[p_start], 0)
        in_index = map[root.data]
        left_subtree_size = in_index - in_start
        
        root.left = self.generate(pre, p_start+1, p_end+left_subtree_size, ino, in_start, in_index-1, map)
        root.right = self.generate(pre, p_start+left_subtree_size+1, p_end, ino, in_index+1,in_end, map)
        return root


    def generate_tree(self, pre:[], ino:[])->Node:
        map = {}
        for i in range(len(ino)):
            map[ino[i]] = i
        
        return self.generate(pre, 0, len(pre)-1, ino, 0, len(ino)-1, map)




def inorder(root:Node):
    if root == None:
        return None
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def preorder(root:Node):
    if root == None:
        return None
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


def serialize(root:Node):
    construct = TreeConstructor(root)
    construct.initialize()
    counter = 0
    with open(r"counter.txt", "r") as file:
        count = int(file.readline())
        counter = count+1
    with open(r"counter.txt", "w") as file:
        file.write(str(counter))

    path = os.path.join("Files", "file"+str(counter)+".pkl")
    with open(path, "wb") as file:
        pickle.dump(construct, file)
    return path


if __name__ == "__main__":
    s = input(">>> ")
    encoder = HuffmanEncoder()
    encoded = encoder.encode(s)
    print(encoded)

    root = encoder.getRoot()

    file_path = serialize(root)
    print(file_path)
    inorder(root)
    print()
    preorder(root)
    print()
    zip_path = utils.make_rar(file_path)
    print(zip_path)
    # ino = construct.get_inorder()
    # pre = construct.get_preorder()
    # print(ino)
    # print(pre)
    # inorder(root)
    # print()
    # preorder(root)
    # print()
    root = None
    with open(file_path, "rb") as file:
        obj = pickle.load(file)
        preorder = obj.get_preorder()
        inorder = obj.get_inorder()
        print(inorder)
        print(preorder)
        decoder = HuffmanDecoder()
        root = decoder.generate_tree(preorder, inorder)
        print()
        
    # preorder(root)
    # print()
    # inorder(root)
    # print()
    # print(type(root))

    
 

    

    
    # with open("Files/TreeConstruct.pkl", "wb") as file:
    #     pickle.dump(construct, file)
    
    # with open("Files/TreeConstruct.pkl", "rb") as file:
    #     obj = pickle.load(file)
    #     root = obj.construct_tree()
    #     dec_str = decoder.decode(root, enc_str)
    #     print(dec_str)


    # inorder(root)
    # print()
    # construct = TreeConstructor(root)
    # construct.preorder(construct.root)
    # print()
    # construct.inorder(construct.root)
    

    # print("\n"*3)
    # data = "abracadabra bom bom"
    # encoder = HuffmanEncoder()
    # enc_str = encoder.encode(data)
    # print(enc_str)
    # freq = encoder.getFrequency()
    # print(freq)
    # code = encoder.getCode()
    # print(code)
    # root = encoder.getRoot()
    # decoder = HuffmanDecoder()
    # dec_str = decoder.decode(root, enc_str)
    # print(dec_str)



    