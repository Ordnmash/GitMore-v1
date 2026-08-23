# this code is used to clean the commits.txt to remove unecessary commits messages or non-english commits
def remove_fromData(symbol: str):
  for i,c in commits:
    if symbol in c:
      commits.pop(i)
      i-=1
  return #None

remove_fromData('~')
