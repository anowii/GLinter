import argparse
from Core.github_repo import GitHubRepo
import Core.utils as utils
from Core.leak_checker import LeakChecker

#https://github.com/anowii/clone-this-test.git
#https://github.com/anowii/test_leaks.git

def main():

    # ****** WELCOME BANNER ****** #
    print("=" * 90, "")
    print( "\t\t\t  Welcome to the GLinter Tool!")
    print("=" * 90, "")
    utils.clean_reports()
    utils.clean_folder(target_folder="ClonedRepo")
    # Initate Parser
    parser = argparse.ArgumentParser(description="Process URL or path to a folder, choose one.")
    group = parser.add_mutually_exclusive_group(required=True)
    #group.add_argument("--file", help="Path to file", type=str)
    group.add_argument("--url", help="URL to git repo", type=str)
    group.add_argument("--dir", help="Path to folder", type=str)

    args = parser.parse_args()
    try:
        intial_check_passed = False
        if args.url:
            print(f"Processing URL: {args.url}")
            target = args.url
            #****** CHECKS URL **********#
            success, msg = utils.cloneURL(target)
            if(success):
                target = "ClonedRepo/"
                intial_check_passed = True
            else:
                print(msg)
        elif args.dir:
            print(f"Processing folder: {args.dir}")
            target = args.dir
            #******* CHECK FOLDER **********#
            success, msg = utils.validPath(target)
            if(success):
                intial_check_passed = True
            else:
                print(msg)  
    except argparse.ArgumentError as e:
        parser.print_help()

    if(intial_check_passed):    
        run_program(target_path=target)
    else:
        print("FAIL")

def run_program(target_path):
        #******* CHECKING ARTIFACTS *******#
        repo = GitHubRepo(target_path)
        repo.run_checks()
        repo.run_check_test()
        print("=" * 90)
       
        #********* CONTRIBUTERS **********#
        utils.printLines("-",90)
        utils.printBanner("CONTRIBUTERS & COMMITS")
        utils.printLines("-",90)
        success, msg = repo.getGitSummary()
        if(success):
            repo.printGitSummary()
        else:
            utils.printSpecialBanner(f"{utils.RED}{msg}{utils.RESET}")
        utils.printLines("=",90)

        #****SECURITY w/ Gitleaks ********#
        print("=" * 90)
        utils.printBanner("CHECKING SECURITY with gitleaks")  
        print("=" * 90,"\n")
        LeakChecker(target_folder=target_path).print_gitleak_highlights()
        LeakChecker(target_folder=target_path).print_gitleak_report()
        print("=" * 90,"\n")

    
if __name__ == "__main__":
    main()