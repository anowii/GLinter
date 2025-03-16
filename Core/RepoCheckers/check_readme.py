import os
from Core.utils import RED, RESET, YELLOW, GREEN, BLUE, is_file_empty, printBanner,printSpecialBanner, printLines
from Core.RepoCheckers.repo_check_base import RepoCheck

#
# README CHECK                  
#

class ReadMeCheck(RepoCheck):
    """Check for README.md files."""
    def __init__(self, folder_path):
        super().__init__(folder_path, check_type='readme')  
        self.readMe_files = []  
        self.amount_of_files = 0
        self.score = 0
 
    def run_check(self):
        for root, _, files in os.walk(self.folder_path, topdown=True):            
            for filename in files:
                if filename.lower() == "readme.md":
                    self.readMe_files.append([root, filename])
                    if not is_file_empty(is_file_empty(os.path.join(root,filename))):
                        self.update_score()
                    self.amount_of_files += 1

    
    def get_file_amount(self):
        return (self.amount_of_files)

    
    def get_score(self):
        return self.score
    
    def format_results(self):
        if not self.readMe_files:
            return f"{RED}FAIL{RESET} | README.MD"
        elif self.readMe_files and self.score > 0:
            return f"{YELLOW}WARN{RESET} | README.MD"
        return f"{GREEN}PASS{RESET}  | README.MD"
    
    def print_formatted_list(self):
        for folder, files in self.readMe_files:
            printSpecialBanner(f"{BLUE}{folder}{RESET}: {files}")

