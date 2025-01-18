#!/usr/bin/env python3
import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import *
from blocksplitter import *
from extracttitle import extract_title
from directorycopy import *
from pagegenerator import generate_page
from blockmarkdown import *



class TestParentNode(unittest.TestCase):
    #def test_print_directory(self):
        #from_path, template_path, dest_path
        #generate_page("/home/mici/gitHub/MicahsProjects/staticWebsite/content/index.html","/home/mici/gitHub/MicahsProjects/staticWebsite/template.html","Filler")
    def test_markdown_to_html(self):
        print(split_nodes_link([TextNode('# Tolkien Fan Club\n\n**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn\'t work yet)\n\n', TextType.NORMAL)]))

    #def test_regex_split(self):
        #print(regex_split_test('# Tolkien Fan Club\n\n**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn\'t work yet)\n\n'))
        #print(regex_split_test('[first post here](/majesty) (sorry the link doesn\'t work yet)\n\n'))
        #print(regex_split_test('(sorry the link doesn\'t work yet)\n\n[first post here](/majesty)'))
        #returnList = regex_split_test('# Tolkien Fan Club\n\n**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn\'t work yet)\n\nRead my [first post here](/majesty)[first post here](/majesty)')
        #for i in range(0, len(returnList)):
            #if i % 2 == 0:
                #print(f"{returnList[i]} should be a text")
            #else:
                #print (f"{returnList[i]} should be a link")

if __name__ == "__main__":
    unittest.main()


