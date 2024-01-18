import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')

# Parentesis
phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415)-555-4242.')

if __name__ == '__main__':
  areaCode, mainNumber = mo.groups()
  print(areaCode)
  print(mainNumber)