
import os, subprocess, re

#******************* COLORS  *******************#
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"
#***********************************************#
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

def checkSecurity(target_folder):
    command = ["gitleaks", "detect", "-v", "--report-path", "gitleaks-report.json", "--source", target_folder]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.returncode == 0, result.stderr


def clean_folder(target_folder):    
    command = ["rm", "-rf", target_folder]

    result = subprocess.run(
        command, 
        capture_output=True,
        text=True,
    )
    return result.returncode == 0, result.stderr


def checkFile(filename, check_list):
    if checkREAD(filename):
        check_list[0] = checkREAD(filename)
    elif checkLicense(filename):
        check_list[1] = checkLicense(filename)
    elif checkGitIgnore(filename):
        check_list[2] = checkGitIgnore(filename)

def getGitSummary(target_folder):
    log_command = [f"cd {target_folder} && git shortlog --summary --numbered --no-merges && cd .."]
    with open("gitstat.log", "w", encoding="utf-8") as f:
        result = subprocess.run(log_command, stdout=f, stderr=subprocess.PIPE, text=True, shell=True)   
    return result.returncode == 0, result.stderr


def getNumberOfFiles(target_folder):
    count  = 0
    for root, dirs, files in os.walk(target_folder):
        count += len(files)
    return count
    
def getNumberOfFolders(target_folder):
    count  = 0
    for root, dirs, files in os.walk(target_folder):
        count += len(dirs)
    return count


def getNumberOfTestFiles(target_folder):
    count  = 0
    for root, dirs, files in os.walk(target_folder):
        for filename in files:
            if(re.search("test", filename, re.IGNORECASE)):
                count += 1
    return count

def checkREAD(filename):
    return (filename == "README.md")

def checkLicense(filename):
    return (filename == "LICENSE")

def checkGitIgnore(filename):
    return (filename == ".gitignore")



def printResults(target_folder, check_list, test_files):
    print("-" * 90, "")
    if(check_list[0]):  print(f"| {GREEN}OK{RESET}  |"," README.md")
    else:               print(f"| {RED}N/A{RESET} |"," README.md")
    print("-" * 90, "")
    if(check_list[1]):  print(f"| {GREEN}OK{RESET}  |"," LICENSE")
    else:               print(f"| {RED}N/A{RESET} |"," LICENSE")
    print("-" * 90, "")

    if(check_list[2]):  print(f"| {GREEN}OK{RESET}  |"," .gitignore")
    else:               print(f"| {RED}N/A{RESET} |"," .gitignore")
    print("-" * 90, "")


    print("-" * 90, "")
    if(test_files):
        print(f"| OK  | Filename w/ test ({getNumberOfTestFiles(target_folder)} out of {getNumberOfFiles(target_folder)} files)")
        for dir, files in test_files:
            print(f"|     |",f"  {dir} --> {files}")
    else:
        print(f"| N/A | Filename w/ test")

        