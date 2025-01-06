#!/usr/bin/env python3
import unittest
from blocksplitter import text_to_textnodes, split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import *

class test_fullTesting(unittest.TestCase):
    def test_basicString(self):
        textString = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev) and a second image ![here](www.currentimage.com)"
        result = text_to_textnodes(textString)
        self.maxDiff = None
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.NORMAL),
            TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINKS, "https://boot.dev"),
            TextNode(" and a second image ", TextType.NORMAL),
            TextNode("here", TextType.IMAGES, "www.currentimage.com")
        ]
        self.assertEqual(result, expected)

    def test_emptyString(self):
        textString = ""
        result = text_to_textnodes(textString)
        self.assertEqual(result, [])  # Empty input should return an empty list

    def test_onlyText(self):
        textString = "This is a simple text without any formatting."
        result = text_to_textnodes(textString)
        expected = [
            TextNode("This is a simple text without any formatting.", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_singleBold(self):
        textString = "This is **bold text** only."
        result = text_to_textnodes(textString)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold text", TextType.BOLD),
            TextNode(" only.", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_multipleLinks(self):
        textString = "Check out [this link](https://example.com) and [another one](https://another.com)."
        result = text_to_textnodes(textString)
        expected = [
            TextNode("Check out ", TextType.NORMAL),
            TextNode("this link", TextType.LINKS, "https://example.com"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("another one", TextType.LINKS, "https://another.com"),
            TextNode(".", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
