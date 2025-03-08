import os, re
from func_utils import RED, RESET, GREEN, workflow_names,printBanner, printSpecialBanner
from typing import List
from repo_check import RepoCheck,LicenseCheck, ReadMeCheck, WorkflowCheck, GitIgnoreCheck, TestCheck

class GitHubRepo:
    def __init__(self, folder_path: str):
        """
        Initialize the GitHubRepo class with the folder path. 
        Scans the folder for test files, workflow files, and checks for artifacts.
        """
        
 
        self.folder_path = folder_path
        self.checks: List[RepoCheck] = [
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
            msg = check.format_results()
            print("-" * 90) 
            printSpecialBanner(f"{msg} ({check.score} out of {check.get_max_score()})")
            print("-" * 90)
            check.print_formatted_list()

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

   



