import os, re, textwrap
from Core.utils import RED, RESET, GREEN, BLUE, printBanner,printSpecialBanner, printLines
from Core.RepoCheckers.repo_check_base import RepoCheck

#
#  TEST FOLDER CHECK   
#

class TestFolderCheck(RepoCheck):
    """Check for test-related files."""
    def __init__(self, folder_path):
        super().__init__(folder_path, check_type='testfolder')  
        self.test_folders = []  
        self.amount_folders = 0

    def run_check(self):
        """
        Checks for test-related files or directories
        """
        for root, dirs, files in os.walk(self.folder_path):
            for dirname in dirs:
                if re.search("test", dirname, re.IGNORECASE):
                    dir_path = os.path.join(root, dirname)
                    dir_files = [file for file in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, file))] 
                    self.test_folders.append([root, dir_path, len(dir_files)])

    def get_file_amount(self):
        return self.amount_folders
      
    def get_score(self):
        return self.score
    
    def format_results(self):
        if not self.test_folders:
            return f"{RED}FAIL{RESET} | Folders w/ test"
        return f"{GREEN}PASS{RESET} | Folder w/ test"
    
    def print_formatted_list(self):
        for _,folder, _ in self.test_folders:
            printSpecialBanner(f"{BLUE}{folder}{RESET}")



#
# TEST FILE CHECK             
#
class TestFileCheck(RepoCheck):
    """Check for test-related files."""
    def __init__(self, folder_path):
        super().__init__(folder_path, check_type='testfile')  
        self.test_files = [] 
        self.amount_files = 0
        

    def run_check(self):
        """
        Checks for test-related files or directories
        """
        for root, dirs, files in os.walk(self.folder_path):
            matched_files = [file for file in files if re.search("test", file, re.IGNORECASE)]
            if matched_files:
                self.test_files.append([root,matched_files])  
        
    def get_file_amount(self):
        return 0
        
    def get_score(self):
        return self.score

    def format_results(self):
        if not self.test_files:
            return f"{RED}FAIL{RESET} | Files w/ test"
        return f"{GREEN}PASS{RESET} | Files w/ test"
    
    def print_formatted_list(self):
        for folder, files in self.test_files:
            printSpecialBanner(f"{BLUE}{folder}{RESET}:")
            wrapped_text = textwrap.fill(", ".join(files), width=90)
            for line in wrapped_text.split("\n"):
                printBanner(f"  [{line}]")
        printLines("-",90)
