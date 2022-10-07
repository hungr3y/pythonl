# Ticket Randomizer - создает экзаминационные билеты с вопросами и ответами, расположенными в случайном порядке, вместе с ключами ответов

import random

# Данные билета. Ключи - названия штатов, значения - столицы

capitals = {'Alabama': 'Montgomery','Alaska': 'Juneau','Arizonaa':'Phoenix', 'Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connnecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahasssee', 'Georgia': 'Atlanta}', 'Alabama1': 'Montgomery1','Alaska1': 'Juneau1','Arizonaa1':'Phoenix1', 'Arkansas1': 'Little Rock1',
            'California1': 'Sacramento1', 'Colorado1': 'Denver1', 'Connnecticut1': 'Hartford1', 'Delaware1': 'Dover1',
            'Florida1': 'Tallahasssee1', 'Georgia1': 'Atlanta1'}

# Генерация списка билетов

for quizNum in range(3):
    #TODO cоздать файлы билетов и ключей ответов
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')

    #TODO Hаписать заголовок билета
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    quizFile.write('Name:\n\nDate:\n\nYear:\n\n')
    quizFile.write((' ' * 15) +
                   'Proverka znaniy stolits shtatov (Ticket %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    #TODO Перемешать порядок следования штатов

    states = list(capitals.keys())
    random.shuffle(states)

    #TODO Организовать цикл по всем 50 штатм, создавая вопрос для каждого
    for questionNume in range(len(capitals)):
        correctAnswer = capitals[states[questionNume]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        #TODO Записать варианты вопросов и ответов в файл билета
        quizFile.write('%s. Vibirite stolitsu shtata %s.\n' % (questionNume + 1, states[questionNume]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        #TODO Записать ключ ответа в файл
        answerKeyFile.write('%s. %s\n' % (questionNume + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()



