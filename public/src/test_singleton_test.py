#!/usr/bin/env python3
import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import *
from blocksplitter import *






class TestParentNode(unittest.TestCase):
    def test_eatingWords(self):
        text = '```python\ndef hello_world():\n    print(\"Hello, World!\")\n```'
        print(text_to_textnodes(text.strip("`")))

if __name__ == "__main__":
    unittest.main()


