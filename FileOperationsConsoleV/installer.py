import os, shutil, sys

def check_python():
    try:
        result = os.system("python --version")
        return result == 0
    except:
        return False

def copy_files(path):
    try:
        shutil.copy("main.py", f"{path}\\FileOperations")
        if str(sys.platform) == "linux":
            shutil.copy("fileops.bat", "./usr/bin/FileOperations")
        elif str(sys.platform) == "win32":
            shutil.copy("fileops.bat", "C:\\Windows\\System32\\FileOperations")
        else:
            print("You used unknow OS. Install failed")
    except Exception as e:
        print(f"Unknow Error: {e}")

if __name__ == '__main__':
    print("It is a installer of FileOps SW\n")
    path_where_install = input("Input path where you want to install")
    copy_files(path_where_install)