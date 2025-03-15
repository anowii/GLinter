import json, subprocess, os
from Core.utils import clean_reports


class LeakChecker():
    def __init__(self, target_folder: str):
        self.target_folder= target_folder
        self.file_path = "Reports/gitleaks-report.json"
        self.run_gitleaks()
        self.gitleak_list = self.load_report() 

        
    def run_gitleaks(self):
        command = ["gitleaks", "detect", "-v", "--report-path", self.file_path , "--source", self.target_folder]
        result = subprocess.run(command,capture_output=True, text=True)
        return result.returncode == 0, result.stderr

    def print_gitleak_highlights(self):
        gitleaks_command = ["gitleaks", "detect", "-v", "--report-path", self.file_path, "--source", self.target_folder]
        grep_command = ["grep", "-E", "commits scanned|scan completed|leaks found"]

        with subprocess.Popen(gitleaks_command, stdout=subprocess.PIPE) as gitleaks_proc:
            with subprocess.Popen(grep_command, stdin=gitleaks_proc.stdout, stdout=subprocess.PIPE, text=True) as grep_proc:
                return grep_proc.communicate()[0]
            
    def print_gitleak_report(self):
        print("="*90)
        for entry in self.gitleak_list:
            print(f" [Description: {entry['Description']}], [Author: {entry['Author']}]")
            print(f" [File: {entry['File']}], [Secret: {entry['Secret']}]")
            print("-"*90)


    def load_report(self):
        if os.path.isfile(self.file_path):
            with open(self.file_path, "r") as file:
                data = json.load(file)  
            return data
        else:
            return []