import re
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode
from regexfunction import extract_markdown_images, extract_markdown_link
from blocksplitter import text_to_textnodes
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
    blockedOut = markdown_to_blocks(markdown)
    extendingList = []
    for currentBlock in blockedOut:
        print(f"Current block: {currentBlock}")
        blockType = block_to_blocktype(currentBlock)
        print(f"Current block type: {blockType}")
        if blockType == "header":
            print("This one is a header")
            headingNumber = (len(list(re.findall(r"^(#+)",currentBlock))[0]))
            extendingList.extend([
                HTMLNode(f"h{headingNumber}", f"{currentBlock}", None, None)
            ])
        elif blockType == "quote block":
            print("This one is a quote block")
            extendingList.extend([
                HTMLNode("blockquote", currentBlock, None, None)
            ])
        elif blockType == "sorted list":
            childrenList = []
            print("This one is a sorted list")
            splitLines = currentBlock.split("\n")
            for currentLineIndex in range (1, len(splitLines)+1):
                currentChildren = (text_to_children(splitLines[currentLineIndex - 1].lstrip(f"{currentLineIndex}. ")))
                print (currentChildren)
                childrenList.append(HTMLNode("li", None, splitLines[currentLineIndex - 1]))
            extendingList.append(HTMLNode("ol", None, childrenList, None))
        elif blockType == "code":
            print("This one is a code block")
            extendingList.extend([
                HTMLNode("code", None, currentBlock, None)
            ])
        elif blockType == "unsorted list":
            childrenList = []
            print("This one is an unsorted list")
            splitLines = currentBlock.split("\n")
            for currentLine in splitLines:
                currentChildren = (text_to_children(currentLine.lstrip("* -")))
                print (currentChildren)
                childrenList.append(HTMLNode("li", None, currentChildren, None))
            extendingList.append(HTMLNode("ul", None, childrenList, None))


            
        elif blockType == "normal":
            print("This one is a normal")
            extendingList.extend([
                HTMLNode("p", currentBlock, None, None)
            ])
    return (HTMLNode("div", None, extendingList, None))

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
