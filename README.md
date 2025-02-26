# GLinter - Repository Linter 

## Project Aim and Objective
The goal of GLinter is to provide a repository linter that ensures repositories follow best practices for structure, security, and documentation. The tool will be a CLI-based solution that allows users to quickly evaluate repositories.

## Requirements
|**General**                                                                                  |  Status  |
|---------------------------------------------------------------------------------------------|----------|
|RQ1.1: The system shall take a URL to a GitHub repository as an argument                     |    -     |
|RQ1.2: The system shall take a folder path to a git repository as an argument                |   DONE   |
|RQ1.3: The system shall summarize all findings with an indicator for passed or failed checks |     -    |

**Artifacts**

|**General**                                                                                  |  Status  |
|---------------------------------------------------------------------------------------------|----------|
|RQ2.1: The system shall check whether a .gitignore file exists                               |   DONE   |
|RQ2.2: The system shall check whether a LICENSE file exists                                  |     -    |
|RQ2.3: The system shall check whether GitHub workflow files and folder exist                 |     -    |
|RQ2.4: The system shall list all files with their complete file path that includes the word test         |     -    |
|RQ2.3: The system shall check whether GitHub workflow files and folder exist                 |     -    |
 
 
 - RQ2.3: The system shall check whether GitHub workflow files and folder exist
 - RQ2.4: The system shall list all files with their complete file path that includes the word test ✅
    -RQ2.4.1: The system shall lista all folder with their complete filepath that includes the word test   

**Security**
 - RQ3.1: The system shall facilitate a tool to check for credentials that should not be stored in the
   repository

**Contributions**
  - RQ4.1: The system shall summarize the number of commits
  - RQ4.2: The system shall summarize the git names of contributors

**Optional Requirements**
 - RQ5.1: The system shall be containerized via Docker to remove the necessity of having all dependencies
   installed
 - RQ5.2: The system shall clone a GitHub repository locally for further inspections
 - RQ5.3: The system shall be able to batch process multiple repositories
