import re

phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # Tiene grupos
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

if __name__ == '__main__':
  # print(mo.group())
  for phone in mo: print(phone)