import io
import os
import sys
import subprocess
import gitpy
workbranchFileName = '.settings/workbranch.git'

def main():
    os.system("ww.cmd")
    branchName = gitpy.getWorkBranchName()
    if len(branchName)==0:
       print("No information about working branch. Use parameter for create one")
       sys.exit()
    os.system('git push origin '+branchName)	

main()