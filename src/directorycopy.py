import os
import shutil
import re
def directory_copy(movingDirectory, targetDirectory):
    possibleYes = ["Yes", "Y", "yes", "y", "YES"]
    if os.path.exists(targetDirectory) == False:
        createAnswer = ""
        possibleNo = ["No", "no", "N", "n", "NO"]
        possibleAnswers = possibleNo + possibleYes
        os.mkdir(targetDirectory)
        copying_function(movingDirectory, targetDirectory)
    else:
        shutil.rmtree(targetDirectory)
        os.mkdir(targetDirectory)
        copying_function(movingDirectory, targetDirectory)
    
def copying_function(movingDirectory, targetDirectory):
    listToBeCopied = os.listdir(movingDirectory)
    #print(f"Full directory list: {listToBeCopied}")
    for currentDirectory in listToBeCopied:
        #print(f"Current directory: {currentDirectory}")
        copyingThis = os.path.join(movingDirectory, currentDirectory)
        #print (f"Current file path: {copyingThis}")
        if os.path.isdir(copyingThis) == True:
            #print (f"Directory detected at {copyingThis}")
            newDirectory = os.path.join(targetDirectory, currentDirectory)
            os.mkdir(newDirectory)
            copying_function(copyingThis, os.path.join(targetDirectory, currentDirectory))
        elif os.path.isfile(copyingThis) == True:
            #print (f"File detected at: {copyingThis}")
            #print (f"Copying file to {targetDirectory} from {copyingThis}")
            shutil.copy(copyingThis, targetDirectory)
        #shutil.copy(copyingThis, targetDirectory)