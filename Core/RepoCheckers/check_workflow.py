import os, textwrap
from Core.utils import RED, RESET, YELLOW, GREEN, BLUE, is_file_empty, printBanner,printSpecialBanner, printLines
from Core.RepoCheckers.repo_check_base import RepoCheck

#
# WORKFLOW CHECK              
#

class WorkflowCheck(RepoCheck):
    """Check for GitHub Actions workflows."""
    def __init__(self, folder_path):
        super().__init__(folder_path, check_type='workflow')  
        self.workflow_files = []  
        self.amount_of_files = 0
        self.score = 0


    def run_check(self):
        """
        Checks for workflow directories/files
        """ 
        for root, dirs, _ in os.walk(self.folder_path, topdown=True):     
            if ".github" in dirs:
                dir_path = os.path.join(root,".github")
                if "workflow" in os.listdir(dir_path):
                    dir_path = os.path.join(dir_path,"workflow")        
                    matched_files= [file for file in os.listdir(dir_path)]
                    if matched_files:
                        self.workflow_files.append([dir_path, matched_files])
                        
        for dir_path,files in self.workflow_files:
            for file in files:
                if not is_file_empty(os.path.join(dir_path, file)):
                    self.update_score()
                    self.amount_of_files += 1
    
    def get_file_amount(self):
        return (self.amount_of_files)
    
          
    def get_score(self):
        return self.score
    
    def format_results(self):
        if not self.workflow_files:
            return f"{RED}FAIL{RESET} | workflow "
        elif self.workflow_files and self.score > 0 :
            return f"{YELLOW}WARN{RESET} | workflow"
        return f"{GREEN}PASS{RESET}  | workflow"
   
    def print_formatted_list(self):
        for folder, files in self.workflow_files:
            printSpecialBanner(f"{BLUE}{folder}{RESET}")
            wrapped_text = textwrap.fill(", ".join(files), width=90)
            for line in wrapped_text.split("\n"):
                printBanner(f"  [{line}]")
        printLines("-",90)