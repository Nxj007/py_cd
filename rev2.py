## initializing string
string = "GeeksforGeeks"
## initializing a dictionary
duplicates = {}
for char in string:
   if char in duplicates:
      ## increasing count if present
      duplicates[char] += 1
   else:
      ## initializing count to 1 if not present
      duplicates[char] = 1
for key, value in duplicates.items():
   if value > 1:
      print(key, end = " ")
print()