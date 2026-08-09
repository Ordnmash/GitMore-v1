# this code is used to clean the commits.txt to remove unecessary commits messages or non-english commits
def remove_fromData(symbol):
  for i,c in commits:
    if symbol in c:
      commits.pop(i) # note that data would change indexes as you pop 

remove_fromData('$')
# then all commits containing '$' are removed if less than 100 commits, you might need to re-call the function if there are commits containing the unwanted symbols
