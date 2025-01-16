#!/usr/bin/env python3
import unittest
import unittest.util
from blockmarkdown import markdown_to_html_node, block_to_blocktype, markdown_to_blocks
from htmlnode import *
from textnode import *
import difflib
class TestBlocking(unittest.TestCase):
    maxDiff = None
    def test_firstTestCase(self):
        self.maxDiff = None
        unittest.util._MAX_LENGTH = 99999999999
        function = markdown_to_html_node("Hello")
        #print(f"Output here: {function}\n")
        #print("Expected Output here: tag=div value=None children=[tag=h1 value=[TextNode(Hello, TextType.NORMAL, )] children=None props=None] props=None")
        expectedOutcome = HTMLNode("div", None, [HTMLNode("h1", [TextNode("Hello", TextType.NORMAL, )])])
        #print(repr(markdown_to_html_node("# Hello")))
        #print(repr(expectedOutcome))
        #print("\n".join(diff))
        self.assertEqual(markdown_to_html_node("# Hello"), expectedOutcome)
if __name__ == "__main__":
    unittest.main()
