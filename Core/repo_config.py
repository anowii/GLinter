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
