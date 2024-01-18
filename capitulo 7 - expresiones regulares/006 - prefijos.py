import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')

if __name__ == '__main__':
  print(mo.group())
  print(mo.group(1))