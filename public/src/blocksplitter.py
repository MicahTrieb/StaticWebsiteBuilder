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
                if (delimiter == currentNode.text[currentIndex]) and text_type != TextType.BOLD:
                    print(f"Found it at: {currentIndex}")
                    indexList.append(currentIndex)
                elif(delimiter == currentNode.text[currentIndex]) and text_type == TextType.BOLD:
                    print(f"Found them at: {currentIndex}")
                    if currentNode.text[currentIndex + 1] == "*":
                        indexList.append(currentIndex)
                        indexList.append(currentIndex + 1)
            if(len(indexList)) == 2:
                returnList.append(TextNode(f'"{currentNode.text[:indexList[0]]}"',currentNode.text_type))
                returnList.append(TextNode(f'"{(currentNode.text[indexList[0] + 1:indexList[1]])}"',text_type))
                returnList.append(TextNode(f'"{(currentNode.text[indexList[1] + 1:])}"',currentNode.text_type))
            elif(len(indexList)) > 2:
                #Note for future, this is meant to index and append the bolded indexes  
                
            indexList = []
        print (returnList)
        print("Made it")
    print (f"Final return list: {returnList}")
    return returnList
    