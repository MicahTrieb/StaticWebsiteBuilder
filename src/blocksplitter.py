#third times the charm :)
#for currentWord in previousSentence:
#if currentWord == "third":
#currentWord == "forth"
from htmlnode import LeafNode, HTMLNode, ParentNode
from textnode import TextType, TextNode
from regexfunction import extract_markdown_images, extract_markdown_link
import re
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    returnList = []
    for currentNode in old_nodes:
        if currentNode.text_type != TextType.NORMAL:
            returnList.append(currentNode)
        else:
            splitString = currentNode.text.split(delimiter)
            if splitString and len(splitString) != 2:
                for currentIndex in range(0, len(splitString)):
                    if currentIndex == 0 or currentIndex == len(splitString) - 1:
                        if splitString[currentIndex] == "":
                            continue
                    if currentIndex % 2 == 0:
                            returnList.append(TextNode(f"{splitString[currentIndex]}",TextType.NORMAL))
                    else:
                            returnList.append(TextNode(f"{splitString[currentIndex]}", text_type))

            
            elif (len(splitString) == 2) and splitString:
                raise Exception("Unmatched delimiter")
            else:
                returnList.append(currentNode)
    return (returnList)
        


def split_nodes_image(old_nodes):
    returnList = []
    textList = []
    for currentNode in old_nodes:
        #print(f"Current Node here: {currentNode}")
        preImageRegexed = re.findall(r"(^.+)(?=\!\[[^\]]+\]\([^\)]+\))", currentNode.text)
        imageExistenceCheck = re.findall(r"\!\[([^\]]+)\]\([^\)]+\)", currentNode.text)
        if not preImageRegexed and not imageExistenceCheck:
            returnList.append(currentNode)
            #print(f"Continuing here with {currentNode}")
            continue
        #print(f"Pre Image Regex here: {preImageRegexed}\nImage Exists here: {imageExistenceCheck}\n")
        splitImageText = re.split(r"!\[([^\)]+)\)",currentNode.text)
        #print (f"split Image Text Here: {splitImageText} with Node {currentNode} containing {currentNode.text}")
        for currentIndex in range(0, len(splitImageText)):
            if currentIndex == 0 or currentIndex == len(splitImageText) - 1:
                if splitImageText[currentIndex] == "":
                    #print(f"Empty index detected at {[currentIndex]}")
                    continue
            if currentIndex % 2 == 0:
                #print(f"Normal texttype detected here: {splitImageText[currentIndex]}")
                textList.extend([
                    TextNode(splitImageText[currentIndex], TextType.NORMAL)
                ])
            else:
                imageRegex = re.findall(r"!\[([^\]]+)\]\(([^\)]+)\)",currentNode.text)
                #print(f"Image Regex Here: {imageRegex}")
                textList.extend([
                    TextNode(imageRegex[0][0], TextType.IMAGES, imageRegex[0][1])
                ])       
        returnList.extend(textList)
        textList = []
    return returnList
#Code redone using re.split instead 
def split_nodes_link(old_nodes):
    returnList = []
    textList = []
    for currentNode in old_nodes:
        #Checking to make sure there's a link in the currentNode's text
        preLinkRegexed = re.findall(r"(^.+)(?=\[[^\]]+\]\([^\)]+\))", currentNode.text)
        linkExistenceCheck = re.findall(r"(?<!!)\[([^\]]+)\]", currentNode.text)
        if not preLinkRegexed and not linkExistenceCheck:
            returnList.append(currentNode)
            continue
        #Splitting the text by the link regex
        splitNodeText = re.split(r"(?<!!)(\[[^\)]+\))", currentNode.text)
        for currentIndex in range(0, len(splitNodeText)):
                #Checking to see if the beginning or end is empty, incase the regex is at the beginning/end
                if currentIndex == 0 or currentIndex == len(splitNodeText) - 1:
                    if splitNodeText[currentIndex] == "":
                        continue
                if currentIndex % 2 == 0:
                    textList.extend([
                        TextNode(splitNodeText[currentIndex], TextType.NORMAL)]) 
                else:
                    linkRegex = re.findall(r"\[([^\]]+)\]\(([^\)]+)\)", splitNodeText[currentIndex].strip("'"))
                    textList.extend([
                    TextNode(linkRegex[0][0], TextType.LINKS, linkRegex[0][1])
                ])
        returnList.extend(textList)
        textList = []
    return returnList

def text_to_textnodes(text):
    #print("1")
    if not text:
        return []
    parsingTextNode = [TextNode(text, TextType.NORMAL)]
    #print (f"PARSING NODE OUTPUT HERE: {parsingTextNode}\n\n\n")
    if (split_nodes_image(parsingTextNode)):
        #print("2")
        #print(f"Split node image return here: {split_nodes_image(parsingTextNode)}")
        returnNodes = split_nodes_image(parsingTextNode)
    else:
        returnNodes = parsingTextNode
        #print("3")
    #print (f"RETURN NODE HERE:\n {returnNodes}\n\n\n")
    if split_nodes_link(returnNodes):
        returnNodes = split_nodes_link(returnNodes)

    #print (f"LINK PULLED RETURN NODES: {returnNodes}\n")
    runningList = []
    currentContent = split_nodes_delimiter(returnNodes, "**", TextType.BOLD)
    newList = split_nodes_delimiter(currentContent, "*", TextType.ITALIC)
    newList2 = split_nodes_delimiter(newList, "`", TextType.CODE)
    return newList2

def simple_parser(self):
    pass

def regex_split_test(text):
   #return(re.split(r"(?<!!)\[([^\]]+)\]\(([^\)]+)\)", text))  
   return (re.split(r"(?<!!)\[([^\)]+)\)", text))