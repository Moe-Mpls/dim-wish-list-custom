import shutil


def main():
    # Paths for files
    voltronFile = "./dim-wish-list-sources/voltron.txt"
    # voltronFile = "./dim-wish-list-sources/choosy_voltron.txt"
    customFile = "./customList.txt"
    finalFile = "./finalList.txt"

    # Clear finalFile
    with open(finalFile, mode='w') as clearFile:
        pass

    # Bulk copy Voltron source
    try:
        shutil.copy(voltronFile, finalFile)

        print("File copied successfully.")
    except:
        print("Error occurred while copying file.")

    # Append custom list
    try:
        with open(customFile, mode='r') as sourceFile:
            with open(finalFile, mode='a') as targetFile:
                shutil.copyfileobj(sourceFile, targetFile)

        print("File copied successfully.")
    except:
        print("Error occurred while copying file.")


main()
