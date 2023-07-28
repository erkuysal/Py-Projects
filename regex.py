import re

# [*] Causes the resulting RE to match 0 or more repetitions of the preceding RE
print(" * Operator: ")

print(re.findall("ab*cd","abcde"))

print(re.findall("ab*cde","abcd"))
print(re.findall("ab*c","abcd"))

# [.] matches any character except a newline
print('\n'" . Operator: ")

print(re.findall("ab.d","abc"))
print(re.findall("ab.d","abcde"))

print(re.findall("a.c","abcde"))
print(re.findall("a.e","abcde"))

# [.*]
print('\n'" .* Operator: ")

print(re.findall("a.*","abcd"))
print(re.findall("a.*","bcde"))