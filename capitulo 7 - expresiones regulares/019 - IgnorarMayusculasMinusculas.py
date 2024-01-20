import re

robocopRegex = re.compile(r'robocop', re.I)
mo = robocopRegex.search('RoboCop is part man, part machine, all cop.')
print(mo.group())

mo = robocopRegex.search('ROBOCOP protects the innocent.')
print(mo.group())

mo = robocopRegex.search('Al, why does your programming book talk about robocop so much?')
print(mo.group())