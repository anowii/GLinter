import os 
import argparse
import re, sys
import run_test

check_artifacts = [False,False,False]
test_files = []
workflow_files = []
#gitleaks.exe --path="C:\Users\Documents\GitHub\GlinterFolder\GLinter" --report="C:\Users\Documents\GitHub\GlinterFolder\GLinter\gitleaks_report.json"
#https://github.com/anowii/clone-this-test.git

def main():
    
    print("=" * 90, "")
    print( "\t\t\t\tWelcome to the GLinter Tool!")
    print("=" * 90, "")
    # Init Parser
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help='Path/URL to target')
    args = parser.parse_args()
    target = args.arg1

    print(f"Target argument:  {target}\n")
    run_test.clean_folder()
    print("-" * 90, "") 

    print(" CHECKING FOR ARTIFACTS")
    try:
        ################## URL ##################
        if(re.match(r"^http", target)):
            if (run_test.cloneURL(target)==0):
                target = "ClonedRepo\\"
                for root, dirs, files in os.walk(target, topdown=True):
                    #print(root, dirs, files)
                    if os.path.basename(root).lower() == "workflow":
                        workflow_files.append(["workflow",files])         
                    if(re.search("test", os.path.basename(root), re.IGNORECASE)):
                        temp_match = [file for file in files if re.search("test", file, re.IGNORECASE)]
                        test_files.append([os.path.basename(root),temp_match])
                    else:
                        temp_match = [file for file in files if re.search("test", file, re.IGNORECASE)]
                        if temp_match:
                            test_files.append([os.path.basename(root),temp_match])
                    for filename in files:
                        run_test.checkFile(filename, check_artifacts)
            run_test.printResults(target,check_artifacts,test_files, workflow_files)
        ################## FOLDER ##################
        elif(run_test.validPath(target) == 0):
            #target = target.replace("\\", "\\\\")
            for root, dirs, files in os.walk(target, topdown=True):
                print(root, dirs, files)
                if os.path.basename(root).lower() == "workflow":
                    workflow_files.append(["workflow",files])         
                if(re.search("test", os.path.basename(root), re.IGNORECASE)):
                    temp_match = [file for file in files if re.search("test", file, re.IGNORECASE)]
                    test_files.append([os.path.basename(root),temp_match])
                else:
                    temp_match = [file for file in files if re.search("test", file, re.IGNORECASE)]
                    if temp_match:
                        test_files.append([os.path.basename(root),temp_match])
                for filename in files:
                    run_test.checkFile(filename, check_artifacts)
            run_test.printResults(target,check_artifacts,test_files, workflow_files)
    

    except argparse.ArgumentError as e:
        parser.print_help()
    print(f" CHECKING SECURITY {target}")
    print("-" * 90, "") 
    run_test.checkSecurity(target)

    print("=" * 90, "\n")
    #print(workflow_files)
    #print(test_files)

if __name__ == "__main__":
    main()