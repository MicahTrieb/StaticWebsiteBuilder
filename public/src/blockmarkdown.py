import re

def markdown_to_blocks(inputString):
    return [block.strip() for  block in inputString.split("\n\n")]


def block_to_blocktype(inputBlock):
    headerRegex = re.findall(r"^#+(?= )", inputBlock)
    #print(headerRegex)
    if headerRegex:
        return "header"
    else:
        return "normal"