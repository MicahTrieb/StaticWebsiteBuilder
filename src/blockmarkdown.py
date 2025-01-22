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
    for currentBlock in allBlocks:
        #print (f"DEBUG TEXT TO TEXTNODE HERE: {text_to_textnodes(currentBlock)}")
        #print(allBlocks)
        blockType = block_to_blocktype(currentBlock)
        splitBlock = currentBlock.split("\n")
        textNodeList = []
        if blockType == "header":
            headingNumber = (len(list(re.findall(r"^(#+)",currentBlock))[0]))
            for currentIndex in splitBlock:
                childrenToNodes = text_to_textnodes(currentIndex.lstrip("# "))
                if len(childrenToNodes) == 1:
                    divNode.add_child(LeafNode(f"h{headingNumber}", text_to_textnodes(currentBlock.lstrip("# "))[0].text_node_to_html_node(), None))
                    continue
                elif len(childrenToNodes) > 1:
                    for currentNode in childrenToNodes:
                        if currentNode.text_type == TextType.NORMAL:
                            textNodeList.append(currentNode.text.lstrip("# "))
                        else:
                            textNodeList.append(currentNode.text_node_to_html_node().lstrip("# "))
                    combinedList = "".join(textNodeList)
                    divNode.add_child(LeafNode(f"h{headingNumber}", combinedList))

        if blockType == "code":
            childrenNode = ParentNode("pre", None, [])
            childrenNode.add_child(LeafNode("code", text_to_textnodes(currentBlock.strip("`"))[0].text_node_to_html_node(), None))
            divNode.add_child(childrenNode)           
        if blockType == "unsorted list":
            textNodeList = []
            childrenList = []
            for currentIndex in range(0, len(splitBlock)):
                if re.findall(r"(^- )", splitBlock[currentIndex]):
                    childrenToNodes = text_to_textnodes(splitBlock[currentIndex].lstrip("- "))
                elif re.findall(r"(^\* )", splitBlock[currentIndex]):
                    childrenToNodes = text_to_textnodes(splitBlock[currentIndex].lstrip("* "))
                if len(childrenToNodes) == 1:
                    childrenList.append(LeafNode("li",childrenToNodes[0].text_node_to_html_node(), None))
                elif len(childrenToNodes) > 1:
                    for currentNode in childrenToNodes:
                        if currentNode.text_type == TextType.NORMAL:
                            textNodeList.append(currentNode.text)
                        else:
                            textNodeList.append(currentNode.text_node_to_html_node())
                    combinedList = "".join(textNodeList)
                    childrenList.append(LeafNode("li", combinedList,None))
            childrenNode = ParentNode("ul", None, [])
            childrenNode.add_child(childrenList)
            divNode.add_child(childrenNode)
                    
        if blockType == "sorted list":
            textNodeList = []
            childrenList = []
            for currentIndex in range(0, len(splitBlock)):
                childrenToNodes = text_to_textnodes(splitBlock[currentIndex].lstrip(f"{currentIndex + 1}. "))
                if len(childrenToNodes) == 1:
                    childrenList.append(LeafNode("li", childrenToNodes[0].text_node_to_html_node()))
                elif len(childrenToNodes) > 1:
                    for currentNode in childrenToNodes:
                        if currentNode.text_type == TextType.NORMAL:
                            textNodeList.append(currentNode.text)
                        else:
                            textNodeList.append(currentNode.text_node_to_html_node())
                    combinedList = "".join(textNodeList)
                    childrenList.append(LeafNode("li", combinedList,None))
            childrenNode = ParentNode("ol", None, [])
            childrenNode.add_child(childrenList)
            divNode.add_child(childrenNode)
        if blockType == "quote block":
            textNodeList = []
            for currentIndex in splitBlock:
                childrenToNodes = text_to_textnodes(currentIndex.lstrip("> "))
                if len(childrenToNodes) == 1:
                    divNode.add_child(LeafNode("blockquote", currentIndex.lstrip("> ")))
                elif(len(childrenToNodes) > 1):
                    for currentIndex in childrenToNodes:
                        if currentIndex.text_type == TextType.NORMAL:
                            textNodeList.append(currentIndex.text)
                        else:
                            textNodeList.append(currentIndex.text_node_to_html_node())
                    combinedList = "".join(textNodeList)
                    divNode.add_child(LeafNode("blockquote", combinedList))                             
        if blockType == "normal":
            textNodeList = []
            for currentIndex in splitBlock:
                childrenToNodes = text_to_textnodes(currentIndex)
                if len(childrenToNodes) == 1:
                    divNode.add_child(LeafNode("p", currentIndex))
                elif(len(childrenToNodes) > 1):
                    for currentIndex in childrenToNodes:
                        if currentIndex.text_type == TextType.NORMAL:
                            textNodeList.append(currentIndex.text)
                        else:
                            textNodeList.append(currentIndex.text_node_to_html_node())
                    combinedList = "".join(textNodeList)
                    divNode.add_child(LeafNode("p", combinedList))

    return(divNode)
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
    