import os
import shutil

def directory_copy(movingDirectory, targetDirectory):
    possibleYes = ["Yes", "Y", "yes", "y", "YES"]
    if os.path.exists(targetDirectory) == False:
        createAnswer = ""
        possibleNo = ["No", "no", "N", "n", "NO"]
        possibleAnswers = possibleNo + possibleYes
        while createAnswer not in possibleAnswers:
            createAnswer = input(f"Directory not found, would you like to create directory {targetDirectory}?\n")
        if createAnswer in possibleNo:
            raise Exception("Target directory does not exist")
        elif createAnswer in possibleYes:
            os.mkdir(targetDirectory)
            copying_function(movingDirectory, targetDirectory)
    else:
        deleteAnswer = input(f"Warning, this will delete {targetDirectory}, are you sure? \n")
        if deleteAnswer in possibleYes:
            shutil.rmtree(targetDirectory)
            os.mkdir(targetDirectory)
            copying_function(movingDirectory, targetDirectory)

        else:
            raise Exception("Directory will not be deleted")
    
def copying_function(movingDirectory, targetDirectory):
    listToBeCopied = os.listdir(movingDirectory)
    for currentDirectory in listToBeCopied:
        print(currentDirectory)
        shutil.copy(currentDirectory, targetDirectory)