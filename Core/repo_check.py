import os, re, textwrap
from .utils import RED, RESET, YELLOW, GREEN, BLUE, is_file_empty, printBanner,printSpecialBanner, printLines

class RepoCheck:
    """Base class for all repository checks."""
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.score = 0
        self.amount_of_files = 0
    
    def run_check(self):
        """Run the specific check (to be overridden)."""
        pass

    def update_score(self, value):
        """Update the score based on check results."""
        self.score += value

    def get_file_amount(self):
        """Return the max score for this check."""
        pass

    def get_score(self):
        """Return score."""
        pass

    def get_type(self):
        """Return check type."""
        pass

    def format_results(self):
        """Format results for output."""
        pass
    
    def print_formatted_list(self):
        """Prints a formatted list."""
        pass

###########################################
#           GIT IGNORE CHECK              #
###########################################

class GitIgnoreCheck(RepoCheck):
    """Check for .gitignore files."""
    def __init__(self, folder_path):
        super().__init__(folder_path)  
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
                    self.update_score(is_file_empty(os.path.join(root, filename)))
                    self.amount_of_files += 1

    def get_file_amount(self):    
        return (self.amount_of_files)
    
    def get_type(self):
        return "gitignore"
      
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


###########################################
#           LICENSE CHECK                 #
###########################################

class LicenseCheck(RepoCheck):
    """Check for license files."""
    def __init__(self, folder_path):
        super().__init__(folder_path)  
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
                    self.update_score(is_file_empty(os.path.join(root,filename)))

    def get_file_amount(self):
        return len(self.license_files)
    
    def get_type(self):
        return "license"
          
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

###########################################
#          WORKFLOW    CHECK              #
###########################################
class WorkflowCheck(RepoCheck):
    """Check for GitHub Actions workflows."""
    def __init__(self, folder_path):
        super().__init__(folder_path)  
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
                self.update_score(is_file_empty(os.path.join(dir_path, file)))
                self.amount_of_files += 1
    
    def get_file_amount(self):
        return (self.amount_of_files)
    
    def get_type(self):
        return "workflow"  
          
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


###########################################
#           TEST FOLDER CHECK             #
###########################################
class TestFolderCheck(RepoCheck):
    """Check for test-related files."""
    def __init__(self, folder_path):
        super().__init__(folder_path)  
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
    
    def get_type(self):
        return "testfolder"
      
    def get_score(self):
        return self.score
    
    def format_results(self):
        if not self.test_folders:
            return f"{RED}FAIL{RESET} | Folders w/ test"
        return f"{GREEN}PASS{RESET} | Folder w/ test"
    
    def print_formatted_list(self):
        for _,folder, _ in self.test_folders:
            printSpecialBanner(f"{BLUE}{folder}{RESET}")



###########################################
#           TEST FILE  CHECK              #
###########################################
class TestFileCheck(RepoCheck):
    """Check for test-related files."""
    def __init__(self, folder_path):
        super().__init__(folder_path)  
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

    def get_type(self):
        return "testfile"
    
          
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


###########################################
#           README CHECK                  #
###########################################

class ReadMeCheck(RepoCheck):
    """Check for README.md files."""
    def __init__(self, folder_path):
        super().__init__(folder_path)  
        self.readMe_files = []  
        self.amount_of_files = 0
        self.score = 0
 
    def run_check(self):
        for root, _, files in os.walk(self.folder_path, topdown=True):            
            for filename in files:
                if filename.lower() == "readme.md":
                    self.readMe_files.append([root, filename])
                    self.update_score(is_file_empty(os.path.join(root,filename)))
                    self.amount_of_files += 1

    
    def get_file_amount(self):
        return (self.amount_of_files)
    
    def get_type(self):
        return "readme"
    
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

