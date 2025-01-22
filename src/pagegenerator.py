import os
import shutil
from blocksplitter import text_to_textnodes
from blockmarkdown import markdown_to_html_node, node_clean_up
from extracttitle import extract_title
from directorycopy import directory_copy
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
    preReadDirectory = open(from_path, "r")
    readingDirectory = preReadDirectory.read()
    preReadDirectory.close()
    openTemplate = open(template_path, "r")
    template = openTemplate.read()
    openTemplate.close()
    print(template)
    template = template.replace("{{ Title }}", extract_title(readingDirectory))
    template = template.replace("{{ Content }}", markdown_to_html_node("".join(list(readingDirectory))).to_html())
    print(template)
    #directory_copy("/home/mici/gitHub/MicahsProjects/staticWebsite/static", "/home/mici/gitHub/MicahsProjects/staticWebsite/public")
    if os.path.exists("/home/mici/gitHub/MicahsProjects/staticWebsite/temp"):
        shutil.rmtree("/home/mici/gitHub/MicahsProjects/staticWebsite/temp")
    os.mkdir("/home/mici/gitHub/MicahsProjects/staticWebsite/temp")
    tempDirectory = "/home/mici/gitHub/MicahsProjects/staticWebsite/temp/index.html"
    with open(tempDirectory, "w") as temp_file:
        temp_file.write(template)
    directory_copy("/home/mici/gitHub/MicahsProjects/staticWebsite/temp", dest_path)
    shutil.rmtree("/home/mici/gitHub/MicahsProjects/staticWebsite/temp")


def directory_target_identifier(directory):
    if os.path.isfile(directory):
        return "File"
    elif os.path.isdir(directory):
        return "Directory"



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.isdir(dir_path_content):
        allContents = os.listdir(dir_path_content)
        for currentItem in allContents:
            currentDirectory = os.path.join(dir_path_content, currentItem)
            contentType = directory_target_identifier(currentDirectory)
            if contentType == "File":
                generate_pages_recursive(currentDirectory, template_path, dest_dir_path)
            elif contentType == "Directory":
                #contentDictionary[currentItem] = directory_target_identifier(currentDirectory)
                generate_pages_recursive(currentDirectory, template_path, dest_dir_path)
    elif os.path.isfile(dir_path_content):
        try:
            extract_title(dir_path_content)
            writingDirectory = os.path.join(dest_dir_path, dir_path_content)
            generate_page(writingDirectory, template_path, dest_dir_path)
        except:
            pass
    #return contentDictionary