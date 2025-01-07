#!/usr/bin/env python3
import unittest
from textnode import *

class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_normal_text(self):
        textnode = TextNode("This is normal text", TextType.NORMAL)
        self.assertEqual(textnode.text_node_to_html_node(), "This is normal text")

    def test_bold_text(self):
        textnode = TextNode("This is bold text", TextType.BOLD)
        self.assertEqual(textnode.text_node_to_html_node(), "<b>This is bold text</b>")

    def test_italic_text(self):
        textnode = TextNode("This is italic text", TextType.ITALIC)
        self.assertEqual(textnode.text_node_to_html_node(), "<i>This is italic text</i>")

    def test_code_text(self):
        textnode = TextNode("print(\"Hello, World!\")", TextType.CODE)
        self.assertEqual(textnode.text_node_to_html_node(), "<code>print(\"Hello, World!\")</code>")

    def test_image_text(self):
        textnode = TextNode("An image", TextType.IMAGES, "https://example.com/image.png")
        self.assertEqual(textnode.text_node_to_html_node(), "<img src=\"https://example.com/image.png\" alt=\"An image\" />")

    def test_invalid_text_type(self):
        with self.assertRaises(Exception):
            TextNode("Invalid", "UNKNOWN_TYPE").text_node_to_html_node()

    def test_empty_normal_text(self):
        textnode = TextNode("", TextType.NORMAL)
        self.assertEqual(textnode.text_node_to_html_node(), "")

    def test_empty_bold_text(self):
        textnode = TextNode("", TextType.BOLD)
        self.assertEqual(textnode.text_node_to_html_node(), "<b></b>")

    def test_empty_italic_text(self):
        textnode = TextNode("", TextType.ITALIC)
        self.assertEqual(textnode.text_node_to_html_node(), "<i></i>")

    def test_empty_code_text(self):
        textnode = TextNode("", TextType.CODE)
        self.assertEqual(textnode.text_node_to_html_node(), "<code></code>")

    def test_empty_link_text(self):
        textnode = TextNode("", TextType.LINKS, "https://example.com")
        self.assertEqual(textnode.text_node_to_html_node(), "<a href=\"https://example.com\"></a>")

    def test_empty_image_text(self):
        textnode = TextNode("", TextType.IMAGES, "https://example.com/image.png")
        self.assertEqual(textnode.text_node_to_html_node(), "<img src=\"https://example.com/image.png\" alt=\"\" />")

    def test_missing_url_in_links(self):
        with self.assertRaises(TypeError):
            TextNode("Link without URL", TextType.LINKS).text_node_to_html_node()

    def test_missing_url_in_images(self):
        with self.assertRaises(TypeError):
            TextNode("Image without URL", TextType.IMAGES).text_node_to_html_node()

    def test_long_text_normal(self):
        long_text = "A" * 1000
        textnode = TextNode(long_text, TextType.NORMAL)
        self.assertEqual(textnode.text_node_to_html_node(), long_text)

    def test_long_text_bold(self):
        long_text = "A" * 1000
        textnode = TextNode(long_text, TextType.BOLD)
        self.assertEqual(textnode.text_node_to_html_node(), f"<b>{long_text}</b>")

    def test_link_with_special_chars(self):
        textnode = TextNode("Special & Char Link", TextType.LINKS, "https://example.com?a=1&b=2")
        self.assertEqual(textnode.text_node_to_html_node(), "<a href=\"https://example.com?a=1&b=2\">Special & Char Link</a>")

    def test_image_with_special_chars(self):
        textnode = TextNode("Image with special chars", TextType.IMAGES, "https://example.com/image?name=a&size=large")
        self.assertEqual(textnode.text_node_to_html_node(), "<img src=\"https://example.com/image?name=a&size=large\" alt=\"Image with special chars\" />")

    def test_code_with_special_chars(self):
        textnode = TextNode("<div>Hello</div>", TextType.CODE)
        self.assertEqual(textnode.text_node_to_html_node(), "<code><div>Hello</div></code>")

    def test_text_with_non_ascii_chars(self):
        textnode = TextNode("こんにちは", TextType.NORMAL)
        self.assertEqual(textnode.text_node_to_html_node(), "こんにちは")

    def test_bold_with_non_ascii_chars(self):
        textnode = TextNode("مرحبا", TextType.BOLD)
        self.assertEqual(textnode.text_node_to_html_node(), "<b>مرحبا</b>")

    def test_italic_with_non_ascii_chars(self):
        textnode = TextNode("Привет", TextType.ITALIC)
        self.assertEqual(textnode.text_node_to_html_node(), "<i>Привет</i>")

    def test_code_with_non_ascii_chars(self):
        textnode = TextNode("print(\"こんにちは\")", TextType.CODE)
        self.assertEqual(textnode.text_node_to_html_node(), "<code>print(\"こんにちは\")</code>")

if __name__ == "__main__":
    unittest.main()

