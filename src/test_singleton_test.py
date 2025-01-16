#!/usr/bin/env python3
import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import *
from blocksplitter import *
from extracttitle import extract_title
from directorycopy import *
from pagegenerator import generate_page




class TestParentNode(unittest.TestCase):
    def test_print_directory(self):
        #from_path, template_path, dest_path
        generate_page("/home/mici/gitHub/MicahsProjects/staticWebsite/content/index.html","/home/mici/gitHub/MicahsProjects/staticWebsite/template.html","Filler")
if __name__ == "__main__":
    unittest.main()


