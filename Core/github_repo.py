from Core.RepoCheckers import RepoCheck, ReadMeCheck, GitIgnoreCheck,WorkflowCheck,LicenseCheck,TestFolderCheck,TestFileCheck
import subprocess
from typing import List
import Core.utils as utils

check_names = ["readme","gitignore","license","workflow","testfolders", "testfiles"]

class GitHubRepo:
    def __init__(self, folder_path: str):
        """
        Initialize the GitHubRepo class with the folder path. 
        Scans the folder for test files, workflow files, and checks for artifacts.
        """
        self.folder_path = folder_path
        self.checks: List[RepoCheck] = [
            ReadMeCheck(folder_path),
            GitIgnoreCheck(folder_path),
            LicenseCheck(folder_path),
            WorkflowCheck(folder_path)
        ]
        self.test_checks: List[RepoCheck] = [
            TestFolderCheck(folder_path),
            TestFileCheck(folder_path)
        ]
        self.gitstat_path = "Reports/gitstat.log"

    def run_checks(self):
        """Execute all checks."""
        for check in self.checks:
            check.run_check()
            msg = check.format_results()
            print("-" * 90) 
            utils.printSpecialBanner(f"{msg} : FILES CHECKED({check.get_file_amount()}) : SCORE({check.score})")
            print("-" * 90)
            check.print_formatted_list()

    def get_test_type(self, check_type):
        """Get at specific test type """

        if check_type in check_names:
            for check in self.checks:
                if(check.get_type() == check_type):
                    return check
            for check in self.test_checks:
                if(check.get_type() == check_type):
                    return check
        return f"Please choose a name in the list: {check_names}"

    def run_check_test(self):
        """Execute all checks for test folders and files."""
        for test_check in self.test_checks:
            test_check.run_check()
            msg = test_check.format_results()
            print("-" * 90) 
            utils.printSpecialBanner(f"{msg}")
            print("-" * 90)
            test_check.print_formatted_list()
        
    def getGitSummary(self):
        if(utils.is_git_repo(self.folder_path)):
            log_command = ["git", "--git-dir", f"{self.folder_path}/.git", "shortlog", "--summary", "--numbered", "--no-merges"]
            with open("Reports/gitstat.log", "w+", encoding="utf-8") as file:
                result = subprocess.run(log_command, stdout=file, stderr=subprocess.PIPE, text=True,check=True)   
                return result.returncode == 0, result.stderr
        else: 
            return False, "Target does not contain a .git folder "
        
    def printGitSummary(self):
        if(utils.is_git_repo(self.folder_path)):
            count = 0
            with open("Reports/gitstat.log", "r", encoding="utf-8") as log_file:
                utils.printBanner("shows top 10: if there are more contributers see 'Reports/'gitstat.log'")
                print("|","-"*86, "|")
                for line in log_file:
                    if count <= 10 :
                        count += 1
                        log = line.split()
                        utils.printBanner(f"{log[0]} {log[1]}")


