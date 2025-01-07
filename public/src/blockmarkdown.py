
def markdown_to_blocks(inputString):
    print("Ran successfully")
    return [block.strip() for  block in inputString.split("\n\n")]