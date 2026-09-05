def remove_fromData(symbol: str):
  for i,c in enumerate(commits):
    if symbol in c:
      commits.pop(i)
      i-=1
  return None
remove_fromData('~')
