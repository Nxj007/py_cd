#from collections import Counter
'''def is_anagram(str1, str2):
	return Counter(str1) == Counter(str2)
'''
# or without having to import anything
def is_anagram(str1, str2):
	return sorted(str1) == sorted(str2)

print(is_anagram('geek', 'eegk'))
print(is_anagram('aded','dade'))
#print(is_anagram('geek', 'peek'))	
