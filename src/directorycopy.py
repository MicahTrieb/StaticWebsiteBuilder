import os
import shutil

def directory_copy(movingDirectory, targetDirectory):
    possibleYes = ["Yes", "Y", "yes", "y", "YES"]
    if os.path.exists(targetDirectory) == False:
        createAnswer = ""
        possibleNo = ["No", "no", "N", "n", "NO"]
        possibleAnswers = possibleNo + possibleYes
        while createAnswer not in possibleAnswers:
            createAnswer = input(f"Directory not found, would you like to create directory {targetDirectory}?")
        if createAnswer in possibleNo:
            raise Exception("Target directory does not exist")
        elif createAnswer in possibleYes:
            os.mkdir(targetDirectory)
    deleteDirectory = input(f"Warning, this will remove the target directory: {targetDirectory}, are you sure?")
    if deleteDirectory in possibleYes:
        shutil.rmtree(targetDirectory)
        listToBeCopied = os.listdir(movingDirectory)

    else:
        raise Exception("Directory will not be deleted")
    
def copying_function(movingDirectory, targetDirectory):
    listToBeCopied = os.listdir(movingDirectory)
    for currentDirectory in listToBeCopied:
        shutil.copy(currentDirectory, targetDirectory)