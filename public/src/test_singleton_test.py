#!/usr/bin/env python3
import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import *
from blocksplitter import *






class TestParentNode(unittest.TestCase):
    def test_eatingWords(self):
        text = '[Markdown Guide](https://www.markdownguide.org)\n- ![Example Image](https://via.placeholder.com/150)'
        print(text_to_textnodes(text))

if __name__ == "__main__":
    unittest.main()


