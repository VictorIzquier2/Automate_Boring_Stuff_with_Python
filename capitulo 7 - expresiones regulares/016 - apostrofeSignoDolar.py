import re

beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello word!')
print(mo)

mo2 = beginsWithHello.search('He said Hello.') == None
print(mo2)

endsWithNumber = re.compile(r'\d$')
mo3 = endsWithNumber.search('Your number is 42')
print(mo3)

mo4 = endsWithNumber.search('Your number is forty two.') == None
print(mo4)

wholeStringIsNum = re.compile(r'^\d+$')
mo5 = wholeStringIsNum.search('1234567890')
print(mo5)

mo6 = wholeStringIsNum.search('12345xyz67890') == None
print(mo6)

mo7 = wholeStringIsNum.search('12    34567890') == None
print(mo7)