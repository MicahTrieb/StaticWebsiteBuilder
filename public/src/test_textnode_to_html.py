#!/usr/bin/env python3  
import unittest

from textnode import *

	#def __init__(self, text, text_type, url=""):
		#self.text = text
		#self.url = url
		#self.text_type = text_type
class TestTextFunction(unittest.TestCase):
	def test_first_test(self):
		textnode = TextNode("This is the test", TextType.NORMAL)
		self.assertEqual(textnode.text_node_to_html_node(), "This is the test")

		        # ParentNode with self-closing children
       # child = LeafNode(tag="img", value=" ")
       # parent = ParentNode(tag="div", children=[child])
       # self.assertEqual(parent.to_html(), "<div><img> </img></div>")


if __name__ == "__main__":
	unittest.main()
		
	

