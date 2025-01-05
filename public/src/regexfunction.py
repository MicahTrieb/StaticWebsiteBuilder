import re


def extract_markdown_images(text):
    returnList = []
    #matches = re.findall(r"!\[([^\]]+)\]", text)
    #otherMatches = re.findall(r"\(([^\)]+)\)", text)
    matches = re.findall(r"!\[([^\]]+)\]\(([^\)]+)\)", text)
    print(f"Post regex matches: {matches}\n\n")
    #while matches and otherMatches:
    while matches:
        print (f"Popping {matches[0]} off of {matches}\n\n")
        poppedMatches = matches.pop(0)
        print (f"{poppedMatches} successfully popped, leaving {matches}\n\n")
        returnList.append(
            (poppedMatches[0],
            poppedMatches[1])
        )
        print (f"Post popping and appending, resulting in {returnList}\n\n")
        
    return returnList
def extract_markdown_link(text):
    returnList = []
    matches = re.findall(r"\[([^\]]+)\]", text)
    otherMatches = re.findall(r"\(([^\)]+)\)", text)
    #print(f"Post regex matches: {matches}\n Post regex other matches: {otherMatches}\n")
    while matches and otherMatches:
        returnList.append((matches.pop(0),otherMatches.pop(0)))    
    return returnList

