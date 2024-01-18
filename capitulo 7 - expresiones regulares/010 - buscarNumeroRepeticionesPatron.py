import re

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo2 = haRegex.search('Ha')

if __name__ == '__main__':
  print(mo1.group())
  print(mo2 == None)