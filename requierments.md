# Project Requirements & Implementation Tasks

This document outlines the system requirements and the corresponding tasks needed for implementation.

## 📌 General
- [ ] **RQ1.1:** Support GitHub repository URLs  
  - [x] Parse repository URL input  
  - [x] Clone repository to a local folder  
  - [x] Validate if it's a git repository  

- [ ] **RQ1.2:** Support local folder paths to Git repositories  
  - [x] Verify folder existence  
  - [ ] Check if `.git` folder exists  

- [ ] **RQ1.3:** Summarize findings with pass/fail indicators  
  - [ ] Define a standard output format for results  
  - [ ] Implement result aggregation logic  
  - [ ] Assign pass/fail status for each check  

- [ ] **RQ1.4:** Allow configuring the clone/cache folder via config file  
  - [ ] Implement configuration file parsing  
  - [ ] Allow specifying clone/cache directory  
  - [ ] Validate user-provided paths  

- [ ] **RQ1.5:** Allow certain checks to fail (configurable)  
  - [ ] Add config flag to define optional checks  
  - [ ] Implement logic to skip or report warnings for optional failures  

- [ ] **RQ1.6:** Return exit status codes  
  - [ ] Define exit codes (`0` for success, non-zero for failure)  
  - [ ] Implement exit code handling  
  - [ ] Test different failure scenarios  

---

## 📂 Artifacts
- [ ] **RQ2.1:** Check if a `.gitignore` file exists  
  - [ ] Look for `.gitignore` in the root of the repository  
  - [ ] Output result  

- [ ] **RQ2.2:** Check if a `LICENSE` file exists  
  - [ ] Search for `LICENSE` or `LICENSE.txt`  
  - [ ] Output result  

- [ ] **RQ2.3:** Check if GitHub workflow files exist  
  - [ ] Look in `.github/workflows/` directory  
  - [ ] Output result  

- [ ] **RQ2.4:** List all files with “test” in the name  
  - [ ] Scan repository files  
  - [ ] Filter filenames containing “test”  
  - [ ] Output complete file paths  

- [ ] **RQ2.5:** Ignore files and directories listed in `.gitignore`  
  - [ ] Parse `.gitignore`  
  - [ ] Exclude ignored files when processing  

---

## 🔒 Security
- [ ] **RQ3.1:** Detect secrets stored in the repository  
  - [x] Integrate with a tool like `Gitleaks` or implement regex-based scanning  
  - [x] Scan all text files for potential credentials  
  - [ ] Provide a report on detected secrets  

---

## 👥 Contributions
- [ ] **RQ4.1:** Summarize the number of commits  
  - [ ] Run `git rev-list --count HEAD`  
  - [ ] Output total commits  

- [ ] **RQ4.2:** Summarize contributor names  
  - [ ] Run `git log --pretty=format:%an | sort -u`  
  - [ ] Output unique contributor names  

- [ ] **RQ4.3:** Rank contributions by commit count  
  - [ ] Run `git shortlog -s -n`  
  - [ ] Sort and display commit counts per contributor  

--

Use this checklist to track progress and mark off completed requirements! ✅  
