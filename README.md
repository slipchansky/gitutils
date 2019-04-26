# gitutils
Git utilites


gpc.py - git common constants:
 masterBranchName = 'master'
 developBranchName = 'develop'
 settingsDirectoryName = '.settings'
 mainBranchFileName = settingsDirectoryName+'/mainbranch.git'
 workbranchFileName = settingsDirectoryName+'/workbranch.git'



ww.py, ww.cmd - work with branch

ww branch-name - [create and] switch to work branch
ww - switch to current work branch

dev.py, dev.cmd - switch to development branch
lbranches.py - list of local branches and current branch
branches.py - list of all (local and remote branches)

delbranch.py, db.cmd - switch to development branch and delete work branch locally and reotely
