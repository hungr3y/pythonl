import os

testVar = "C:\\Source\\pythonl\\module_os_testing"
print(os.path.basename(testVar))

helloFile = open(testVar + '\\newtext1.txt','w')
helloFile.write('Hello, world!\n')
helloFile.close()

helloFile = open(testVar + '\\newtext1.txt','a')
helloFile.write('i\'m banana')
helloFile.close()

helloFile = open(testVar + '\\newtext1.txt')
contentRead = helloFile.read()
contentReadlines = helloFile.readlines()
helloFile.close()

print(contentRead)
print('\n**********************************\n')
