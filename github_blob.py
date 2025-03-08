
import os, re
from func_utils import RED, RESET, GREEN, is_file_empty

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


    def format_results(self):
        """Format results for output (to be overridden)."""
        pass

    def get_max_score(self):
        """Return the max score for this check. Should be overridden by subclasses."""
        pass

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
        if not self.gitignore_files :
            return f"| {RED}N/A{RESET} |  .gitignore", self.gitignore_files
        return f"| {GREEN}OK{RESET}  |  .gitignore", self.gitignore_files
    

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
            return f"| {RED}N/A{RESET} |  license", self.license_files
        return f"| {GREEN}OK{RESET}  |  license", self.license_files

class WorkflowCheck(RepoCheck):
    """Check for GitHub Actions workflows."""
    def __init__(self, folder_path):
        super().__init__(folder_path)  
        self.workflow_files = []  
    
    def run_check(self):
        """
        Checks for workflow directories/files
        They should be in .github/workflows
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
            return f"| {RED}N/A{RESET} |  workflows", self.workflow_files
        return f"| {GREEN}OK{RESET}  |  workflows", self.workflow_files

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
            return f"| {RED}N/A{RESET} |  Test:f", self.test_files
        return f"| {GREEN}OK{RESET}  |   Test:f", self.test_files

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
            return f"| {RED}N/A{RESET} |  README.MD", self.readMe_files
        return f"| {GREEN}OK{RESET}  |   README.MD", self.readMe_files