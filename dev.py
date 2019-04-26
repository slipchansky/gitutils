import io
import os
import sys
import subprocess

mainBranchFileName = '.settings/mainbranch.git'

developBranchName = 'develop'

try:
    with io.open(mainBranchFileName, 'r', encoding='utf8') as fin:
      lines=fin.readlines()
      if len(lines)>0:
        developBranchName = lines[0].strip()
        print("Main branch is '"+developBranchName+"'")
except FileNotFoundError:
        print("Main branch is '"+developBranchName+"'")

os.system('git checkout '+developBranchName)