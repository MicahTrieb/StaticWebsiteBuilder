from htmlnode import LeafNode, HTMLNode, ParentNode
from textnode import *
#I made it too complicated, restarting from scratch, naming this OLDTWO
#This function is so I can recursively append to the list
def nesting_split_function(nestingList, indexList, theNode, text_type, currentReturnList):
    if not isinstance(nestingList, list) or not isinstance(indexList, list):
        raise Exception("The nesting list or the index list were not a list type")
    if nestingList and indexList:
        print(f"This is the nesting list: {nestingList}\n")
        print(f"This is the index list: {indexList}\n")
#Commenting this here for reference
#TextNode(f'"{currentNode.text[:indexList[0]]}"',currentNode.text_type))
#checking the lower value between the first indexes of both lists
        if min(indexList[0],nestingList[0]) == indexList[0]:
            print (f"This functionality worked. Returning the first value between {indexList[0]} and {nestingList[0]}, which is {indexList[0]}")
            poppedList = indexList[:2]
            print(f"This is the popped index list: {poppedList}\n")
            indexList = indexList[2:]
            print(f"This is the index list after the current indexing have been removed: {indexList}")
            print(f"This is the node's text contents in the recursive function: {theNode.text}\n")
            currentReturnList.extend([
                TextNode(f'"{theNode.text[:poppedList[0]]}"',theNode.text_type),
                TextNode(f'"{theNode.text[poppedList[0] + 1:poppedList[1]]}"',text_type),

            ])
            
        elif min(indexList[0],nestingList[0]) == nestingList[0]:
            print (f"This functionality worked. Returning the first value between {indexList[0]} and {nestingList[0]}, which is {nestingList[0]}")
            poppedList = nestingList[:2]
            print(f"This is the popped nesting list: {poppedList}")
            nestingList = nestingList[2:]
            #Note for
            currentReturnList.extend([

            ])
        elif min(indexList[0],nestingList[0]) == nestingList[0] and min(indexList[0],nestingList[0]) == indexList[0]:
            raise Exception("Something terrible happened, index and nesting lists overlapped")
    elif nestingList:
        pass
    elif indexList: 
        pass
    elif indexList == [] and nestingList = []:
        return currentReturnList
    return nesting_split_function()


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
        if currentNode.text_type != TextType.NORMAL:
            returnList.append(currentNode)
        else:
            #Using range to parse through the indexes of the currentNode's letters
            for currentIndex in range(0,len(currentNode.text)):
                #Checks to see if there is a match and that the expected type is not BOLD
                if (delimiter == currentNode.text[currentIndex]) and text_type != TextType.BOLD:
                    print(f"Found {currentNode.text[currentIndex]} at: {currentIndex}")
                    #Checking for any nested text
                    if currentIndex + 1 < len(currentNode.text):
                        if currentNode.text[currentIndex + 1] == delimiter:
                            print(f"Nesting detected at: {currentIndex} and {currentIndex + 1}, changing variable \n")
                            if currentIndex in nestingList:
                                #Appending detected nesting then skipping the rest of the loop, as well as making sure duplicates don't get in
                                nestingList.append(currentIndex + 1)
                                continue
                            else:
                                #If duplicate is not detected, appends two numbers
                                nestingList.extend([
                                    currentIndex, currentIndex + 1
                                ])
                                continue
                    #Making sure it doesn't double count the one behind it too
                    if currentNode.text[currentIndex - 1] != delimiter:
                        indexList.append(currentIndex)
                        #If BOLD is wanted, this will find it and append it to currentIndex
                elif(delimiter == currentNode.text[currentIndex]) and text_type == TextType.BOLD:
                    print(f"Found them at: {currentIndex}")
                    if currentNode.text[currentIndex + 1] == "*":
                        indexList.append(currentIndex)
                #Checking to see if nestingList was appended to, if so, starts this loop
            if(nestingList):
                nesting_split_function(nestingList, indexList, currentNode, text_type, returnList)
                print(f"This is the nesting list: {nestingList}\n")
                print(f"This is the index list: {indexList}\n")
                if min(indexList[0],nestingList[0]) == indexList[0]:
                    print (f"This functionality worked. Returning the first value between {indexList[0]} and {nestingList[0]}, which is {indexList[0]}")

                elif min(indexList[0],nestingList[0]) == nestingList[0]:
                    print (f"This functionality worked. Returning the first value between {indexList[0]} and {nestingList[0]}, which is {nestingList[0]}")
                elif min(indexList[0],nestingList[0]) == nestingList[0] and min(indexList[0],nestingList[0]) == indexList[0]:
                    raise Exception("Something terrible happened, index and nesting lists overlapped")
            #Checking to make sure indexList is equal to two and it wasn't looking for bolded stuff
            elif(len(indexList)) == 2 and text_type != TextType.BOLD:
                returnList.append(
                    TextNode(f'"{currentNode.text[:indexList[0]]}"',currentNode.text_type))
                returnList.append(
                    TextNode(f'"{(currentNode.text[indexList[0] + 1:indexList[1]])}"',text_type))
                returnList.append(
                    TextNode(f'"{(currentNode.text[indexList[1] + 1:])}"',currentNode.text_type))
                indexList = []
            #Making sure the delimiter was an asterisk, and that it was looking for bold
            elif delimiter == "*" and text_type == TextType.BOLD and len(indexList) > 0:
                print("Index list: ", indexList)
                returnList.append(
                    TextNode(f'"{currentNode.text[:indexList[0]]}"',currentNode.text_type))
                returnList.append(
                    TextNode(f'"{(currentNode.text[indexList[0] + 2:indexList[1]])}"',text_type))
                returnList.append(
                    TextNode(f'"{(currentNode.text[indexList[1] + 2:])}"',currentNode.text_type))  
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
        #print (returnList)
        #print("Made it")
    for i in returnList:
        print(f"{i}\n")
    if returnList == []:
        return f'"{old_nodes.text}"',old_nodes.text_type
    return returnList
    
