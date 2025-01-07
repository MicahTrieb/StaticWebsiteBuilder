#!/usr/bin/env python3
import unittest
from blocksplitter import *
from textnode import *

class TestSplitNodesDelimiter(unittest.TestCase):
    
    # Test basic functionality
    def test_single_delimiter_pair(self):
        node = TextNode("hello `world` there", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode('hello ', TextType.NORMAL),
            TextNode('world', TextType.CODE),
            TextNode(' there', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)

    def test_multiple_delimiter_pairs(self):
        node = TextNode("hello `world` and `planet`", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode('hello ', TextType.NORMAL),
            TextNode('world', TextType.CODE),
            TextNode(' and ', TextType.NORMAL),
            TextNode('planet', TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected)

    # Test edge cases
    def test_no_delimiters(self):
        node = TextNode("hello world", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode('hello world', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)

    def test_missing_closing_delimiter(self):
        node = TextNode("hello `world", TextType.NORMAL)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_empty_content_between_delimiters(self):
        node = TextNode("hello `` there", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode('hello ', TextType.NORMAL),
            TextNode('', TextType.CODE),
            TextNode(' there', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)

    # Test different delimiter types
    def test_bold_delimiter(self):
        node = TextNode("hello **world** there", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode('hello ', TextType.NORMAL),
            TextNode('world', TextType.BOLD),
            TextNode(' there', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)

    def test_italic_delimiter(self):
        node = TextNode("hello *world* there", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [
            TextNode('hello ', TextType.NORMAL),
            TextNode('world', TextType.ITALIC),
            TextNode(' there', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)

    def test_code_delimiter(self):
        node = TextNode("hello `world` there", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode('hello ', TextType.NORMAL),
            TextNode('world', TextType.CODE),
            TextNode(' there', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)

if __name__ == "__main__":
    unittest.main()
