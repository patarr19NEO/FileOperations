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
                file.write(" ")
            return f"File {file_name} was succesfully created in {self.current_dir}"
        except Exception as e:
            return f"Failed. Error: {e}"

    def openFolder(self, folder_name_for_opening):
        if not os.path.exists(folder_name_for_opening):
            return f"Folder {folder_name_for_opening} not found"
        try:
            os.startfile(folder_name_for_opening)
            return f"Folder {folder_name_for_opening} opened"
        except Exception as e:
            return f"Failed. Error: {e}"

    def openFile(self, file_name_for_opening):
        if not os.path.exists(file_name_for_opening):
            return f"File {file_name_for_opening} not found"
        try:
            os.startfile(file_name_for_opening)
            return f"File {file_name_for_opening} opened"
        except Exception as e:
            return f"Failed. Error: {e}"

    def copyFilesContent(self, from_file, to_file):
        if not os.path.exists(from_file):
            return f"File {from_file} doesn't exist"
        if not os.path.exists(to_file):
            return f"File {to_file} doesn't exist"
        try:
            with open(from_file, "w") as ff:
                ff_content = ff.read()
            with open(to_file, "w") as tf:
                tf.write(ff_content)
        except Exception as e:
            return f"Failed. Error: {e}"

    def showOS(self):
        return f"Your OS: {sys.platform()}"

fo = FileOperarions()

if __name__ == '__main__':
    while True:
        user_input = input()
        if user_input.startswith("fileops create -fol"):
            _, _, _, folder_name = user_input.split()
            print(fo.createFolder(folder_name))
        elif user_input.startswith("fileops create -fil"):
            _, _, _, file_name = user_input.split()
            print(fo.createFile(file_name))
        elif user_input.startswith("fileops open -fol"):
            _, _, _, folder_name_for_opening = user_input.split()
            print(fo.openFolder(folder_name_for_opening))
        elif user_input.startswith("fileops open -fil"):
            _, _, _, file_name_for_opening = user_input.split()
            print(fo.openFile(file_name_for_opening))
        elif user_input.startswith("fileops copy"):
            _, _, from_file, to_file = user_input.split()
            print(fo.copyFilesContent(from_file, to_file))
        elif user_input.startswith("fileops show -os"):
            print(fo.showOS())
        else:
            print("fileops: Invalid Command")