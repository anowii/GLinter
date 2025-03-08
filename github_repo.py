import os, re
from func_utils import RED, RESET, GREEN, workflow_names
from github_blob import GitIgnoreCheck, WorkflowCheck,TestCheck,ReadMeCheck,LicenseCheck

class GitHubRepo:
    def __init__(self, folder_path: str):
        """
        Initialize the GitHubRepo class with the folder path. 
        Scans the folder for test files, workflow files, and checks for artifacts.
        """
 
        self.folder_path = folder_path
        self.checks = [
            ReadMeCheck(folder_path),
            LicenseCheck(folder_path),
            WorkflowCheck(folder_path),
            GitIgnoreCheck(folder_path),
            TestCheck(folder_path),
        ]

    
    def run_checks(self):
        """Execute all checks."""
        for check in self.checks:
            check.run_check()
            msg, list = check.format_results()
            print(msg, check.score, list)
            print("-" * 90, "")

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

   



