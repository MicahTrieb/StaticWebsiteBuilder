import re


def extract_markdown_images(text):
    returnList = []
    #matches = re.findall(r"!\[([^\]]+)\]", text)
    #otherMatches = re.findall(r"\(([^\)]+)\)", text)
    matches = re.findall(r"!\[([^\]]+)\]\(([^\)]+)\)", text)
    print(f"Post regex matches: {matches}")
    #while matches and otherMatches:
    for match in matches:
        print (match)
        returnList.append(
            (match[0],
            match[1])
        )
        
    return returnList
def extract_markdown_link(text):
    returnList = []
    matches = re.findall(r"\[([^\]]+)\]", text)
    otherMatches = re.findall(r"\(([^\)]+)\)", text)
    #print(f"Post regex matches: {matches}\n Post regex other matches: {otherMatches}\n")
    while matches and otherMatches:
        returnList.append((matches.pop(0),otherMatches.pop(0)))    
    return returnList

