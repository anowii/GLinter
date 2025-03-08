
import os, subprocess, re

#******************* COLORS  *******************#
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"
#***********************************************#
#*************** WORKFLOW NAMES  ***************#
workflow_names = [ "build.yml",
                "workflow.yml", 
                "ci_pipeline.yml", 
                "deploy_pipeline.yml", 
                "test_workflow.yml", 
                "build_and_release.yml", 
                "code_quality.yml", "ci.yml", 
                "deploy.yml", 
                "release_workflow.yml", 
                "workflow_config.yml" ]
#***********************************************#

def validPath(target_folder):
    ''' Checks if the path is valid '''
    if not os.path.exists(target_folder):
       return False, f"{RED}Error (folder) : Folder path does not found{RESET}"
    else:
        return True, "Success"

def cloneURL(git_url):
    clone_command = ["git", "clone", git_url, "ClonedRepo"]
    result = subprocess.run(clone_command, capture_output=True, text=True)
    return result.returncode == 0, result.stderr


def clean_folder(target_folder):    
    command = ["rm", "-rf", target_folder]

    result = subprocess.run(
        command, 
        capture_output=True,
        text=True,
    )
    return result.returncode == 0, result.stderr



def getGitSummary(target_folder):
    log_command = [f"cd {target_folder} && git shortlog --summary --numbered --no-merges && cd .."]
    with open("gitstat.log", "w", encoding="utf-8") as f:
        result = subprocess.run(log_command, stdout=f, stderr=subprocess.PIPE, text=True, shell=True)   
    return result.returncode == 0, result.stderr

#              format = 87 - len(f"| {log[0]} {log[1]}")
#                    print(f"| {log[0]} {log[1]}", " "*format, "|") 

def printBanner(text: str):
    text_len = 85-len(text)
    print(f"| {text}", " "*text_len, "|") 

def printSpecialBanner(text: str):
    text_len = 94-len(text)
    print(f"| {text}", " "*text_len, "|") 

def is_file_empty(target_path):
    """Returns True if the file is empty, False otherwise."""
    if os.path.getsize(target_path) == 0:
        return 1
    elif os.path.getsize(target_path) > 0:
        return 2

def getNumberOfFiles(target_folder):
    count  = 0
    for root, dirs, files in os.walk(target_folder):
        count += len(files)
    return count
    
def getNumberOfFolders(target_folder):
    count  = 0
    for root, dirs, _ in os.walk(target_folder):
        count += len(dirs)
    return count


def getNumberOfTestFiles(target_folder):
    count  = 0
    for root, _, files in os.walk(target_folder):
        for filename in files:
            if(re.search("test", filename, re.IGNORECASE)):
                count += 1
    return count


        