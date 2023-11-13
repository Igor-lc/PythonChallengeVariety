import sys
number = sys.argv[1].lower()
ends = (".png" , ".jpeg" , ".jpg" , ".gif")
number = number.endswith(ends)
print(number)