import json, os, subprocess


class LeakChecker():
    def __init__(self, target_folder: str):
            self.target_folder= target_folder
            self.gitleak_json = "gitleaks-report.json"
            self.gitleak_folder = "Gitleaks/"
            self._run_gitleaks
            self.gitleak_list = self.load_report()

    def remove_old_files(self):
        target = self.gitleak_folder + self.gitleak_json

        if not os.path.isdir(self.gitleak_folder):
            os.makedirs(self.gitleak_folder)

        if os.path.exists(target):
            os.remove(target)
        
        
    def _run_gitleaks(self):
        self.remove_old_files()
        command = ["gitleaks", "detect", "-v", "--report-path", "Gitleaks/gitleaks-report.json", "--source", self.target_folder]
        result = subprocess.run(command,capture_output=True, text=True)
        return result.returncode == 0, result.stderr

    def print_gitleak(self):
        gitleaks_command = ["gitleaks", "detect", "-v", "--report-path", "Gitleaks/gitleaks-report.json", "--source", self.target_folder]
        grep_command = ["grep", "-E", "commits scanned|scan completed|leaks found"]

        with subprocess.Popen(gitleaks_command, stdout=subprocess.PIPE) as gitleaks_proc:
            with subprocess.Popen(grep_command, stdin=gitleaks_proc.stdout, stdout=subprocess.PIPE, text=True) as grep_proc:
                return grep_proc.communicate()[0]
            
        
    def load_report(self):
        with open(self.gitleak_folder+self.gitleak_json, "r") as file:
            data = json.load(file)  
        return data

"""
if __name__ == "__main__":
    checker = LeakChecker("ClonedRepo")
    print(checker.load_report())
    print(checker.print_gitleak())
"""
    