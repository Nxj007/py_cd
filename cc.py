'''
Camel Case Prg
'''

class Solution:
   def solve(self, words):
      s = "".join(word[0].upper() + word[1:].lower() for word in words)
      return s[0].lower() + s[1:]
ob = Solution()
words = ["Hello", "World", "Python", "Programming"]
print(ob.solve(words))