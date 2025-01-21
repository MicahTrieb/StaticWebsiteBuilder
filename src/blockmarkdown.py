import re
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import *
from regexfunction import extract_markdown_images, extract_markdown_link
from blocksplitter import text_to_textnodes, simple_parser, split_nodes_delimiter, split_nodes_image, split_nodes_link
def markdown_to_blocks(inputString):
    return [block.strip() for block in inputString.split("\n\n")]


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
    divNode = ParentNode("div", [], None)
    allBlocks = markdown_to_blocks(markdown)
    #print(allBlocks)
    #return "Stop code here debug line"
    appendingBlockList = []
    for currentBlock in allBlocks:
        #print (f"DEBUG TEXT TO TEXTNODE HERE: {text_to_textnodes(currentBlock)}")
        blockType = block_to_blocktype(currentBlock)
        if blockType == "header":
            headingNumber = (len(list(re.findall(r"^(#+)",currentBlock))[0]))
            divNode.add_child(LeafNode(f"h{headingNumber}", text_to_textnodes(currentBlock.lstrip("# "))[0].text_node_to_html_node(), None))
        if blockType == "code":
            childrenNode = ParentNode("pre", None, [])
            childrenNode.add_child(LeafNode("code", text_to_textnodes(currentBlock.strip("`"))[0].text_node_to_html_node(), None))
            divNode.add_child(childrenNode)
        if blockType == "quote block":
            divNode.add_child(LeafNode("blockquote", text_to_textnodes(currentBlock.lstrip("> "))[0].text_node_to_html_node(), None))
        if blockType == "unsorted list":
            splitBlock = currentBlock.split("\n")
            childrenList = []
            for currentSplittedBlock in splitBlock:
                lenOfList = len(text_to_textnodes(currentSplittedBlock.lstrip("-* ")))
                for currentIndex in range (0, lenOfList):
                    childrenList.append(LeafNode("li", (text_to_textnodes(currentSplittedBlock.lstrip("-* ")))[currentIndex].text_node_to_html_node(), None))
            childrenNode = ParentNode("ul", None, [])
            childrenNode.add_child(childrenList)
            divNode.add_child(childrenNode)
        if blockType == "sorted list":
            splitBlock = currentBlock.split("\n")
            childrenList = []
            for currentBlockIndex in range(0, len(splitBlock)):
                childrenList.append(LeafNode("li", text_to_textnodes(splitBlock[currentBlockIndex].lstrip(f"{currentBlockIndex + 1}. "))[0].text_node_to_html_node()))
            childrenNode = ParentNode("ol", None, [])
            childrenNode.add_child(childrenList)
            divNode.add_child(childrenNode)
        if blockType == "normal":
            if currentBlock:
                divNode.add_child(LeafNode("p", text_to_textnodes(currentBlock)[0].text_node_to_html_node(), None))
    print(node_clean_up(divNode))
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
    
def node_clean_up(node, level = 0):
    fullString = ""
    currentIndent = "    " * level
    if isinstance(node, TextNode):
        fullString += (f"{currentIndent}{node.text}\n")

    if isinstance(node, HTMLNode):
        fullString += (f"\n{currentIndent}Tag: {node.tag}   Value: {node.value}   Children: ")
        if node.children:
            for currentNodeChild in node.children:
                fullString += node_clean_up(currentNodeChild, level + 1)
        else:
            fullString += (f"No children\n")

    return(fullString)
    