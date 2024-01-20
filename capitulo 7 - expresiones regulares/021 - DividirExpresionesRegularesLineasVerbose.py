import re

phoneRegex = re.compile(r'''(
  (\d{3}|\(\d{3}\))?            # codigo de area
  (\s|-|\.)?                    # separador
  \d{3}                         # primeros 3 dígitos
  (\s|-|\.)                     # separador
  \d{4}                         # 4 últimos dígitos
  (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
  )''', re.VERBOSE)

mo = phoneRegex.search('Mi teléfono es (954) 394 6490 ext. 34.')
print(mo.group())