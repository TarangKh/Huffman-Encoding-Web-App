import heapq
from collections import defaultdict
from src.tree_constructor import Node
from src.tree_constructor import TreeConstructor
import pickle
import os
from src import utils

    

class HuffmanEncoder:
    def __init__(self):
        self.encodedMap = {}                # to map each character it's huffman value
        self.freqMap = defaultdict(int)     # to map each character with it's frequency 
        self.rootnode = None 
        self.minHeap = []        
        self.total_chars = 0


    ## utility function to store characters along with their huffman code in hash table
    def storeCode(self, root:Node, s:str):
        if root.left == None and root.right == None:
            self.encodedMap[root.data] = s
        else:
            self.storeCode(root.left, s+"0")
            self.storeCode(root.right, s+"1")


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
        self.encodedMap.clear()
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
        self.encodedMap.clear()
        self.storeCode(self.rootnode, "")
    ## function to enocde the given string and return encoded string
    def encode(self, s:str)->str:
        self.total_chars = len(s)
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

    # function to return total characters of the input
    def getTotalChars(self):
        return self.total_chars
    



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
    print(s)
    encoder = HuffmanEncoder()
    encoded = encoder.encode(s)
    print(encoded)
    root = encoder.getRoot()
    decoder = HuffmanDecoder()
    decoded = decoder.decode(root, encoded)
    print(decoded)


    