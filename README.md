# GLinter Tool

## Project Aim and Objective
The goal of GLinter is to provide a repository linter that ensures repositories follow best practices for structure, security, and documentation. The tool is be a CLI-based solution that allows users to evaluate if your repository follow best practices.

### Prerequisites
- Python 3.12.3: could most likely work with other versions
- Clone the repository to use the tool
- Install denpendencies with ```pip install -r requirements.txt```
- To run with gitleaks ```sudo apt-get install gitleaks```
- To run w/o gitleaks set ```"git_leaks_check":false```

### Runnning the Prototype
```python GLinter.py --url <GIT_REPO_URL>```
or 
```python GLinter.py --dir <LOCAL_FOLDER>```

### Configuration Files
In the configuration file ```config.json``` you can specify where you want the cloned repo to end up. If you are using the command ```--dir <LOCAL_FOLDER>``` the program will use the path to specified for the local folder. But you can still skip checks using the config file.  
```
[
    { "cloned_dirpath": "NewRepo" },
    {
      "git_leaks_check": true,
      "artifact_check": true,
      "test_check": false,
      "commit_contribute_check": false
    }
]
```
For further configurations with .gitignoreleaks check out: [GITLEAKS](https://github.com/gitleaks/gitleaks)

### Good to know 
- All core classes and functions is found in the **Core** Folder
- Gitleaks will produce a report file in json format in the **Reports** folder
- The unit_test.py is not a valuble unittest

## Best Practices 
- The repository contains a readme.md file 
- The repository contains a .gitignore file 
- The repository contains a license file 
- The repository contains test files/unittests


