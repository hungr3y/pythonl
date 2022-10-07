import re, pyperclip


testtext = '845.123.5243, 865-123-5456, takoi vot jujutsu_kaisen@part.zero part< tekst 654 123 6343 and emails privet@kakdela.ru, takje 09ou@just.ju'
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?                  # area code    
(\s|-|\.)?                          # separater
(\d{3})                             # first 3 numbers
(\s|-|\.)                           # separater
(\d{4})                             # last four numbers
(\s*(ext|x|ext.)\s*\d(2,5))?        # ext code
)''', re.VERBOSE)


#  regex for emails

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+           # first part of email
@                           # @
[a-zA-Z0-9.-]+              # domain
(\.[a-zA-Z]{2,4})           # last part
)''', re.VERBOSE)

#  find in text pattern

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# copy results to the bufer

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied in buffer')
    print('\n'.join(matches))
else:
    print('nothing was found')





'''
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Найденный телефонный номер: ' + chunk)
print('done.')
'''
