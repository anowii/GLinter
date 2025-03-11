import json, os, subprocess


class LeakChecker():
    def __init__(self, target_folder: str):
            self.target_folder= target_folder
            self.gitleak_json = "gitleaks-report.json"
            self.gitleak_folder = "Reports/"
            self._run_gitleaks()
            self.gitleak_list = self.load_report()

    def remove_old_files(self):
        path_to_file = os.path.join(self.gitleak_folder, self.gitleak_json)
        command = ["touch", path_to_file]

        if not os.path.isdir(self.gitleak_folder):
            os.makedirs(self.gitleak_folder)

        if os.path.exists(path_to_file):
            os.remove(path_to_file)
        subprocess.run(command, capture_output=True,text=True)
        
        
    def _run_gitleaks(self):
        self.remove_old_files()
        command = ["gitleaks", "detect", "-v", "--report-path", "Reports/gitleaks-report.json", "--source", self.target_folder]
        result = subprocess.run(command,capture_output=True, text=True)
        return result.returncode == 0, result.stderr

    def print_gitleak(self):
        gitleaks_command = ["gitleaks", "detect", "-v", "--report-path", "Reports/gitleaks-report.json", "--source", self.target_folder]
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
        print(self.gitleak_folder,self.gitleak_json)
        with open(self.gitleak_folder+self.gitleak_json, "r") as file:
            data = json.load(file)  
        return data


"""
if __name__ == "__main__":
    checker = LeakChecker("../GLinter")
    print(checker.load_report())
    print(checker.print_gitleak())
"""
    