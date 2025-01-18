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
    for currentNode in old_nodes:
        textList = []
        regexedList = []
        regexDictionary = {}
        #print(currentNode)
        #print (extract_markdown_images(currentNode.text))
        regexedImages = extract_markdown_images(currentNode.text)
        if regexedImages:
            for currentImageRegex in regexedImages:
                regexDictionary[currentImageRegex[0]] = currentImageRegex[1]
        #print (regexDictionary)
        preLinkRegexed = re.findall(r"(.+)(?=\!\[.+\])", currentNode.text)
        linkExistanceCheck = re.findall(r"!\[([^\]]+)\]", currentNode.text)
        if not preLinkRegexed and not linkExistanceCheck:
            returnList.append(currentNode)
            continue
        #print (preLinkRegexed)
        matchList = []
        for match in re.finditer((r"!\[([^\]]+)\]"), currentNode.text):
            matchList.append((match.start(), match.group(0), 'image'))
        for match in re.finditer((r"([\w\s*`.]+?)(?=\!\[[^\]]+\]\([^\)]+\)|\[[^\]]+\]\([^\)]+\)|$)"), currentNode.text):
            matchList.append((match.start(), match.group(0), 'text'))
        for match in re.finditer((r"(?<!!)\[([^\]]+)\]\(([^\)]+)\)"), currentNode.text):
            matchList.append((match.start(), match.group(0), 'text'))
        matchList.sort(key=lambda x: x[0])
        #print(f"Image matches: {[(m.start(), m.group(0)) for m in re.finditer(r'!\[([^\]]+)\]', currentNode.text)]}")
        #print(f"Text matches: {[(m.start(), m.group(0)) for m in re.finditer(r'([\w\s*`.]+?)(?=\!\[[^\]]+\]\([^\)]+\)|\[[^\]]+\]\([^\)]+\)|$)', currentNode.text)]}")
        #print(f"Link matches: {[(m.start(), m.group(0)) for m in re.finditer(r'(?<!!)\[([^\]]+)\]\(([^\)]+)\)', currentNode.text)]}")

        for currentMatch in matchList:
            #print(f"Current match here: {currentMatch}\n")
            #print (f"Regex dictionary here: {regexDictionary}\n")
            #print (f"Full match list here: {matchList}\n")
            if currentMatch[2] == 'text' and currentMatch[1]:
                textList.extend([
                    TextNode(currentMatch[1], TextType.NORMAL)
                ])
                #print ("Text extended")
            if currentMatch[2] == 'image' and currentMatch[1]:
                dictionaryIndexer = currentMatch[1].strip("![]")
                
                textList.extend([
                    TextNode(dictionaryIndexer, TextType.IMAGES, regexDictionary[dictionaryIndexer])
                ])
                #print ("Image link extended")
        #print (f"Current match list: {matchList}")
        returnList.extend(textList)
        textList = []
        regexDictionary = {}
    return returnList

def split_nodes_link(old_nodes):
    returnList = []
    print (old_nodes)
    for currentNode in old_nodes:
        textList = []
        regexedList = []
        regexDictionary = {}
        print(f"Current node's text: {currentNode.text}")
        regexedLinks = extract_markdown_link(currentNode.text)
        print(f"Regexed Links: {regexedLinks}")
        if regexedLinks:
            for currentLinkRegex in regexedLinks:
                regexDictionary[currentLinkRegex[0]] = currentLinkRegex[1]
                print (regexDictionary)
        preLinkRegexed = re.findall(r"(^.+)(?=\[[\w\s]\]\([\w\s]+\))", currentNode.text)
        linkExistanceCheck = re.findall(r"\[([^\]]+)\]", currentNode.text)
        if not preLinkRegexed and not linkExistanceCheck:
            returnList.append(currentNode)
            continue
        matchList = []
        for match in re.finditer(r"(?<!!)\[([\w\s$-/:-?{-~!\"])+(?=\])\]", currentNode.text):
            matchList.append((match.start(), match.group(0), 'link'))
        for match in re.finditer((r"(?<!\])[\w\s.'*\(\)]+(?=\[|$)"), currentNode.text):
            matchList.append((match.start(), match.group(0), 'text'))
        matchList.sort(key=lambda x: x[0])
        #print(f"Current match list: {matchList}\n")
        for currentMatch in matchList:
            if currentMatch[2] == 'text' and currentMatch[1].strip():
                textList.extend([
                    TextNode(currentMatch[1], TextType.NORMAL)
                ])
            if currentMatch[2] == 'link' and currentMatch[1].strip():
                dictionaryIndexer = currentMatch[1].strip("[]")
                textList.extend([
                    TextNode(dictionaryIndexer, TextType.LINKS, regexDictionary[dictionaryIndexer])
                ])
        #print (matchList)
        #print (f"Final return list: {textList}")
        returnList.extend(textList)
        textList = []
    return returnList

def text_to_textnodes(text):
    print("1")
    if not text:
        return []
    parsingTextNode = [TextNode(text, TextType.NORMAL)]
    print (f"PARSING NODE OUTPUT HERE: {parsingTextNode}\n\n\n")
    if (split_nodes_image(parsingTextNode)):
        print("2")
        print(f"Split node image return here: {split_nodes_image(parsingTextNode)}")
        returnNodes = split_nodes_image(parsingTextNode)
    else:
        returnNodes = parsingTextNode
        print("3")
    print (f"RETURN NODE HERE:\n {returnNodes}\n\n\n")
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