import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('My number is 415-555-4242.')
if mo:
  print('Phone number found: ' + mo.group())
else:
  print('No phone number found.')