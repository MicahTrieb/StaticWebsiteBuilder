import os
import shutil
from blocksplitter import text_to_textnodes
from blockmarkdown import markdown_to_html_node, node_clean_up
from extracttitle import extract_title
from htmlnode import ParentNode, HTMLNode, LeafNode
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if not os.path.isfile(from_path):
        raise Exception("From path is not a file")
    if not os.path.isfile(template_path):
        raise Exception("Template path is not a file")
    #readingDirectory = str(os.read(os.open(from_path, os.O_APPEND), 25000)).lstrip("b' ")
    #newTemplate = str(os.read(os.open(template_path, os.O_APPEND), 25000)).lstrip("b' ")
    #newTemplate = newTemplate.replace("{{ Title }}", extract_title(readingDirectory))
    #formattedContents = markdown_to_html_node(readingDirectory.lstrip(f"# {extract_title(readingDirectory)}"))
    readingDirectory = open(from_path, "r")
    print(readingDirectory.read())
    #newTemplate = newTemplate.replace("{{ Content }}", node_clean_up(formattedContents))
    #for i in formattedContents.children:
        #print (i)
    
    #print (extract_title(readingDirectory))
    #markdown_to_html_node(readingDirectory.lstrip("b'"))

def html_format_builder(self):
    pass