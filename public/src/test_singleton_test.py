#!/usr/bin/env python3
import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import *
from blocksplitter import *






class TestParentNode(unittest.TestCase):
    def test_bold_text(self):
        textnode = TextNode("This is bold text", TextType.BOLD)
        self.assertEqual(textnode.text_node_to_html_node(), "<b>This is bold text</b>")

if __name__ == "__main__":
    unittest.main()


