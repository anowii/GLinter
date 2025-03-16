import os
from Core.utils import RED, RESET, YELLOW, GREEN, BLUE, is_file_empty, printSpecialBanner
from Core.RepoCheckers.repo_check_base import RepoCheck

#
#  LICENSE CHECK                
#

class LicenseCheck(RepoCheck):
    """Check for license files."""
    def __init__(self, folder_path):
        super().__init__(folder_path,check_type='license')  
        self.license_files = []
        self.score = 0

    def run_check(self):
        """
        Checks for license
        """
        for root, _, files in os.walk(self.folder_path, topdown=True):            
            if os.path.basename(root).lower() == "license":
                self.license_files.append([root, files])
            for filename in files:
                if os.path.basename(filename).lower() == "license":
                    self.license_files.append([root,filename])
                    self.amount_of_files += 1
                    if not is_file_empty(os.path.join(root,filename)):
                        self.update_score()

    def get_file_amount(self):
        return len(self.license_files)
    
          
    def get_score(self):
        return self.score
    
    def format_results(self):
        if not self.license_files:
            return f"{RED}FAIL{RESET} | LICENSE "
        elif self.license_files and self.score > 0 :
            return f"{YELLOW}WARN{RESET} | LICENSE"
        return f"{GREEN}PASS{RESET}  | LICENSE"
   
    def print_formatted_list(self):
        for folder, files in self.license_files:
            printSpecialBanner(f"{BLUE}{folder}{RESET}: {files}")