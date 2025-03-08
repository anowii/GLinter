import os, re, textwrap
from func_utils import RED, RESET, YELLOW, GREEN, is_file_empty, printBanner

class RepoCheck:
    """Base class for all repository checks."""
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.score = 0
    
    def run_check(self):
        """Run the specific check (to be overridden)."""
        pass

    def update_score(self, value):
        """Update the score based on check results."""
        self.score += value

    def get_max_score(self):
        """Return the max score for this check. Should be overridden by subclasses."""
        pass

    def format_results(self):
        """Format results for output (to be overridden)."""
        pass
    
    def print_formatted_list(self):
        """Prints a formatted list"""

class GitIgnoreCheck(RepoCheck):
    """Check for .gitignore files."""
    def __init__(self, folder_path):
        super().__init__(folder_path)  
        self.gitignore_files = []  

    def run_check(self):
        """
        Checks for .gitingnore
        """
        for root, _, files in os.walk(self.folder_path, topdown=True):            
            if os.path.basename(root).lower() == ".gitignore":
                self.gitignore_files.append([root, files])

            for filename in files:
                if os.path.basename(filename).lower() == ".gitignore":
                    self.gitignore_files.append([root,filename])
                    self.update_score(is_file_empty(os.path.join(root,filename)))

    def get_max_score(self):
        return 2*len(self.gitignore_files)
    
    def format_results(self):
        if not self.gitignore_files:
            return f"{RED}N/A{RESET} |  .gitignore"
        elif self.gitignore_files and self.score <= (self.get_max_score()/2):
            return f"{YELLOW}MEH{RESET} |  .gitignore"
        return f"{GREEN}OK{RESET}  |  .gitignore"
        
    def print_formatted_list(self):
        for folder, _ in self.gitignore_files:
            printBanner(f" In {folder}")

class LicenseCheck(RepoCheck):
    """Check for .gitignore files."""
    def __init__(self, folder_path):
        super().__init__(folder_path)  
        self.license_files = []  

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

    def get_max_score(self):
        return 2*len(self.license_files)
    
    def format_results(self):
        if not self.license_files :
            return f"{RED}N/A{RESET} |  license"
        return f"{GREEN}OK{RESET}  |  license"

    def print_formatted_list(self):
        for folder, _ in self.license_files:
            printBanner(f" In {folder}")

class WorkflowCheck(RepoCheck):
    """Check for GitHub Actions workflows."""
    def __init__(self, folder_path):
        super().__init__(folder_path)  
        self.workflow_files = []  
    
    def run_check(self):
        """
        Checks for workflow directories/files
        """
        for root, dirs, _ in os.walk(self.folder_path, topdown=True):
                
            if ".github" in dirs:
                for subroot, subdirs, _ in os.walk(os.path.join(root,".github")):
                    if "workflows" in subdirs:
                        matched_files = [file for file in os.listdir(os.path.join(subroot,"workflows"))]
                        self.update_score(1)

                        if matched_files:
                            self.workflow_files.append([os.path.join(subroot,"workflows"), matched_files])
                            self.update_score(1)

    def get_max_score(self):
        return 2
    
    def format_results(self):
        if not self.workflow_files :
            return f"{RED}N/A{RESET} |  workflows"
        return f"{GREEN}OK{RESET}  |  workflows"
   
    def print_formatted_list(self):
        for folder, files in self.workflow_files:
            printBanner(f"In {folder}")
            wrapped_text = textwrap.fill(", ".join(files), width=90)
            for line in wrapped_text.split("\n"):
                printBanner(f"   {line}")

class TestCheck(RepoCheck):
    """Check for test-related files."""
    def __init__(self, folder_path):
        super().__init__(folder_path)  
        self.test_folders = []  
        self.test_files = [] 
        self.amount_folders = 0
        self.amount_files = 0

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

            matched_files = [file for file in files if re.search("test", file, re.IGNORECASE)]
            if matched_files:
                self.test_files.append([root,matched_files])  
        
    # def format_test_files(self):
    # def format_test_folders(self):
  
    def get_max_score(self):
        return 0

    def format_results(self):
        if not self.test_files:
            return f"{RED}N/A{RESET} |  Test:f"
        return f"{GREEN}OK{RESET}  |   Test:f"
    
    def print_formatted_list(self):
        for folder, files in self.test_files:
            printBanner(f"In {folder}")
            wrapped_text = textwrap.fill(", ".join(files), width=90)
            for line in wrapped_text.split("\n"):
                printBanner(f"   {line}")

class ReadMeCheck(RepoCheck):
    """Check for README.md files."""
    def __init__(self, folder_path):
        super().__init__(folder_path)  
        self.readMe_files = []  

    def run_check(self):
        for root, _, files in os.walk(self.folder_path, topdown=True):            
            for filename in files:
                if os.path.basename(filename).lower() == "readme.md":
                    self.readMe_files.append([root, filename])
                    self.update_score(is_file_empty(os.path.join(root,filename)))

    
    def get_max_score(self):
        return 2*len(self.readMe_files)
    
    def format_results(self):
        if not self.readMe_files:
            return f"{RED}N/A{RESET} | README.MD"
        return f"{GREEN}OK{RESET}  | README.MD"
    
    def print_formatted_list(self):
        for folder, files in self.readMe_files:
            printBanner(f" In {folder}")
