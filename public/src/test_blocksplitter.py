#!/usr/bin/env python3
import unittest
from blocksplitter import *
from textnode import * 

#def split_nodes_delimiter(old_nodes, delimiter, text_type):



class TestParentNode(unittest.TestCase):
    def test_function_variability(self):
        old_nodes = TextNode("Hello, I am here to tell you *Samantha* is a wonderful person", TextType.NORMAL)
        delimiter = "*"
        expectedoutput = [
            TextNode("Hello, I am here to tell you ", TextType.NORMAL),
            TextNode("*Samantha*", TextType.ITALIC),
            TextNode(" is a wonderful person", TextType.NORMAL)
        ]
        self.assertEqual(split_nodes_delimiter(old_nodes, delimiter, TextType.NORMAL), expectedoutput)


        pass
if __name__ == "__main__":
    unittest.main()



