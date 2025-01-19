import os
import shutil
from blocksplitter import text_to_textnodes
from blockmarkdown import markdown_to_html_node, node_clean_up
def generate_page(from_path, template_path, dest_path):
    #print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if not os.path.isfile(from_path):
        raise Exception("From path is not a file")
    if not os.path.isfile(template_path):
        raise Exception("Template path is not a file")
    #openDirectory = os.open(template_path, os.O_APPEND)
    #readingDirectory = str(os.read(openDirectory, 2500000))
    #print (text_to_textnodes(readingDirectory))
    #openDirectory = os.open(from_path, os.O_APPEND)
    readingDirectory = str(os.read(os.open(from_path, os.O_APPEND), 25000))
    #markdown_to_html_node(readingDirectory.lstrip("b'"))
    #print(readingDirectory)
    print ((markdown_to_html_node(readingDirectory.lstrip("b'"))))
    #print (text_to_textnodes(readingDirectory))
    