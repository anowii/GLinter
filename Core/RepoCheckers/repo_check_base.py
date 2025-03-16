
class RepoCheck:
    """Base class for all repository checks."""
    def __init__(self, folder_path, check_type):
        self.folder_path = folder_path
        self.check_type = check_type
        self.score = 0
        self.amount_of_files = 0
    
    def run_check(self):
        """Run the specific check (to be overridden)."""
        pass

    def update_score(self):
        self.score = self.score + 1

    def get_file_amount(self):
        """Return the max score for this check."""
        pass

    def get_score(self):
        pass

    def get_type(self):
        return self.check_type

    def format_results(self):
        """Format results for output."""
        pass
    
    def print_formatted_list(self):
        """Prints a formatted list."""
        pass
