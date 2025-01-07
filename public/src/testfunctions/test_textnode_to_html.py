#!/usr/bin/env python3  
import unittest

from textnode import *

class TestTextFunction(unittest.TestCase):
	def test_first_test(self):
		textnode = TextNode("This is the test", TextType.NORMAL)
		self.assertEqual(textnode.text_node_to_html_node(), "This is the test")


if __name__ == "__main__":
	unittest.main()
		
	

