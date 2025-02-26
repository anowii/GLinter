# GLinter - Repository Linter 


## Problem Statement
Not all development projects that are published on GitHub are done in a professional manner. This can lead to security and other issues, and it is, in general, not professional. For example, you should never store credentials in a repository since searching for and using them for malicious purposes is easy. Furthermore, it is essential to have a .gitignore file to exclude files that should not be stored in the repository, such as build artifacts.

## Goal of the Project
The goal of this project is to create a tool that can check a GitHub repository for common issues and provide a report to the user. A user should be able to see and fix the issues that are
found in their repository. Especially in the context of university projects, this tool can be helpful to ensure that students follow best practices when publishing their code.

## Requirements
General
RQ1.1: The system shall take a URL to a GitHub repository as an argument
 RQ1.2: The system shall take a folder path to a git repository as an argument
 RQ1.3: The system shall summarize all findings with an indicator for passed or failed checks
Artifacts
RQ2.1: The system shall check whether a .gitignore file exists
RQ2.2: The system shall check whether a LICENSE file exists
RQ2.3: The system shall check whether GitHub workflow files exist
 RQ2.4: The system shall list all files with their complete file path that includes the word test
Security
RQ3.1: The system shall facilitate a tool to check for credentials that should not be stored in the repository
Contributions
RQ4.1: The system shall summarize the number of commits
RQ4.2: The system shall summarize the git names of contributors

Optional Requirements
RQ5.1: The system shall be containerized via Docker to remove the necessity of having all dependencies installed
RQ5.2: The system shall clone a GitHub repository locally for further inspections
 RQ5.3: The system shall be able to batch process multiple repositories
