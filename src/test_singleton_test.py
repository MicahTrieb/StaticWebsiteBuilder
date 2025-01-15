#!/usr/bin/env python3
import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import *
from blocksplitter import *






class TestParentNode(unittest.TestCase):
    def test_multipleLinks(self):
        textString = "Check out [this link](https://example.com) and [another one](https://another.com)."
        result = text_to_textnodes(textString)
        expected = [
            TextNode("Check out ", TextType.NORMAL),
            TextNode("this link", TextType.LINKS, "https://example.com"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("another one", TextType.LINKS, "https://another.com"),
            TextNode(".", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()


