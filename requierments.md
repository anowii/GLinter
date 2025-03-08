# Project Requirements & Implementation Tasks

This document outlines the system requirements and the corresponding tasks needed for implementation.

## 📌 General
- [x] **RQ1.1:** Support GitHub repository URLs  
  - [x] Parse repository URL input  
  - [x] Clone repository to a local folder  
  - [x] Validate if it's a git repository  

- [ ] **RQ1.2:** Support local folder paths to Git repositories  
  - [x] Verify folder existence  
  - [ ] Check if `.git` folder exists  

- [ ] **RQ1.3:** Summarize findings with pass/fail indicators  
  - [x] Define a standard output format for results  
  - [ ] Implement result aggregation logic  
  - [x] Assign pass/fail status for each check  

- [ ] **RQ1.4:** Allow configuring the clone/cache folder via config file  
  - [x] Implement configuration file parsing  
  - [ ] Allow specifying clone/cache directory  
  - [x] Validate user-provided paths  

- [ ] **RQ1.5:** Return exit status codes  
  - [ ] Define exit codes (`0` for success, non-zero for failure)  
  - [ ] Implement exit code handling  
  - [ ] Test different failure scenarios  

---

## 📂 Artifacts
- [ ] **RQ2.1:** Check if a `.gitignore` file exists  
  - [x] Look for `.gitignore` in the root of the repository  
  - [x] Output result  
  - [ ] Final touches on output

- [ ] **RQ2.2:** Check if a `LICENSE` file exists  
  - [x] Search for `LICENSE` or `LICENSE.txt`  
  - [ ] Output result / final touches

- [ ] **RQ2.3:** Check if GitHub workflow files exist  
  - [x] Look in `.github/workflows/` directory  
  - [ ] Output result  

- [ ] **RQ2.4:** List all files with “test” in the name  
  - [x] Scan repository files  
  - [x] Filter filenames containing “test”  
  - [x] Output complete file paths  

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
- [x] **RQ4.1:** Summarize the number of commits  
  - [x] Run `git rev-list --count HEAD`  
  - [x] Output total commits  

- [x] **RQ4.2:** Summarize contributor names  
  - [x] Run `git log --pretty=format:%an | sort -u`  
  - [x] Output unique contributor names  

- [x] **RQ4.3:** Rank contributions by commit count  
  - [x] Run `git shortlog -s -n`  
  - [x] Sort and display commit counts per contributor  

--

Use this checklist to track progress and mark off completed requirements! ✅  
