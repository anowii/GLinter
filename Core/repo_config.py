import json

class RepoConfig:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.data = self.load_json()

    def load_json(self):
        """Loads and parses the JSON file."""
        try:
            with open(self.json_file_path, 'r') as file:
                data = json.load(file)
                return data
        except Exception as e:
            print(f"Error loading JSON file: {e}")
            return []

    def check_config(self):
        """Check if the JSON contains the necessary keys."""
        if not self.data:
            print("Error: JSON data is empty or invalid.")
            return False

        cloned_dirpath = self.data[0].get("cloned_dirpath")
        if not cloned_dirpath:
            print("Error: 'cloned_dirpath' key is missing.")
            return False

        checks = self.data[1] if len(self.data) > 1 else {}
        valid_checks = [
            "git_leaks_check",
            "artifact_check",
            "test_check",
            "commit_contribute_check",
        ]

        for check in valid_checks:
            if check not in checks:
                print(f"Warning: {check} is missing.")
        
        return True

    def get_cloned_dirpath(self):
        """Get the cloned directory path."""
        return self.data[0].get("cloned_dirpath")

    def get_checks(self):
        """Get the checks configuration."""
        if len(self.data) > 1:
            return self.data[1]
        return {}
    
    def get_config(self):
        return self.data[0].get("cloned_dirpath"), self.data[1]
