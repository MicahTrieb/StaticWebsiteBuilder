from htmlnode import LeafNode, HTMLNode, ParentNode
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    print(f"These are the old nodes before entering the code: {old_nodes}\n")
    #Making sure delimiter and text_type are valid before entering code loop
    if delimiter == None or delimiter == "":
        return old_nodes
    if text_type == None or text_type == "":
        raise Exception("Text type is required for delimiter")
    if not isinstance(old_nodes,list):
        raise Exception("Old Nodes must be in a list")
    #Establishing empty lists to be used later
    indexList = []
    returnList = []
    nestingList = []
    #Iterating through every node sent through, 
    for currentNode in old_nodes:
        print(f"This is the current node in the for loop: {currentNode}\n")
        print(f"This is the current text of the node: {currentNode.text}\n")
        #Returning the node as is if the wanted text type is NORMAL
        if (delimiter == "**"):
            delimiter = "*"
        if currentNode.text_type != TextType.NORMAL:
            returnList.append(currentNode)

        else:
            #Using range to parse through the indexes of the currentNode's letters
            for currentIndex in range(0,len(currentNode.text)):
                #Checks to see if there is a match and that the expected type is not BOLD
                if (delimiter == currentNode.text[currentIndex]) and text_type != TextType.BOLD:
                    print(f"Found {currentNode.text[currentIndex]} at: {currentIndex}")
                    indexList.append(currentIndex)
                elif(delimiter == currentNode.text[currentIndex]) and text_type == TextType.BOLD:
                    print(f"Found them at: {currentIndex}")
                    if currentNode.text[currentIndex + 1] == "*":
                        indexList.append(currentIndex)
            if(indexList == []):
                returnList.append(TextNode(f'"{currentNode.text}"',currentNode.text_type))
            if(len(indexList)) % 2 != 0:
                raise Exception("Unmatched delimiters") 
            elif(len(indexList)) == 2 and text_type != TextType.BOLD:
                print("Not bold\n")
                returnList.append(
                    TextNode(f'"{currentNode.text[:indexList[0]]}"',currentNode.text_type))
                returnList.append(
                    TextNode(f'"{(currentNode.text[indexList[0] + 1:indexList[1]])}"',text_type))
                returnList.append(
                    TextNode(f'"{(currentNode.text[indexList[1] + 1:])}"',currentNode.text_type))
                
                indexList = []
            #Making sure the delimiter was an asterisk, and that it was looking for bold
            elif (delimiter == "**" or delimiter == "*") and text_type == TextType.BOLD:
                print("Index list: ", indexList)
                print("\nBold")
                returnList.append(
                    TextNode(f'"{currentNode.text[:indexList[0]]}"',currentNode.text_type))
                returnList.append(
                    TextNode(f'"{(currentNode.text[indexList[0] + 2:indexList[1]])}"',text_type))
                returnList.append(
                    TextNode(f'"{(currentNode.text[indexList[1] + 2:])}"',currentNode.text_type))  
                print (f"Return List: {returnList}\n")
                indexList = []
            #Checking to see if the function picked up multiple copies, if so, makes sure they have pairs
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
                        print(f"This was one iteration of the nextCurrentIndex code: {returnList}\n",)
                        lastStop = nextStopValue
                        for i in returnList:    
                            print(f"{i}\n")
                    else:#(splitList[currentIndex]):
                        try:
                            returnList.extend([
                                TextNode(f'"{currentNode.text[splitList[currentIndex][0]+1:splitList[currentIndex][1]]}"',text_type),
                                TextNode(f'"{currentNode.text[splitList[currentIndex][1]+1]:}"',currentNode.text_type)])
                        except:
                            returnList.extend([
                                TextNode(f'"{currentNode.text[splitList[currentIndex][0]+1:splitList[currentIndex][1]]}"',text_type),
                            ])
           
                    for i in returnList:
                        print(f"{i}\n")
            return returnList
