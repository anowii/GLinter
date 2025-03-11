import os, subprocess, re

#***** COLORS  ******#
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"
#********************#

def validPath(target_folder):
    ''' Checks if the path is valid '''
    if not os.path.exists(target_folder):
       return False, f"{RED}Error (folder) : Folder path does not found{RESET}"
    else:
        return True, "Success"

def cloneURL(git_url):
    clean_folder(target_folder="ClonedRepo")
    if(re.match(r"^http", git_url)):
        clone_command = ["git", "clone", git_url, "ClonedRepo"]
        result = subprocess.run(clone_command, capture_output=True, text=True)
        return result.returncode == 0, result.stderr
    else: 
        return False, f"{RED}Error (url) : target is not a valid url{RESET}"

def clean_reports():
    rm_command = ["rm","-rf","Reports"]
    try:    
        if os.path.isdir("Reports"):
            subprocess.run(rm_command, check=True, capture_output=True,text=True)
        os.makedirs("Reports")
    except Exception:
        print("REPORT CLEANING FAILED")


def clean_folder(target_folder):    
    rm_command = ["rm", "-rf", target_folder]
    try:    
        if os.path.isdir(target_folder):
            subprocess.run(rm_command, check=True, capture_output=True,text=True)
    except Exception:
        print("REPORT CLEANING FAILED")

def printBanner(text: str):
    text_len = 85-len(text)
    print(f"| {text}", " "*text_len, "|") 

def printLines(text:str, len:int):
    print(text*len)

def printSpecialBanner(text: str):
    text_len = 94-len(text)
    print(f"| {text}", " "*text_len, "|") 

def is_file_empty(target_path):
    """Returns True if the file is empty, False otherwise."""
    if os.path.getsize(target_path) == 0:
        return 0.5
    else:
        #print(target_path,  os.path.getsize(target_path))
        return 1
    
def is_git_repo(target_path):
    """ Run 'git status' in the target-path """
    try:
        subprocess.run(
            ['git', 'status'],
            capture_output=True,  
            text=True,            
            check=True,           
            cwd=target_path    
        )
        return True
    except:
        return False
    
