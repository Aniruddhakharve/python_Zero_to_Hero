import re

spelling = "this is brown bear "
pattern = r"brown"

search = re.search(pattern , spelling)
if search:
    print ("founded pattern is :",search.group())

else:
    print ("not found the pattern")   