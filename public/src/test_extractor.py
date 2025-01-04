#!/usr/bin/env python3
import unittest
from blocksplitter import *
from textnode import *

class test_extractor(unittest.TestCase):
    def test_firstExtractor(self):
        old_node = (TextNode("This is test text with a ![funny image](www.google.com) and a potential link to a ![troll image](www.troll.com)",TextType.IMAGES))
        functionRun = split_nodes_image([old_node])
        #self.assertEqual(functionRun, ("This is a test hehe"))


if __name__ == "__main__":
    unittest.main()