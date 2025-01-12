import re
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode
from regexfunction import extract_markdown_images, extract_markdown_link
from blocksplitter import text_to_textnodes, simple_parser, split_nodes_delimiter, split_nodes_image, split_nodes_link
def markdown_to_blocks(inputString):
    return [block.strip() for  block in inputString.split("\n\n")]


def block_to_blocktype(inputBlock):
    headerRegex = re.findall(r"^#+(?= )", inputBlock)
    if headerRegex:
        return "header"
    codeBlock1 = re.findall(r"^`{3}", inputBlock)
    codeBlock2 = re.findall(r"`{3}(?=$)", inputBlock)
    if(codeBlock1 and codeBlock2):
        return "code"
    if inputBlock:
        unsortedLines = inputBlock.split("\n")
        if(unsortedLines):
            counter = 0
            for currentLine in unsortedLines:
                currentList = [(re.findall(r"^\-(?= )", currentLine)), (re.findall(r"^\*(?= )", currentLine))]
                if currentList[0] or currentList[1]:
                    counter += 1
        if counter == len(unsortedLines) and unsortedLines:
            return "unsorted list"
        if(unsortedLines):
            counter = 0
            for currentLine in unsortedLines:
                if (re.findall(r"^>", currentLine)):
                    counter += 1
            if counter == len(unsortedLines) and unsortedLines:
                return "quote block"
            counter = 1
            for currentLine in unsortedLines:
                if re.search(rf"^{counter}\. ", currentLine):
                    #print (currentLine)
                    counter +=1 
                if counter == len(unsortedLines) - 1 and unsortedLines:
                    return ("sorted list")
    return "normal"

def markdown_to_html_node(markdown):
    divNode = HTMLNode("div", None, [], None)
    allBlocks = markdown_to_blocks(markdown)
    appendingBlockList = []
    for currentBlock in allBlocks:
        blockType = block_to_blocktype(currentBlock)
        if blockType == "header":
            strippedBlock = currentBlock.lstrip("# ")
            headingNumber = (len(list(re.findall(r"^(#+)",currentBlock))[0]))
            currentNode = text_to_textnodes(strippedBlock)
            divNode.add_child(HTMLNode(f"h{headingNumber}", None, currentNode, None))
        if blockType == "code":
            strippedBlock = currentBlock.strip("`")
            currentNode = text_to_textnodes(strippedBlock)
            divNode.add_child(HTMLNode("code", strippedBlock, None))
    return divNode
def text_to_children(text):
    nodes = []
    currentTextNodes = (text_to_textnodes(text))
    for currentNode in currentTextNodes:
        nodes.append(TextNode.text_node_to_html_node(currentNode))
    return nodes
def add_child(self, node):
    if isinstance(node, list):
        for currentNode in node:
            if not isinstance(currentNode, HTMLNode):
                raise Exception("All list contents must be HTMLNodes")
        self.children.extend(node)
    elif isinstance(node, HTMLNode):
        self.children.append(node)
    else:
        raise Exception("Content must be an HTMLNode")
