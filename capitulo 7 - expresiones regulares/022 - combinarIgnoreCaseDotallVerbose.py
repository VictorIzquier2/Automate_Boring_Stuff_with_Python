import re

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
mo = someRegexValue.findall('This is a test string with Foo\nand a new line with fOO.')
print(mo)
someRegexValue2 = re.compile('''
foo           # Busca la cadena foo
''', re.IGNORECASE | re.DOTALL | re.VERBOSE)
mo = someRegexValue2.findall('A different test string with foo\nand another line with FOO.')
print(mo)

