import io
import os
import sys
import subprocess
import gpc



def getRemotreBranches():
    p = subprocess.Popen('git ls-remote', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.stdout.readlines()
    retval = p.wait()
    
    branches = set()
    for bytes in output:
        line = bytes.decode('utf-8')
        
        b = line.strip()
        a = b.split('\t')

        if len(a) < 2:
          continue

        a = a[1].split('/')
        if len(a)<2:
           continue

        b = a[len(a)-1]
        branches.add(b)

    return branches


def getLocalBranches():
    p = subprocess.Popen('git branch', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.stdout.readlines()
    retval = p.wait()

    response = {}
    
    branches = set()
    for bytes in output:
        line = bytes.decode('utf-8')
        #print(line)
        b = line.strip()
        a = b.split(' ')


        if(a[0]=='*'):
           b = a[1].strip()
           response['current'] = b
        branches.add(b)

    response['branches']  = branches
    return response

def getAllBranches():
    response = getLocalBranches()
    response['branches'].update(getRemotreBranches())
    return response


def toRoot():
   if os.path.isdir(".git"):
      return True
   cwd = os.getcwd()
   if cwd == '/' or len(cwd)==3 and cwd.endswith("\\"):
      return False

   os.chdir("..")
   return toRoot()

def getWorkBranchName():
    try:
      with io.open(gpc.workbranchFileName, 'r', encoding='utf8') as fin:
        lines=fin.readlines()
        if len(lines)<1:
          print("No information about working branch. Use parameter for create one")
          return ""
        branchName = lines[0].strip()
        return branchName
    except IOError:
        return ""
