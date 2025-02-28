import os, subprocess, sys, re

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

def validPath(dirPath):
    if not os.path.exists(dirPath):
        print(f"{RED}Error (folder) : Folder path does not found{RESET}")
        sys.exit(1)
    else:
        return 0

def cloneURL(git_url):
    clone_command = ["git", "clone", git_url, "ClonedRepo\\"]
    result = subprocess.run(clone_command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"{RED}Error (url) :{RESET}", result.stderr)
        sys.exit(1)
    else:
        return result.returncode

def checkSecurity(target_folder):
    command = [".\\run_gitleaks.bat",  target_folder]
    try:
        subprocess.run(command, text=True)
        #print(f"| {GREEN}OK{RESET}  |",f" No secrets found ")
    except subprocess.CalledProcessError as e:
        print(f"Error while running Gitleaks: {e.stderr}")

def clean_folder():
    folder_path = "ClonedRepo\\"
    command = f"Remove-Item -Recurse -Force {folder_path}"
    try:
        result = subprocess.run(
            ["powershell", "-Command", command], 
            capture_output=True,
            text=True,
            check=True
            )
        print(f"Clean up needed, removed the folder: {folder_path}")
    except subprocess.CalledProcessError as e:
            if e.stderr and "Cannot find path" in e.stderr:
                print(f"No clean up needed, the folder {folder_path} doesn't exist.")
            else:
                print(f"Error occurred, but not related to missing folder: {result.returncode}")


def checkFile(filename, check_list):
    if checkREAD(filename):
        check_list[0] = checkREAD(filename)
    elif checkLicense(filename):
        check_list[1] = checkLicense(filename)
    elif checkGitIgnore(filename):
        check_list[2] = checkGitIgnore(filename)

def getGitSummary(target_folder):
    log_command = ["git", "shortlog", "--summary", "--numbered", "--no-merges"]
    count = 0
    try:
        with open("gitstat.log", "w", encoding="utf-8") as f:
            result = subprocess.run(log_command, cwd=target_folder, stdout=f, stderr=subprocess.PIPE, text=True, shell=True)
        
        if result.returncode == 0:
            with open("gitstat.log", "r", encoding="utf-8") as log_file:
                print("shows top 10: if there are more contributes see 'gitstat.log'")
                print("|","~"*88)
                for line in log_file:
                    log = line.split()
                    print(f"| {log[0]} {log[1]}") 
        else:
            print("Git command failed with return code:", result.returncode)
            print("Error:", result.stderr)
    
    except FileNotFoundError as e:
        print("Error: Git not found. Is Git installed?", e)
        return []
    except subprocess.CalledProcessError as e:
        print("Error running Git command:", e)
        return []
    except UnicodeDecodeError as e:
        print(f"Error reading the file due to encoding: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

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


def checkWorkFlow(workflow_list):
    correct = 0
    total = 0
    correct_files = []
    for workflow, files in workflow_list:
        for file in files:
            total += 1
            if(file in workflow_names):
                correct += 1
                correct_files.append(file)
                #print(f"\t- {file}")
    return f"({correct} out of {total}) {correct_files}"


def printResults(target_folder, check_list, test_files, workflow_list):
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

    if(workflow_list):
        print(f"| {GREEN}OK{RESET}  |  workflow {checkWorkFlow(workflow_list)}")    
    else:
        print(f"| {RED}N/A{RESET} |"," workflow ")

    print("-" * 90, "")
    if(test_files):
        print(f"| OK  | Filename w/ test ({getNumberOfTestFiles(target_folder)} out of {getNumberOfFiles(target_folder)} files)")
        for dir, files in test_files:
            print(f"|     |",f"  {dir} --> {files}")
    else:
        print(f"| N/A | Filename w/ test")

        