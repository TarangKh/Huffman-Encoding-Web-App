
from tree_constructor import Node
from tree_constructor import TreeConstructor
import pickle
from huffman_encoder import HuffmanDecoder, preorder

file = open(r"Files\file1.pkl", "rb")
obj = pickle.load(file)

decode = HuffmanDecoder()
root = decode.generate_tree(obj.get_preorder(), obj.get_inorder())
preorder(root)

