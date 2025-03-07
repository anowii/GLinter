import os, re
from func_utils import RED, RESET, GREEN, workflow_names

class GitHubRepo:
    def __init__(self, folder_path: str):
        """
        Initialize the GitHubRepo class with the folder path. 
        Scans the folder for test files, workflow files, and checks for artifacts.
        """
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"Folder path {folder_path} does not exist.")
        
        self.folder_path = folder_path
        self.test_files = []
        self.test_folders = []
        self.workflow_files = []
        self.gitIgnore_files = []
        self.license_files = []
        self.read_me_files = []


        self._scan_repository()

    def _scan_repository(self):
        self.scan_repo_workflow()
        self.scan_repo_gitignore()
        self.scan_repo_license()
        self.scan_repo_test_files()
        self.scan_repo_read_me()
   


    def scan_repo_read_me(self):
        """
        Checks for readme files
        """
        for root, dirs, files in os.walk(self.folder_path, topdown=True):            
            if os.path.basename(root).lower() == "readme.md":
                self.read_me_files.append([root, files])
 
            for filename in files:
                if os.path.basename(filename).lower() == "readme.md":
                    self.read_me_files.append([root, filename])

    def scan_repo_workflow(self):
        """
        Checks for workflow directories/files
        """
        for root, dirs, files in os.walk(self.folder_path, topdown=True):
            matched_files = [file for file in files if file in workflow_names]
            if matched_files:
                self.workflow_files.append([root, matched_files])

    def scan_repo_gitignore(self):
        """
        Checks for .gitingnore
        """
        for root, dirs, files in os.walk(self.folder_path, topdown=True):            
            if os.path.basename(root).lower() == ".gitignore":
                self.gitIgnore_files.append([root, files])
 
            for filename in files:
                if os.path.basename(filename).lower() == ".gitignore":
                    self.gitIgnore_files.append([root,filename])

    def scan_repo_license(self):
        """
        Checks for license files
        """
        for root, dirs, files in os.walk(self.folder_path, topdown=True):
            for filename in files:
                if os.path.basename(filename).lower() == "license":
                    self.license_files.append([root, filename])
               
    def scan_repo_test_files(self):
        """
        Checks for test-related files or directories
        """
        for root, dirs, files in os.walk(self.folder_path):
            for dirname in dirs:
                if re.search("test", dirname, re.IGNORECASE):
                    self.test_folders.append([root,dirname])
                
            matched_files = [file for file in files if re.search("test", file, re.IGNORECASE)]
            if matched_files:
                self.test_files.append([root,matched_files])
        

    def printGitSummary(self):
        with open("gitstat.log", "r", encoding="utf-8") as log_file:
            print("| shows top 10: if there are more contributes see 'gitstat.log'", " "*24, "|")
            print("|","~"*86, "|")
            for line in log_file:
                log = line.split()
                count = 87 - len(f"| {log[0]} {log[1]}")
                print(f"| {log[0]} {log[1]}", " "*count, "|") 

   
    def checkGitIgnore(self):
        if(self.gitIgnore_files == []):
            return False,  f"| {RED}N/A{RESET} |  .gitignore", self.gitIgnore_files
        else:
            return True, f"| {GREEN}OK{RESET}  |  .gitignore", self.gitIgnore_files
        
    def checkLicences(self):
        if(self.license_files == []):
            return False,  f"| {RED}N/A{RESET} |  LICENSE", self.license_files
        else:
            return True, f"| {GREEN}OK{RESET}  |  LICENSE", self.license_files
    
    def checkWorkFlow(self):
        if(self.workflow_files == []):
            return False,  f"| {RED}N/A{RESET} |  workflow", self.workflow_files
        else:
            return True, f"| {GREEN}OK{RESET}  |  workflow", self.workflow_files
        
    def checkTestFiles(self):
        if(self.test_files == []):
            return False,  f"| {RED}N/A{RESET} |  Test Files", self.test_files
        else:
            return True, f"| {GREEN}OK{RESET}  |  Test Files", self.test_files

    def checkTestFolders(self):
        if(self.test_folders == []):
            return False,  f"| {RED}N/A{RESET} |  Test Folders", self.test_folders
        else:
            return True, f"| {GREEN}OK{RESET}  |  Test Folders", self.test_folders  
        
    def checkReadMeFiles(self):
        if(self.read_me_files == []):
            return False,  f"| {RED}N/A{RESET} |  README.MD", self.read_me_files
        else:
            return True, f"| {GREEN}OK{RESET}  |  README.MD", self.read_me_files