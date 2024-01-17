import re

phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumberRegex.search('My number is 415-55-424.')
print(f'Phone number found: {mo.group()}')