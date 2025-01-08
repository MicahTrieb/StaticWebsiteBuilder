import re

def markdown_to_blocks(inputString):
    return [block.strip() for  block in inputString.split("\n\n")]


def block_to_blocktype(inputBlock):
    headerRegex = re.findall(r"^#+(?= )", inputBlock)
    if headerRegex:
        return "header"
    codeBlock1 = re.findall(r"^`{3}", inputBlock)
    codeBlock2 = re.findall(r"`{3}(?=$)", inputBlock)
    if(codeBlock1 and codeBlock2):
        return "code"
    if inputBlock:
        unsortedLines = inputBlock.split("\n")
        if(unsortedLines):
            counter = 0
            for currentLine in unsortedLines:
                currentList = [(re.findall(r"^\-(?= )", currentLine)), (re.findall(r"^\*(?= )", currentLine))]
                if currentList[0] or currentList[1]:
                    counter += 1
        if counter == len(unsortedLines) and unsortedLines:
            return "unsorted list"
        if(unsortedLines):
            counter = 0
            for currentLine in unsortedLines:
                if (re.findall(r"^>", currentLine)):
                    counter += 1
            if counter == len(unsortedLines) and unsortedLines:
                return "quote block"
            counter = 1
            for currentLine in unsortedLines:
                if re.search(rf"^{counter}\. ", currentLine):
                    print (currentLine)
                    counter +=1 
                if counter == len(unsortedLines) - 1 and unsortedLines:
                    return ("sorted list")
            

    
    return "normal"