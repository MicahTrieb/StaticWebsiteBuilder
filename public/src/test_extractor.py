#!/usr/bin/env python3
import unittest
from blocksplitter import *
from textnode import *

class test_extractor(unittest.TestCase):
    def test_firstExtractor(self):
        old_node = (TextNode("This is test text with a ![funny image](www.google.com) and a potential link to a ![troll image](www.troll.com)",TextType.NORMAL))
        functionRun = split_nodes_image([old_node])
        expectedOutcome = [
            TextNode("This is test text with a ", TextType.NORMAL),
            TextNode("funny image", TextType.IMAGES, "www.google.com"),
            TextNode(" and a potential link to a ", TextType.NORMAL),
            TextNode("troll image", TextType.IMAGES, "www.troll.com")
        ]
        self.assertEqual(functionRun, expectedOutcome)
    def test_firstLinkExtractor(self):
        old_node = (TextNode("This is a funny test with a link [to the moon](www.themoon.com) and hopefully it returns successfully", TextType.NORMAL))
        functionRun = split_nodes_link([old_node])
        expectedOutcome = [
            TextNode("This is a funny test with a link to ", TextType.NORMAL),
            TextNode("to the moon", TextType.LINKS, "www.themoon.com"),
            TextNode(" and hopefully it returns successfully", TextType.NORMAL)
        ]
        self.assertEqual(functionRun, expectedOutcome)

if __name__ == "__main__":
    unittest.main()