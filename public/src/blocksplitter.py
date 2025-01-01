from htmlnode import LeafNode, HTMLNode, ParentNode
from textnode import *
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    print(f"These are the old nodes before entering the code: {old_nodes}\n")
    if not isinstance(old_nodes,list):
        raise Exception("Old Nodes must be in a list")
    indexList = []
    returnList = []
    for currentNode in old_nodes:
        print(f"This is the current node in the for loop: {currentNode}\n")
        if currentNode.text_type != TextType.NORMAL:
            returnList.append(currentNode)
        else:
            for currentIndex in range(0,len(currentNode.text)):
                if (delimiter == currentNode.text[currentIndex]) and (delimiter != currentNode.text[currentIndex + 1]):
                    if text_type != TextType.BOLD:
                        print(f"Found it at: {currentIndex}")
                        indexList.append(currentIndex)
                elif(delimiter == currentNode.text[currentIndex]) and text_type == TextType.BOLD:
                    print(f"Found them at: {currentIndex}")
                    if currentNode.text[currentIndex + 1] == "*":
                        indexList.append(currentIndex)
                        
            if(len(indexList)) == 2 and delimiter != "*":
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
            elif len(indexList) > 2:
                splitList = [indexList[i:i+2] for i in range(0, len(indexList), 2)]
                if splitList[0][0] == 0:
                    returnList.append(
                        TextNode(f'"{currentNode.text[0]}"',text_type)
                    )
                for currentIndex in range (0, len(splitList)):
                    if splitList[0][0] == 0:
                        continue
                    if currentIndex + 1 < len(splitList):
                        nextStopValue = (splitList[currentIndex + 1][0])
                        returnList.extend([
                            TextNode(f'"{currentNode.text[:splitList[currentIndex][0]]}"',currentNode.text_type),
                            TextNode(f'"{currentNode.text[splitList[currentIndex][0] + 1:splitList[currentIndex][1]]}"',text_type),
                            TextNode(f'"{currentNode.text[splitList[currentIndex][1]+1:nextStopValue]}"',currentNode.text_type)
                        ])
                        print("This was one iteration of the nextCurrentIndex code\n")
                        for i in returnList:
                            print(f"{i}\n")
                    else:
                        returnList.extend([
                        TextNode(f'"{currentNode.text[:currentIndex][0]}"',currentNode.text_type),
                        TextNode(f'"{(currentNode.text[indexList[0] + 1:indexList[1]])}"',text_type),
                        TextNode(f'"{(currentNode.text[indexList[1] + 1:])}"',currentNode.text_type)
                    ])
                        print ("This was one iteration of the nextCurrentIndex's bypass code\n")
                        for i in returnList:
                            print(f"{i}\n")
                indexList = []


                
            indexList = []
        print (returnList)
        print("Made it")
    for i in returnList:
        print(f"{i}\n")
    return returnList
    