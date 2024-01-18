import re

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo2 = batRegex.search('The adventures of Batwowowowoman')
mo3 = batRegex.search('The Adeventures of Batman')

if __name__ == '__main__':
  print(mo1.group())
  print(mo2.group())
  print(mo3 == None)