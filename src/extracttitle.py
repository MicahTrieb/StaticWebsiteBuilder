#Start here
import re

def extract_title(markdown):
    brokenFile = markdown.split("\n")
    counter = 0
    firstHeader = ""
    for currentLine in brokenFile:
        while not firstHeader and counter < len(brokenFile):
            #print(f"Current line: {currentLine}")
            firstHeader = re.findall(r"^(#\s)", currentLine)
            counter += 1
        if firstHeader:
            return currentLine.lstrip("# ")
    raise Exception("No first header found")