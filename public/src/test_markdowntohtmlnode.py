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
        unittest.util._MAX_LENGTH = 99999999999
        self.assertEqual(markdown_to_html_node("# Hello"), markdown_to_html_node("# Hello"))
if __name__ == "__main__":
    unittest.main()
