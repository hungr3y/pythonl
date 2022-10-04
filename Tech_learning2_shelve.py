import shelve, pprint

shelfFile = shelve.open('mydata1')
catz = ['asd', 'asd']
shelfFile['cats1'] = catz
shelfFile.close()
a = [{'da': 'oui'}, {'privet1': 'HAIBULAHIZ', 'privet2': 'ISAMISES', 'privet3': 'OLA'}]
