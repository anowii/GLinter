import re,argparse
from Core.github_repo import GitHubRepo
import Core.utils as utils
from Core.leak_checker import LeakChecker

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
    if(utils.clean_folder(target_folder="ClonedRepo") == 0):
        print("Old repo removed")
    print("-" * 90, "") 

    check_passed = False
    try:
        #**************** CHECKS URL ****************#
        if(re.match(r"^http", target)):
            if(utils.cloneURL(target) != 0):
                target = "ClonedRepo/"
                check_passed = True
        #**************** CHECKS FOLDER ****************#
        elif(utils.validPath(target) != 0):
            check_passed = True
    except argparse.ArgumentError as e:
        parser.print_help()


    #******************* CHECKING ARTIFACTS********************#
    #**********************************************************# 
    repo = GitHubRepo(target)
    if(check_passed):
        repo.run_checks()
        repo.run_check_test()
        print("=" * 90)
       

    #********************* CONTRIBUTERS ***********************#
    #**********************************************************#
    print("-" * 90)
    utils.printBanner("CONTRIBUTERS AND NUMBER OF COMMITS")
    print("-" * 90)
    repo.getGitSummary()
    repo.printGitSummary()
    print("=" * 90, "\n")
       
    #**************** SECURITY w/ Gitleaks ********************#
    #**********************************************************#
    print("-" * 90)
    utils.printBanner("CHECKING SECURITY with gitleaks")  
    print("-" * 90,"\n")
    LeakChecker(target_folder=target).print_gitleak()
    LeakChecker(target_folder=target).print_gitleak_report()
    print("=" * 90,"\n")

    
if __name__ == "__main__":
    main()