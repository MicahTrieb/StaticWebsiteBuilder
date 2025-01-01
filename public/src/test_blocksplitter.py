#!/usr/bin/env python3
import unittest
from blocksplitter import *
from textnode import * 

#def split_nodes_delimiter(old_nodes, delimiter, text_type):



class TestParentNode(unittest.TestCase):
#    def test_function_variability(self):
 #       nodeOne = TextNode("Hello, I am here to tell you **Samantha** is a wonderful person", TextType.NORMAL)
  #      nodeTwo = TextNode("And she is very *amazing* and spectacular", TextType.NORMAL)
   #     nodeThree = TextNode("And this is a very weird block of code", TextType.CODE)
    #    old_nodes = [nodeOne, nodeTwo, nodeThree]
     #   delimiter = "*"
      #  split_nodes_delimiter(old_nodes, delimiter, TextType.BOLD)
        #self.assertEqual(split_nodes_delimiter(old_nodes, delimiter, TextType.ITALIC), expectedoutput)
    def test_multiple_delimiters(self):
        node = TextNode("Text with multiple `code` blocks `here`.", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode('"Text with multiple "', TextType.NORMAL),
            TextNode('"code"', TextType.CODE),
            TextNode('" blocks "', TextType.NORMAL),
            TextNode('"here"', TextType.CODE),
            TextNode('"."', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)


        pass
if __name__ == "__main__":
    unittest.main()



