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
    def test_unsortedList(self):
        inputText = "* This is a pseudo\n* unsorted list that \n* will hopefully be returned "
        testFunction = block_to_blocktype(inputText)
        self.assertEqual(testFunction, "unsorted list")
    def test_fakeUnsortedList(self):
        inputText = "* This is a fake\n*unsorted list that is missing the\n*spaces to make it considered a markdown \n- list"
        testFunction = block_to_blocktype(inputText)
        self.assertEqual(testFunction, "normal")
    def test_multipleUnsortedDividers(self):
        inputText = "* This is an unsorted list with \n- multiple different dividers between \n* * and \n- -, so hopefully it returns back as an unsorted list"
        testFunction = block_to_blocktype(inputText)
        self.assertEqual(testFunction, "unsorted list")
    def test_quoteBlockTesting(self):
        inputText = "> This is a quote block \n>Using varying spacing and \n>    symb0ls, hop>ing that it returns as a quote block"
        testFunction = block_to_blocktype(inputText)
        self.assertEqual(testFunction, "quote block")
    def test_fakeQuoteBlock(self):
        inputText = ">This will be a fake quote block that \n> will not be returned as a quote block, due to \n one of the new lines missing the \n> carrot"
        testFunction = block_to_blocktype(inputText)
        self.assertEqual(testFunction, "normal")
if __name__ == "__main__":
    unittest.main()