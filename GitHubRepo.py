import os, re, run_test

class GitHubRepo:
    def __init__(self, folder_path: str):
        """
        Initialize the GitHubRepo class with the folder path. 
        Scans the folder for test files, workflow files, and checks for artifacts.
        """
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"Folder path {folder_path} does not exist.")
        
        self.folder_path = folder_path
        self.check_artifacts = [False, False, False]  
        self.test_files = []
        self.workflow_files = []
        self.gitIgnore_files = []

        self._scan_repository()

    def _scan_repository(self):
        """
        Walk through the folder and classify files into workflow files, test files,
        and check artifacts using the `run_test.checkFile` function.
        """
        for root, dirs, files in os.walk(self.folder_path, topdown=True):
            # Check for workflow directories/files
            if os.path.basename(root).lower() == "workflow":
                self.workflow_files.append([root, files])
            
            # Check for test-related files or directories
            if re.search("test", os.path.basename(root), re.IGNORECASE):
                matched_files = [file for file in files if re.search("test", file, re.IGNORECASE)]
                if matched_files:
                    self.test_files.append([root, matched_files])
            
            # Check each file for artifacts
            for filename in files:
                run_test.checkFile(filename, self.check_artifacts)
    
    def get_artifact_list(self):
        """
        Get the list of artifacts found during the scan.
        """
        return self.check_artifacts

    def get_test_files(self):
        """
        Get the list of test files found in the repository.
        """
        return self.test_files

    def get_workflow_files(self):
        """
        Get the list of workflow files found in the repository.
        """
        return self.workflow_files
