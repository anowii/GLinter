import os, subprocess, sys, shutil, stat 

#******************* COLORS  *******************#
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"
#***********************************************#

def validPath(dirPath):
    for root, dirs, files in os.walk(dirPath):
        print(root)       
        for dir in dirs:
            if not os.path.exists(root, dir):
                print(f"{RED}Error : Folder path does not found{RESET}")
                sys.exit(1)
    return 0

def validURL(git_url):

    clone_command = ["git", "clone", git_url, "GitFolder\\"]
    result = subprocess.run(clone_command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"{RED}Error :{RESET}", result.stderr)
        sys.exit(1)
    else:
        return result.returncode


def clean_folder():
    print("in clean folder")
    if os.path.exists("GitFolder"):
        if not os.path.exists("GitFolder"):
            return 
        else:
            for root, dirs, file in os.walk("GitFolder"):
                print(root,dirs,file)
                os.chmod(dirs, stat.S_IWRITE)
                for file in dirs:
                    os.chmod(file, stat.S_IWRITE)
                    os.remove(file)
                #if(dirs == ".git"):
                #    for file in dirs:
                #        os.chmod(dirs, stat.S_IWRITE)
                #        try:
                #            shutil.rmtree(file)
                #        except Exception as e:
                #            print(f"Failed to delete folder contents: {e}")
                #try:
                #    shutil.rmtree(dirs)
                #except Exception as e:
                #    print(f"Failed to delete folder contents: {e}")
                
    return

def checkFile(filename, check_list):
    check_list[0] = checkREAD(filename)
    check_list[1] = checkLicense(filename)
    check_list[2] = checkGitIgnore(filename)
    check_list[3] = checkWorkFlows(filename)


def checkREAD(filename):
    return (filename == "README.md")

def checkLicense(filename):
    return (filename == "LICENSE")

def checkGitIgnore(filename):
    return (filename == ".gitignore")

def checkWorkFlows(filename):
    return (filename == "build.yml")


def printResults(check_list, test_files):
    if(check_list[0] == 1):
        print(" README.md", " "* 8 , "| OK")
    else:
        print(" README.md", " "*7 , "| N/A")

    if(check_list[1] == 1):
        print(" LICENSE:", " "* 9 , "| OK")
    else:
        print(" LICENSE:"," "* 9 ," | N/A")

    if(check_list[2] == 1):
        print(" .gitignore:", " "* 6 , "| OK")
    else:
        print(" .gitignore:", " "*6 , "| N/A")

    if(check_list[3] == 1):
        print(" workflow:"," "* 8 , "| OK")
    else:
        print(" Workflow:"," "* 8 , "| N/A")  

    print("-" * 30, "")
    if(test_files):
        print(" Filename w/ test: ")
        for file in test_files:
            print(f"   {file}")
    else:
        print(" Filename w/ test:  N/A")