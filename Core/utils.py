import os, subprocess, re, argparse

#***** COLORS  ******#
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"
#********************#

def validPath(target_folder:str):
    ''' Checks if the path is valid '''
    isFound = os.path.exists(target_folder)
    if (isFound == False):
       return isFound, f"{RED}Error (folder) : Folder path not found{RESET}"
    else:
        return isFound, "Success"

def cloneURL(git_url, target_path):
    clean_folder(target_folder=target_path)
    if(re.match(r"^http", git_url)):
        clone_command = ["git", "clone", git_url, target_path]
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
        print(f"{target_folder} CLEANING FAILED")

def is_folder_empty(target_path):
    return not os.listdir(target_path)

def is_file_empty(target_path):
    """Returns True if the file is empty, otherwise False"""
    if os.path.getsize(target_path) == 0:
        return True
    else:
        return False
    
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
    
def parse_init():
    """Argument parsing and return parsed arguments."""
    parser = argparse.ArgumentParser(description="Process a url to a git repo or a path to a local folder, choose one.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", help="URL to git repo", type=str)
    group.add_argument("--dir", help="Path to folder", type=str)
    return parser, parser.parse_args()

def validate_action(prompt):
    """Ask for validation."""
    while True:
        response = input(f"{prompt} [Y/N]: ")
        if response == "y":
            return True
        elif response == "n":
            print("Operation canceled.")
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

###########################################
#        PRINTING FUNCTIONS               #
###########################################

def printWelcomeBanner():
    print("=" * 90, "")
    print( "\t\t\t  Welcome to the GLinter Tool!")
    print("=" * 90, "")

def printLineBanner(prompt:str):
    printLines("-",90)
    printBanner(f"{prompt}")
    printLines("-",90)

def printStripeBanner(prompt:str):
    print("\n")
    print("=" * 90)
    printBanner(f"{prompt}")  
    print("=" * 90)

def printBanner(text: str):
    text_len = 85-len(text)
    print(f"| {text}", " "*text_len, "|") 

def printLines(text:str, len:int):
    print(text*len)

def printSpecialBanner(text: str):
    text_len = 94-len(text)
    print(f"| {text}", " "*text_len, "|") 