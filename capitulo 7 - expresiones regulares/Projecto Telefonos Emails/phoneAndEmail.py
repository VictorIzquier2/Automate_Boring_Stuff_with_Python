import pyperclip, re

phoneRegex = re.compile(r'''(
  (\d{3}|\(\d{3}\))?              # código de área
  (\s|-|\.)?                      # Separador
  (\d{3})                         # Primeros tres dígitos
  (\s|-|\.)                       # Separador
  (\d{4})                         # Últimos 4 dígitos
  (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extensión      
  )''', re.VERBOSE)

# Create email regex
emailRegex = re.compile(r'''(
  [a-zA-Z0-9._%+-]+               # usuario
  @                               # @ simbolo
  [a-zA-Z0-9.-]+                  # nombre del dominio
  (\.[a-zA-Z]{2,4})               # punto algo
)''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
  phoneNum = '-'.join([groups[1], groups[3], groups[5]])
  if groups[8] != '':
    phoneNum += ' x' + groups[8]
  matches.append(phoneNum)
for groups in emailRegex.findall(text):
  matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
  pyperclip.copy('\n'.join(matches))
  print('Copied to clipboard:')
  print('\n'.join(matches))
else:
  print('No phone numbers or email addresses found.')

