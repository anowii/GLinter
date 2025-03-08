import os
from github_repo import GitHubRepo
import argparse
import re, sys
import func_utils 
from security_utils import LeakChecker

#https://github.com/anowii/clone-this-test.git

def main():
    
    print("=" * 90, "")
    print( "\t\t\t\tWelcome to the GLinter Tool!")
    print("=" * 90, "")
    # Init Parser
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help='Path/URL to target')
    args = parser.parse_args()
    target = args.arg1

    print(f"Target argument:  {target}\n")
    if(func_utils.clean_folder(target_folder="ClonedRepo") == 0):
        print("Old repo removed")
    print("-" * 90, "") 

    check_passed = False
    try:
        #**************** CHECKS URL ****************#
        if(re.match(r"^http", target)):
            if(func_utils.cloneURL(target) != 0):
                target = "ClonedRepo/"
                check_passed = True
        #**************** CHECKS FOLDER ****************#
        elif(func_utils.validPath(target) != 0):
            check_passed = True
    except argparse.ArgumentError as e:
        parser.print_help()
        
    repo = GitHubRepo(target)
    if(check_passed):
        repo.run_checks()
    print("=" * 90)


    print("-" * 90)
    func_utils.printBanner("CHECKING SECURITY with gitleaks")  
    #func_utils.checkSecurity(target)
    print("-" * 90,"\n")

    
    print("-" * 90)
    func_utils.printBanner("CONTRIBUTERS AND NUMBER OF COMMITS")
    print("-" * 90)

    func_utils.getGitSummary(target)
    repo.printGitSummary()
    print("=" * 90, "\n")

    
if __name__ == "__main__":
    main()