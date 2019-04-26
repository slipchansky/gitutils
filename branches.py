import gitpy

a = gitpy.getAllBranches()

for b in a['branches']:
  print(b)

print("\nCurrent: '"+a['current']+"'")
