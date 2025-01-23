    if os.path.isdir(dir_path_content):
        allContents = os.listdir(dir_path_content)
        #print(f"Current directory: {dir_path_content}")
        for currentItem in allContents:
            currentDirectory = os.path.join(dir_path_content, currentItem)
            print(f"Current Directory: {currentDirectory}")
            if os.path.isfile(currentDirectory):
                print(f"Wait a second... {currentDirectory}")
                generate_pages_recursive(currentDirectory, template_path, dest_dir_path)
            elif os.path.isdir(currentDirectory):
                newDirPath = os.path.join(dest_dir_path, currentItem)
                print(f"Making a directory at: {newDirPath}\n")
                os.makedirs(newDirPath)
                print("1")
                generate_pages_recursive(currentDirectory, template_path, dest_dir_path)
    elif os.path.isfile(dir_path_content):
        print(f"File detected at {dir_path_content}")
        print("2")
        try:
            print("2.1")
            with open(dir_path_content, "r") as temp_file:
                readFile = temp_file.read()
            extract_title(readFile)
            writingDirectory = os.path.join(dest_dir_path, dir_path_content)
            print(f"Writing directory here: {writingDirectory}")
            generate_page(writingDirectory, template_path, dest_dir_path)
            print ("2.2")
        except:
            print("BOFA")   
    #return contentDictionary