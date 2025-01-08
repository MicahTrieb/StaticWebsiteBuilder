import re
from htmlnode import HTMLNode, LeafNode, ParentNode
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
    for i in blockedOut:
        print (block_to_blocktype(i))
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
            print("This one is a sorted list")
            currentList = []
            for line in currentBlock:
                currentList.extend([line])
            extendingList.extend([
                HTMLNode("ol", None, [("li", item, None, None) for item in currentList], None)
            ])
        elif blockType == "code":
            print("This one is a code block")
            extendingList.extend([
                HTMLNode("code", None, currentBlock, None)
            ])
        elif blockType == "unsorted list":
            print("This one is an unsorted list")
            currentList = [line.strip("* ") for line in currentBlock.split("\n") if line]
            currentList2 = [line.strip("- ") for line in currentList]
            print
            extendingList.extend([
                HTMLNode("ul", None, [LeafNode("li", item, None, None) for item in currentList2], None)
            ])
        elif blockType == "normal":
            print("This one is a normal")
            extendingList.extend([
                HTMLNode("p", currentBlock, None, None)
            ])
    return (extendingList)