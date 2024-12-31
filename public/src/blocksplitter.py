from htmlnode import LeafNode, HTMLNode, ParentNode
from textnode import *
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #Empty values being passed checks
    if delimiter == None or delimiter == "":
        return old_nodes
    if text_type == None or text_type == "":
        raise Exception("Text type is required for delimiter")
    #Counters for the while loop
    currentIndex = 0
    currentCounter = 0
    calculatedIndexList = []
    splitNodes = list(old_nodes)
    #Checking to see if delimiter was passed as bold
    if delimiter == "**":
        while currentIndex < len(splitNodes):
            #Since we checked if it was a bold delimiter, we can skip over bold vs italic check
            if splitNodes[currentIndex == delimiter]:
                print("Definite bold detected")
                if splitNodes[currentIndex + 1] == delimiter:
                    currentIndex += 2
                    calculatedIndexList.append(currentIndex)
                    calculatedIndexList.append(currentIndex + 1)
                #Checking infront and behind the asterisk to make sure we didn't land on a weird index
                elif (splitNodes[currentIndex - 1] == delimiter):
                    currentIndex += 1
                    calculatedIndexList.append(currentIndex)
                    calculatedIndexList.append(currentIndex - 1)
    #Checking all other delimiters, even bold if a single asterisk was passed through
    else:
        while currentIndex < len(splitNodes):
            #iterating through the list to find the index 
            if splitNodes[currentIndex] == delimiter:
                #checking to see if it's bold instead of italics
                if splitNodes[currentIndex + 1] == delimiter and delimiter == "*":
                    print("Possible BOLD detected")
                    calculatedIndexList.append(currentIndex)
                    calculatedIndexList.append(currentIndex + 1)
                    currentIndex += 2
                else:
                    calculatedIndexList.append(currentIndex)
                    currentIndex += 1
            currentIndex += 1


    pass