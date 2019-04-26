import gitpy
import gpc
import os


def main():
 os.system("ww.cmd")
 branchName = gitpy.getWorkBranchName()
 
 if len(branchName)==0:
    print("No information about working branch. Use parameter for create one")
    sys.exit()

 if branchName==gpc.developBranchName or branchName==gpc.masterBranchName:
    print("Can't delete branch '"+branchName+"'")
    return

 os.system("dev.py")
 os.system("git branch -D "+branchName)
 os.system("git push origin --delete "+branchName)

main()
