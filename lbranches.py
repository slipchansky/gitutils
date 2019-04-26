import gitpy

a = gitpy.getLocalBranches()

for b in a['branches']:
  print(b)

print("\nCurrent: '"+a['current']+"'")

