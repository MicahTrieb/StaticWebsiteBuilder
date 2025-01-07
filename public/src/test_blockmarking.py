#!/usr/bin/env python3
import unittest
from blockmarkdown import markdown_to_blocks

class block_marking(unittest.TestCase):
    def firstMarkDownTest(self):
        inputText = ("# This is a heading\n\n"
                     
        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n"

        "* This is the first list item in a list block\n"
        "* This is a list item\n"
        "* This is another list item\n"
        )
        testFunction = markdown_to_blocks(inputText)
        expectedOutcome = (["# This is a heading","This is a paragraph of text. It has some **bold** and *italic* words inside of it.","* This is the first list item in a list block\n"
        "* This is a list item\n"
        "* This is another list item\n"])

        self.assertEqual(testFunction, expectedOutcome)