import os 
import argparse
import re, sys
import run_test

check_list = [0,0,0,0]
test_files = []

def main():
    
    # Init Parser
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help='Path/URL to target')
    args = parser.parse_args()
    target = args.arg1

    run_test.clean_folder()

    print("=" * 50, "")
    print( "\t Welcome to the GLinter Tool!")
    print("=" * 50, "")
    print(f"Target argument:  {target}\n")
    print("-" * 30, "")
        

    try:
        print("   Checking for Artifacts!")
        print("-" * 50, "")
        if(run_test.validURL(target)==0):
            print("yay")
            sys.exit(1)
        elif(run_test.validPath(target) == 0):
            for root, dirs, files in os.walk(target):
                for filename in files:
                    #print(root+filename)
                    run_test.checkFile(filename, check_list)
                    if(re.search("test", filename, re.IGNORECASE)):
                        test_files.append(root + filename)
            run_test.printResults(check_list,test_files)
            print("-" * 30, "")

    except argparse.ArgumentError as e:
        parser.print_help()



    print("=" * 50, "\n")



if __name__ == "__main__":
    main()