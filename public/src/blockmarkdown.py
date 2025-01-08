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
    unsortedLines = inputBlock.split("\n")
    counter = 0
    if(unsortedLines):
        for currentLine in unsortedLines:
            currentList = [(re.findall(r"^\-(?= )", currentLine)), (re.findall(r"^\*(?= )", currentLine))]
            if currentList[0] or currentList[1]:
                counter += 1
    if counter == len(unsortedLines):
        return "unsorted list"

    else:
        return "normal"