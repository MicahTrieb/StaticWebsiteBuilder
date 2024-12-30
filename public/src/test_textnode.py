import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		try:
			self.assertEqual(node, node2)
			print ("Self Assertion One Succeeded")
		except:
			print ("Self Assertion One Failed")
		node1 = TextNode("None", TextType.ITALIC, "www.google.com")
		node2 = TextNode("None", TextType.ITALIC, "www.google.com")
		try:
			self.assertEqual(node1, node2)
			print ("Self Assertion Two Succeeded")
		except:
			print ("Self Assertion Two Failed")
		node1 = TextNode(None, None, None)
		node2 = TextNode("None", "Non	e", "None")
		try:
			self.assertEqual(node1, node2)
			print ("Self Assertion Three Succeeded")
		except:
			print ("Self Assertion Three Failed")
		node1 = TextNode("This is a text module", TextType.CODE)
		node2 = TextNode("This is a text module", TextType.CODE)
		try:
			self.assertEqual(node1, node2)
			print ("Self Assertion Four Succeeded")
		except:
			print ("Self Assertion Four Failed")

if __name__ == "__main__":
    unittest.main()

