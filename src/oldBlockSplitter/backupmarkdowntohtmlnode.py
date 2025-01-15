'''#This is a backup for the code I am about to nuke

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
                HTMLNode(f"h{headingNumber}", f"{currentBlock.lstrip("#")}", None, None)
            ])
        elif blockType == "quote block":
            print("This one is a quote block")
            extendingList.extend([
                HTMLNode("blockquote", currentBlock.lstrip("> "), None, None)
            ])
        elif blockType == "sorted list":
            childrenList = []
            print("This one is a sorted list")
            splitLines = currentBlock.split("\n")
            for currentLineIndex in range (1, len(splitLines)+1):
                currentChildren = (text_to_children(splitLines[currentLineIndex - 1].lstrip(f"{currentLineIndex}. ")))
                print (currentChildren)
                childrenList.append(HTMLNode("li", None, text_to_textnodes(currentChildren), None))
            extendingList.append(HTMLNode("ol", None, childrenList, None))
        elif blockType == "code":
            print("This one is a code block")
            extendingList.extend([
                HTMLNode("code", None, currentBlock.strip("`"), None)
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
            returnedNodes = text_to_textnodes(currentBlock)
            extendingList.append(HTMLNode("p", None, returnedNodes, None))
    return (HTMLNode("div", None, extendingList, None))
'''