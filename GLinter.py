import argparse
from Core.github_repo import GitHubRepo
import Core.utils as utils
from Core.leak_checker import LeakChecker
from Core.repo_config import RepoConfig

#https://github.com/anowii/clone-this-test.git
#https://github.com/anowii/test_leaks.git

DEFAULT_PATH = "ClonedRepo"

def main(repo_config:RepoConfig):
    utils.printWelcomeBanner()
    intial_check_passed = inital_check(repo_config.get_cloned_dirpath())
    if(intial_check_passed):    
        run_program(repo_config=repo_config)
    else:
        return 0


def inital_check(target_path):
    parser, args = utils.parse_init()
    intial_check_passed = False

    try:
        if args.url:
            print(f"Processing URL: {args.url}")
            url = args.url
            
            intial_check_passed, msg = utils.cloneURL(git_url=url, target_path=target_path)
            if not intial_check_passed:
                return print(msg)

        elif args.dir:
            print(f"Processing folder: {args.dir}")
            #******* CHECK FOLDER **********#
            intial_check_passed, msg = utils.validPath(target_folder=args.dir)
            if not intial_check_passed:
                return print(msg)  
            else:
                repo_config.set_target_path(args.dir)
    except argparse.ArgumentError as e:
        parser.print_usage()
    
    return intial_check_passed

def run_program(repo_config:RepoConfig):
    
    #******* CHECKING ARTIFACTS *******#
    target_path, check_list = repo_config.get_config()
    repo = GitHubRepo(target_path)
    if(check_list.get("artifact_check")):
        utils.printStripeBanner("CHECKING ARTIFACTS")
        repo.run_checks()
    else:
        utils.printStripeBanner("CHECKING ARTIFACTS: SKIPPED")

    if(check_list.get("test_check")):
        utils.printStripeBanner("CHECK FOR TEST FILES & FOLDERS")
        repo.run_check_test()
    else:
        utils.printStripeBanner("CHECK FOR TEST FILES & FOLDERS: SKIPPED")

    #********* CONTRIBUTERS **********#
    if (check_list.get("commit_contribute_check")):
        utils.printStripeBanner("CONTRIBUTERS & COMMITS")
        success, msg = repo.getGitSummary()
        if(success):
            repo.printGitSummary()
        else:
            utils.printSpecialBanner(f"{utils.RED}{msg}{utils.RESET}")
        utils.printLines("=",90)
    else:
        utils.printStripeBanner("CONTRIBUTERS & COMMITS : SKIPPED")


    #****** SECURITY w/ Gitleaks ********#
    if (check_list.get("git_leaks_check")):
        utils.printStripeBanner("CHECKING SECURITY with gitleaks: full report in 'Reports/gitleaks.json'")
        LeakChecker(target_folder=target_path).print_gitleak_highlights()
        LeakChecker(target_folder=target_path).print_gitleak_report()
        utils.printLines("=",90)
    else:
        utils.printStripeBanner("CHECKING SECURITY with gitleaks: SKIPPED")

    
if __name__ == "__main__":
    repo_config = RepoConfig('config.json')
    if repo_config.check_config():
        main(repo_config=repo_config)
    else:
        print("Error: Invalid config")