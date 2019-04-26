import io
import os
#import re
import sys
#import requests
import subprocess
#import lxml.etree as ET
import gitpy
import gpc


def toBranch(branchName):
    print('Switching to branch '+branchName)

    br = gitpy.getAllBranches();
    
    found = False
    inBranch = br['current']==branchName
    if inBranch:
       found = True
    else:
       for b in br['branches']:
         if(b==branchName):
           found = True

    if (found):
       if (inBranch):
         print('Already in work branch '+branchName)
       else:
         print('Switch to existing branch '+branchName)
         os.system('git checkout '+branchName)
    else:
       print('Switch to origin branch '+gpc.developBranchName)
       os.system('git checkout '+gpc.developBranchName)
       print('Switch to new branch '+branchName)
       os.system('git checkout -b '+branchName)


    with io.open(gpc.workbranchFileName, 'w', encoding='utf8') as fout:
      fout.write(branchName)


    

def towork():
    branchName = gitpy.getWorkBranchName()
    if len(branchName)==0:
      print("No information about working branch. Use parameter for create one")
      sys.exit()
    toBranch(branchName)

def relocate():
    if not gitpy.toRoot():
       print("Current directory is not in git repository")
       return false
    work = gitpy.getWorkBranchName()
    print('')
    if len(work)!=0:
       return True

    print("Get known branches...")
    local = gitpy.getAllBranches()

    bs = local['branches']
    print("Known branches are:")
    for b in bs:
       print(b)

    print("Save branch '"+local['current']+"' as working one")

    try:
       os.mkdir(gpc.settingsDirectoryName)
    except OSError:
       x = 1


    with io.open(gpc.workbranchFileName, 'w', encoding='utf8') as fo:
         fo.write(local['current'])
    return False


def main():
    if not relocate():
       return

    try:
        with io.open(gpc.mainBranchFileName, 'r', encoding='utf8') as fin:
          lines=fin.readlines()
          if len(lines)>0:
            gpc.developBranchName = lines[0].strip()
            print("Main branch is '"+gpc.developBranchName+"'")
    except FileNotFoundError:
            print("Main branch is '"+gpc.developBranchName+"'")

    if len(sys.argv) < 2:
       towork()
    else:
       branchName = sys.argv[1]
       toBranch(branchName)

main()