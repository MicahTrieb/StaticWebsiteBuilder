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
            childrenToNodes = text_to_textnodes(splitBlock[currentIndex].lstrip("# "))
            if len(childrenToNodes) == 1:
                divNode.add_child(LeafNode(f"h{headingNumber}", text_to_textnodes(currentBlock.lstrip("# "))[0].text_node_to_html_node(), None))
            elif len(childrenToNodes) > 1:
        if blockType == "code":
            childrenNode = ParentNode("pre", None, [])
            childrenNode.add_child(LeafNode("code", text_to_textnodes(currentBlock.strip("`"))[0].text_node_to_html_node(), None))
            divNode.add_child(childrenNode)
        if blockType == "quote block":
            divNode.add_child(LeafNode("blockquote", text_to_textnodes(currentBlock.lstrip("> "))[0].text_node_to_html_node(), None))
        if blockType == "unsorted list":
            splitBlock = currentBlock.split("\n")
            textNodeList = []
            childrenList = []
            for currentIndex in range(0, len(splitBlock)):
                childrenToNodes = text_to_textnodes(splitBlock[currentIndex].lstrip("-* "))
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