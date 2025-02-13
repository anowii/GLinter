import os
import argparse
import re

check_list = [0,0,0,0]
test_files = []

#******************* FUNCTIONS *******************#
#*************************************************#

def validPath(dirPath):
    return os.path.exists(dirPath)

def checkFile(filename):
    if(filename == "README.md"):
        check_list[0] = 1
        return
    if(filename == "LICENSE"):
        check_list[1] = 1
        return
    if(filename == ".gitignore"):
        check_list[2] = 1
        return
    if(filename == "build.yml"):
        check_list[3] = 1
        return

def printResults():
    if(check_list[0] == 1):
        print(" README.md:", " "* 7 , "OK")
    else:
        print(" README.md:", " "*7 , "N/A")
    if(check_list[1] == 1):
        print(" LICENSE:", " "* 9 , "OK")
    else:
        print(" LICENSE:"," "* 9 ,"N/A")
    if(check_list[2] == 1):
        print(" .gitignore:", " "* 6 , "OK")
    else:
        print(" .gitignore:", " "*6 , "N/A")
    if(check_list[3] == 1):
        print(" workflow:"," "* 8 , "OK")
    else:
        print(" Workflow:"," "* 8 , "N/A")  
    print("-" * 30, "")
    if(test_files):
        print(" Filename w/ test: ")
        for file in test_files:
            print(f"   {file}")
    else:
        print(" Filename w/ test:  N/A")
#******************************************************#
#******************************************************#


def main():

    # Init Parser
    parser = argparse.ArgumentParser()
    parser.add_argument('ARG', help='Path/URL to target')

    print("=" * 50, "")
    print( "\t Welcome to the GLinter Tool!")
    print("=" * 50, "")

    try:
        args = parser.parse_args()
        print(f"Target argument:  {args.ARG}\n")

        print("-" * 30, "")
        print("   Checking for Artifacts!")
        print("-" * 30, "")
        if(validPath(args.ARG)):
            target = args.ARG
            for root, dirs, files in os.walk(target):
                for filename in files:
                    checkFile(filename)
                    if(re.search("test", filename, re.IGNORECASE)):
                        test_files.append(root + filename)
            printResults()
        print("-" * 30, "")

    except argparse.ArgumentError as e:
        parser.print_help()



    print("=" * 50, "\n")

if __name__ == "__main__":
    main()