import re

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('the adventures of Batwoman')

phoneRegex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo1 = phoneRegex.search('My number is 415-555-4242.')
mo2 = phoneRegex.search('My nimber is 555-4242.')


if __name__ == '__main__':
  print(mo1.group())
  print(mo2.group())