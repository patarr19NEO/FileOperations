import os, sys, shutil

class FileOperarions():
    def __init__(self):
        self.current_dir = os.getcwd()

    def createFolder(self, folder_name):
        try:
            os.mkdir(f"{self.current_dir}/{folder_name}")
            return f"Folder {folder_name} was succesfully created in path {self.current_dir}"
        except Exception as e:
            return f"Failed. Error: {e}"

    def createFile(self, file_name):
        try:
            with open(file_name, "w") as file:
                file.write("")
            return f"File {file_name} was succesfully created in {self.current_dir}"
        except Exception as e:
            return f"Failed. Error: {e}"

    def openFolder(self):
        pass

    def openFile(self):
        pass

    def copyFiles(self):
        pass

    def showOS(self):
        pass

fo = FileOperarions()

if __name__ == '__main__':
    user_input = input()
    if user_input.startswith("fileops create -fol"):
        _, _, _, folder_name = user_input.split()
        fo.createFolder(folder_name)
    elif user_input.startswith("fileops create -fil"):
        _, _, _, file_name = user_input.split()
        fo.createFile(file_name)