from Core.utils import printBanner, printSpecialBanner,subprocess
from typing import List
from Core.repo_check import RepoCheck,LicenseCheck, ReadMeCheck, WorkflowCheck, GitIgnoreCheck, TestFileCheck, TestFolderCheck

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

    def run_checks(self):
        """Execute all checks."""
        for check in self.checks:
            check.run_check()
            msg = check.format_results()
            print("-" * 90) 
            printSpecialBanner(f"{msg} Files scored ({check.score} out of {check.get_max_score()})")
            print("-" * 90)
            check.print_formatted_list()

    def run_check_test(self):
        """Execute all checks for test folders and files."""
        for test_check in self.test_checks:
            test_check.run_check()
            msg = test_check.format_results()
            print("-" * 90) 
            printSpecialBanner(f"{msg}")
            print("-" * 90)
            test_check.print_formatted_list()

    def getGitSummary(self):
        log_command = [f"cd {self.folder_path} && git shortlog --summary --numbered --no-merges && cd .."]
        with open("gitstat.log", "w", encoding="utf-8") as f:
            result = subprocess.run(log_command, stdout=f, stderr=subprocess.PIPE, text=True, shell=True)   
        return result.returncode == 0, result.stderr
    
    def printGitSummary(self):
        count = 0
        with open("gitstat.log", "r", encoding="utf-8") as log_file:
            print("| shows top 10: if there are more contributers see 'gitstat.log'", " "*23, "|")
            print("|","-"*86, "|")
            for line in log_file:
                if count <= 10 :
                    count += 1
                    log = line.split()
                    format = 87 - len(f"| {log[0]} {log[1]}")
                    print(f"| {log[0]} {log[1]}", " "*format, "|") 

   



