import os
import shutil
import re
def directory_copy(movingDirectory, targetDirectory):
    possibleYes = ["Yes", "Y", "yes", "y", "YES"]
    if os.path.exists(targetDirectory) == False:
        createAnswer = ""
        possibleNo = ["No", "no", "N", "n", "NO"]
        possibleAnswers = possibleNo + possibleYes
        #while createAnswer not in possibleAnswers:
            #createAnswer = input(f"Directory not found, would you like to create directory {targetDirectory}?\n")
        #if createAnswer in possibleNo:
            #raise Exception("Target directory does not exist")
        if True:# createAnswer in possibleYes:
            os.mkdir(targetDirectory)
            copying_function(movingDirectory, targetDirectory)
    else:
        #deleteAnswer = input(f"Warning, this will delete {targetDirectory}, are you sure? \n")
        if True:#deleteAnswer in possibleYes:
            shutil.rmtree(targetDirectory)
            os.mkdir(targetDirectory)
            copying_function(movingDirectory, targetDirectory)

        else:
            raise Exception("Directory will not be deleted")
    
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