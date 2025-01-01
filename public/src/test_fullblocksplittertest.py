#!/usr/bin/env python3
import unittest
from blocksplitter import *
from textnode import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_single_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode('"This is text with a "', TextType.NORMAL),
            TextNode('"code block"', TextType.CODE),
            TextNode('" word"', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)

    def test_no_delimiters(self):
        node = TextNode("This is plain text with no delimiters.", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode('"This is plain text with no delimiters."', TextType.NORMAL)]
        self.assertEqual(new_nodes, expected)

    def test_multiple_delimiters(self):
        node = TextNode("Text with multiple `code` blocks `here`.", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode('"Text with multiple "', TextType.NORMAL),
            TextNode('"code"', TextType.CODE),
            TextNode('" blocks "', TextType.NORMAL),
            TextNode('"here"', TextType.CODE),
            TextNode('"."', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)

    def test_empty_text_node(self):
        node = TextNode("", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode('""', TextType.NORMAL)]
        self.assertEqual(new_nodes, expected)

    def test_single_char_delimiter(self):
        node = TextNode("A delimiter at `start` and `end`.", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode('"A delimiter at "', TextType.NORMAL),
            TextNode('"start"', TextType.CODE),
            TextNode('" and "', TextType.NORMAL),
            TextNode('"end"', TextType.CODE),
            TextNode('"."', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)

    def test_consecutive_delimiters(self):
        node = TextNode("Code block ``empty`` end.", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode('"Code block "', TextType.NORMAL),
            TextNode('""', TextType.CODE),
            TextNode('"empty"', TextType.CODE),
            TextNode('" end."', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)

    def test_text_with_only_delimiters(self):
        node = TextNode("``````", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode('""', TextType.NORMAL),
            TextNode('""', TextType.CODE),
            TextNode('""', TextType.CODE),
            TextNode('""', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)

    def test_non_matching_delimiter(self):
        node = TextNode("This text has no matching delimiters.", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode('"This text has no matching delimiters."', TextType.NORMAL)]
        self.assertEqual(new_nodes, expected)

    def test_nested_delimiters(self):
        node = TextNode("This is `nested `code` block` example.", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode('"This is "', TextType.NORMAL),
            TextNode('"nested "', TextType.CODE),
            TextNode('"code"', TextType.CODE),
            TextNode('" block"', TextType.CODE),
            TextNode('" example."', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)

    def test_whitespace_inside_delimiters(self):
        node = TextNode("This is ` code block ` example.", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode('"This is "', TextType.NORMAL),
            TextNode('" code block "', TextType.CODE),
            TextNode('" example."', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)

    def test_escape_like_delimiters(self):
        node = TextNode("This is a \\`not a delimiter\\` example.", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode('"This is a \\`not a delimiter\\` example."', TextType.NORMAL)]
        self.assertEqual(new_nodes, expected)

    def test_unicode_text_with_delimiters(self):
        node = TextNode("This is `unicode 𝒜𝓃𝒹 𝓉𝑒𝓍𝓉` example.", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode('"This is "', TextType.NORMAL),
            TextNode('"unicode 𝒜𝓃𝒹 𝓉𝑒𝓍𝓉"', TextType.CODE),
            TextNode('" example."', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)

    def test_special_chars_inside_delimiters(self):
        node = TextNode("Special `!@#$%^&*()` characters.", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode('"Special "', TextType.NORMAL),
            TextNode('"!@#$%^&*()"', TextType.CODE),
            TextNode('" characters."', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)

    def test_long_text_with_delimiters(self):
        node = TextNode("Long text with `delimiters` inside.", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode('"Long text with "', TextType.NORMAL),
            TextNode('"delimiters"', TextType.CODE),
            TextNode('" inside."', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)

    def test_mixed_node_types(self):
        nodes = [
            TextNode("Text with `code block`.", TextType.NORMAL),
            TextNode("Normal text.", TextType.NORMAL),
        ]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        expected = [
            TextNode('"Text with "', TextType.NORMAL),
            TextNode('"code block"', TextType.CODE),
            TextNode('"."', TextType.NORMAL),
            TextNode('"Normal text."', TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected)

if __name__ == "__main__":
    unittest.main()
