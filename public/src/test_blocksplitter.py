#!/usr/bin/env python3
import unittest
from blocksplitter import *
from textnode import * 

#def split_nodes_delimiter(old_nodes, delimiter, text_type):



#    def test_function_variability(self):
 #       nodeOne = TextNode("Hello, I am here to tell you **Samantha** is a wonderful person", TextType.NORMAL)
  #      nodeTwo = TextNode("And she is very *amazing* and spectacular", TextType.NORMAL)
   #     nodeThree = TextNode("And this is a very weird block of code", TextType.CODE)
    #    old_nodes = [nodeOne, nodeTwo, nodeThree]
     #   delimiter = "*"
      #  split_nodes_delimiter(old_nodes, delimiter, TextType.BOLD)
        #self.assertEqual(split_nodes_delimiter(old_nodes, delimiter, TextType.ITALIC), expectedoutput)
class TestParentNode(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode("hello `world` there", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode('"hello "', TextType.NORMAL),
            TextNode('"world"', TextType.CODE),
            TextNode('" there"', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)


if __name__ == "__main__":
    unittest.main()



