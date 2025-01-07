#!/usr/bin/env python3
import unittest
from blockmarkdown import markdown_to_blocks

class block_marking(unittest.TestCase):
    def test_firstMarkDownTest(self):
        inputText = ("# This is a heading\n\n"
                     
        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n"

        "* This is the first list item in a list block\n"
        "* This is a list item\n"
        "* This is another list item\n"
        )
        testFunction = markdown_to_blocks(inputText)
        expectedOutcome = (["# This is a heading","This is a paragraph of text. It has some **bold** and *italic* words inside of it.","* This is the first list item in a list block\n"
        "* This is a list item\n"
        "* This is another list item"])

        self.assertEqual(testFunction, expectedOutcome)
    def test_secondMarkDownTest(self):
        inputText = ("#This is a heading to the newer line\n\nBut honestly I can't imagine this NOT working, like, even if `the code` was inputted, or I **bolded** and *italicized* it and put it all into one line, I still think it will return just fine\n\nNow imagine if I continue to create blocks in the same line\n\nNow it's getting a bit verbose but I shall continue\n\nuntil now")
        testFunction = markdown_to_blocks(inputText)
        expectedOutcome = (["#This is a heading to the newer line","But honestly I can't imagine this NOT working, like, even if `the code` was inputted, or I **bolded** and *italicized* it and put it all into one line, I still think it will return just fine","Now imagine if I continue to create blocks in the same line","Now it's getting a bit verbose but I shall continue", "until now"])
        self.assertEqual(testFunction, expectedOutcome)
if __name__ == "__main__":
    unittest.main()