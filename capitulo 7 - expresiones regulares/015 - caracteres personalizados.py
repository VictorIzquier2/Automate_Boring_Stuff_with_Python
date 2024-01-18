import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)