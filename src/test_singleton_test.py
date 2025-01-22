#!/usr/bin/env python3
import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import *
from blocksplitter import *
from extracttitle import extract_title
from directorycopy import *
from pagegenerator import generate_page
from blockmarkdown import *
from blocksplitter import text_to_textnodes



class TestParentNode(unittest.TestCase):
    #def test_print_directory(self):
        #from_path, template_path, dest_path
        #generate_page("/home/mici/gitHub/MicahsProjects/staticWebsite/content/index.html","/home/mici/gitHub/MicahsProjects/staticWebsite/template.html","/home/mici/gitHub/MicahsProjects/staticWebsite/public")
    #def test_markdown_to_html(self):
        #print(split_nodes_link([TextNode('# Tolkien Fan Club\n\n**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn\'t work yet)\n\n', TextType.NORMAL)]))

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
    #def test_header_check(self):
        #headerText = "# This is a header"
        #print(markdown_to_html_node(headerText))
    #def test_italics_in_stuff(self):
        #testString = "**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)"
        #print(markdown_to_html_node(testString))
    #def test_link_in_header(self):
        #headerText = "# This is a header with a ![hyperlink](www.google.com)"
        #print(markdown_to_html_node(headerText))

    #def test_image_linker(self):
        #imageText = "# This is a header with a ![hyperlink](www.google.com)"
        #print(text_to_textnodes(imageText))
    def test_pass(self):
        pass
if __name__ == "__main__":
    unittest.main()


