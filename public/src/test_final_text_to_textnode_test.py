#!/usr/bin/env python3
import unittest
from blocksplitter import text_to_textnodes, split_nodes_delimiter, split_nodes_image, split_nodes_link


class test_fullTesting(unittest.TestCase):
    def test_basicString(self):
        textString = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        text_to_textnodes(textString)

if __name__ == "__main__":
    unittest.main()