import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')

if __name__ == '__main__':
  print(mo.group(1))
  print(mo.group(2))
  print(mo.group(0))
  print(mo.group())