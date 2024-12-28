import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
		node1 = TextNode(None, TextType.ITALICS, "www.google.com")
		node2 = TextNode("None", TextType.ITALICS, "www.google.com")
		self.assertEqual(node1, node2)
		node1 = TextNode(None, None, None)
		node2 = TextNode("None", "None", "None")
		self.assertEqual(node1, node2)
		node1 = TextNode("This is a test module", TextType.CODE)
		node2 = TextNode("This is a text module", TextType.CODE)
		self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()

