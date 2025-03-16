import os
from Core.utils import RED, RESET, YELLOW, GREEN, BLUE, is_file_empty, printSpecialBanner
from Core.RepoCheckers.repo_check_base import RepoCheck

#
#  GIT IGNORE CHECK
#

class GitIgnoreCheck(RepoCheck):
    """Check for .gitignore files."""
    def __init__(self, folder_path):
        super().__init__(folder_path, check_type='gitignore')  
        self.gitignore_files = []  
        self.amount_of_files = 0
        self.score = 0

    def run_check(self):
        """
        Checks for .gitingnore
        """
        for root, dirs, files in os.walk(self.folder_path, topdown=True):            
            for filename in files:
                if filename == ".gitignore":
                    self.gitignore_files.append([root,filename])
                    if not is_file_empty(os.path.join(root, filename)):
                        self.update_score()
                    self.amount_of_files += 1

    def get_file_amount(self):    
        return (self.amount_of_files)
    

    def get_score(self):
        return self.score
    
    def format_results(self):
        if not self.gitignore_files:
            return f"{RED}FAIL{RESET} |  .gitignore"
        elif self.gitignore_files and self.score > 0 :
            return f"{YELLOW}WARN{RESET} |  .gitignore"
        return f"{GREEN}PASS{RESET}  |  .gitignore"
        
    def print_formatted_list(self):
        for folder, files in self.gitignore_files:
            printSpecialBanner(f"{BLUE}{folder}{RESET}: {files}")