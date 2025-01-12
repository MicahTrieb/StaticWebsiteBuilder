#!/usr/bin/env python3
import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import *
from blocksplitter import *






class TestParentNode(unittest.TestCase):
    def test_empty_content_between_delimiters(self):
        node = TextNode("hello `` there", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode('hello ', TextType.NORMAL),
            TextNode('', TextType.CODE),
            TextNode(' there', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)

if __name__ == "__main__":
    unittest.main()


