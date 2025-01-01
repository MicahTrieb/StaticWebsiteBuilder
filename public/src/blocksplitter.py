from htmlnode import LeafNode, HTMLNode, ParentNode
from textnode import *
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    print(f"These are the old nodes before entering the code: {old_nodes}\n")
    if delimiter == None or delimiter == "":
        return old_nodes
    if text_type == None or text_type == "":
        raise Exception("Text type is required for delimiter")
    if not isinstance(old_nodes,list):
        raise Exception("Old Nodes must be in a list")
    indexList = []
    returnList = []
    nestingList = []
    for currentNode in old_nodes:
        print(f"This is the current node in the for loop: {currentNode}\n")
        print(f"This is the current text of the node: {currentNode.text}\n")
        if currentNode.text_type != TextType.NORMAL:
            returnList.append(currentNode)
        else:
            for currentIndex in range(0,len(currentNode.text)):
                if (delimiter == currentNode.text[currentIndex]) and text_type != TextType.BOLD:
                    print(f"Found {currentNode.text[currentIndex]} at: {currentIndex}")
                    if currentIndex + 1 < len(currentNode.text):
                        if currentNode.text[currentIndex + 1] == delimiter:
                            print(f"Nesting detected at: {currentIndex} and {currentIndex + 1}, changing variable \n")
                            if currentIndex in nestingList:
                                nestingList.append(currentIndex + 1)
                                continue
                            else:
                                nestingList.extend([
                                    currentIndex, currentIndex + 1
                                ])
                                continue
                    if currentNode.text[currentIndex - 1] != delimiter:
                        indexList.append(currentIndex)
                elif(delimiter == currentNode.text[currentIndex]) and text_type == TextType.BOLD:
                    print(f"Found them at: {currentIndex}")
                    if currentNode.text[currentIndex + 1] == "*":
                        indexList.append(currentIndex)
            if(nestingList):
                print(f"This is the nesting list: {nestingList}\n")
                print(f"This is the index list: {indexList}\n")
                while nestingList:
                    currentPopList = [nestingList.pop(0),nestingList.pop(-1)]
                    returnList.extend(
                        [
                            currentPopList
                        ]
                    )
            elif(len(indexList)) == 2 and delimiter != "*":
                returnList.append(
                    TextNode(f'"{currentNode.text[:indexList[0]]}"',currentNode.text_type))
                returnList.append(
                    TextNode(f'"{(currentNode.text[indexList[0] + 1:indexList[1]])}"',text_type))
                returnList.append(
                    TextNode(f'"{(currentNode.text[indexList[1] + 1:])}"',currentNode.text_type))
                indexList = []
            elif delimiter == "*" and text_type == TextType.BOLD and len(indexList) > 0:
                print("Index list: ", indexList)
                returnList.append(
                    TextNode(f'"{currentNode.text[:indexList[0]]}"',currentNode.text_type))
                returnList.append(
                    TextNode(f'"{(currentNode.text[indexList[0] + 2:indexList[1]])}"',text_type))
                returnList.append(
                    TextNode(f'"{(currentNode.text[indexList[1] + 2:])}"',currentNode.text_type))  
                indexList = []
            elif len(indexList) > 2 and len(indexList) % 2 == 0:
                splitList = [indexList[i:i+2] for i in range(0, len(indexList), 2)]
                if splitList[0][0] == 0:
                    returnList.append(
                        TextNode(f'"{currentNode.text[0]}"',text_type)
                    )
                for currentIndex in range (0, len(splitList)):
                    if splitList[currentIndex][0] == 0:
                        continue
                    if currentIndex + 1 < len(splitList):
                        nextStopValue = (splitList[currentIndex + 1][0])
                        returnList.extend([
                            TextNode(f'"{currentNode.text[:splitList[currentIndex][0]]}"',currentNode.text_type),
                            TextNode(f'"{currentNode.text[splitList[currentIndex][0] + 1:splitList[currentIndex][1]]}"',text_type),
                            TextNode(f'"{currentNode.text[splitList[currentIndex][1]+1:nextStopValue]}"',currentNode.text_type)
                        ])
                        print("This was one iteration of the nextCurrentIndex code\n",)
                        lastStop = nextStopValue
                        for i in returnList:    
                            print(f"{i}\n")
                    else:
                        returnList.extend([
                            TextNode(f'"{currentNode.text[splitList[currentIndex][0] + 1:splitList[currentIndex][1]]}"',text_type),
                            TextNode(f'"{currentNode.text[splitList[currentIndex][1] + 1]:}"',currentNode.text_type)
                    ])
                        print ("This was one iteration of the nextCurrentIndex's bypass code\n")
                        for i in returnList:
                            print(f"{i}\n")



                
            indexList = []
        print (returnList)
        #print("Made it")
    for i in returnList:
        print(f"{i}\n")
    if returnList == []:
        return f'"{old_nodes.text}"',old_nodes.text_type
    return returnList
    