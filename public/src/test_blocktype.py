#!/usr/bin/env python3
import unittest
from blockmarkdown import markdown_to_blocks, block_to_blocktype

class blockType(unittest.TestCase):
    def test_headerBlock(self):
        inputText = "### This is a header"
        testFunction = block_to_blocktype(inputText)
        self.assertEqual(testFunction, "header")
    def test_normalBlock(self):
        inputText = "This is a normal block of text"
        testFunction = block_to_blocktype(inputText)
        self.assertEqual(testFunction, "normal")
if __name__ == "__main__":
    unittest.main()