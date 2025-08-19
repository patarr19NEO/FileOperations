import os, shutil, sys, time

"""def copy_files(path):
    try:
        shutil.copy("main.py", f"{path}\\FileOperations")
        if str(sys.platform) == "linux":
            shutil.copy("fileops.bat", "./usr/bin/FileOperations")
        elif str(sys.platform) == "win32":
            shutil.copy("fileops.bat", "C:\\Windows\\System32\\FileOperations")
        else:
            print("You used unknow OS. Install failed")
    except Exception as e:
        print(f"Unknow Error: {e}")"""

if __name__ == '__main__':
    try:
        print("It is a installer of FileOps SW\n")
        try:
            os.system("python --version")
        except:
            print("You don't have Python. Please, install Python3.x to install FileOps")
            input()
            sys.exit(1)
        current_directory = os.getcwd()
        install_path = input(f"Input installation path. Or press Enter to install in your current directory[{os.path.join(current_directory, 'FileOps')}]")
        if not install_path:
            install_path = os.path.join(current_directory, "FileOps")
        try:
            os.makedirs(install_path, exist_ok=True)
        except Exception as e:
            print("Failed. Error: ", e)
            input()
            sys.exit(1)
        files_for_copy = ["main.py", "installer.py"]
        try:
            for file in files_for_copy:
                if not os.path.exists(file):
                    print("Files not found.")
                    sys.exit(1)
                else:
                    shutil.copy(file, install_path)
        except Exception as e:
            print(f"Failed. Error: {e}")
            input()
            sys.exit(1)
        print(f"Congratulations. You've successfully installed FileOps\nNow You can start:\ncd /d {install_path}\nfileops")
    except Exception as e:
        print(f"Failed. Error: {e}")
        input()
        sys.exit(1)