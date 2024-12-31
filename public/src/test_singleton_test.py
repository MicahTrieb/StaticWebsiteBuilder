#!/usr/bin/env python3
import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode






class TestParentNode(unittest.TestCase):
    def test_self_closing_children(self):
        # ParentNode with self-closing children
        child = LeafNode(tag="img", value=" ")
        parent = ParentNode(tag="div", children=[child])
        self.assertEqual(parent.to_html(), "<div><img> </img></div>")
if __name__ == "__main__":
    unittest.main()


