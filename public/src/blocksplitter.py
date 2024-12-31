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
    boldDetected = 0
    calculatedIndexList = []
    splitNodes = list(old_nodes.text)
    stringNodes = old_nodes.text
    returnNodeList = []
    #Checking to see if delimiter was passed as bold
    if delimiter == "**":
        while currentIndex < len(splitNodes):
            #Since we checked if it was a bold delimiter, we can skip over bold vs italic check
            if stringNodes[currentIndex == delimiter]:
                print("Definite bold detected")
                boldDetected = 1
                if stringNodes[currentIndex + 1] == delimiter:
                    currentIndex += 2
                    calculatedIndexList.append(currentIndex)
                    calculatedIndexList.append(currentIndex + 1)
                #Checking infront and behind the asterisk to make sure we didn't land on a weird index
                elif (stringNodes[currentIndex - 1] == delimiter):
                    currentIndex += 1
                    calculatedIndexList.append(currentIndex)
                    calculatedIndexList.append(currentIndex - 1)
    #Checking all other delimiters, even bold if a single asterisk was passed through
    else:
        while currentIndex < len(stringNodes):
            #iterating through the list to find the index 
            if stringNodes[currentIndex] == delimiter:
                #checking to see if it's bold instead of italics
                if stringNodes[currentIndex + 1] == delimiter and delimiter == "*":
                    print("Possible BOLD detected")
                    boldDetected = 1
                    calculatedIndexList.append(currentIndex)
                    calculatedIndexList.append(currentIndex + 1)
                    currentIndex += 2
                #if it is not bold, adding the index to the list to scan through at the end
                else:
                    calculatedIndexList.append(currentIndex)
                    currentIndex += 1
            print(calculatedIndexList,stringNodes[currentIndex])
            currentIndex += 1
    if len(calculatedIndexList) == 2:
        returnNodeList.append(TextNode(stringNodes[:(calculatedIndexList[0])],old_nodes.text_type))
        returnNodeList.append(TextNode("".join(stringNodes[calculatedIndexList[0]:calculatedIndexList[1]]),text_type))
        returnNodeList.append(TextNode(stringNodes[(calculatedIndexList[1] + 1):],old_nodes.text_type))

        print((stringNodes[(calculatedIndexList[1] + 1):]))
        print ((stringNodes[:(calculatedIndexList[0])]))
    if boldDetected == 1 and len(calculatedIndexList) == 4:
        print(stringNodes[:(min(calculatedIndexList[0],calculatedIndexList[1]))])
        print(stringNodes[(max(calculatedIndexList[2],calculatedIndexList[3]) + 1):])
    print (len(calculatedIndexList))
    print (returnNodeList)
    return (returnNodeList)






    

    