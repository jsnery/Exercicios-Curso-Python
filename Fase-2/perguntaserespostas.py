import os


def clear():
    os.system('cls')


examQuestions = [
    {
        'Pergunta': 'Quanto é 5 + 5?',
        'Opcoes': ['1', '4', '12', '10'],
        'Resposta': '10',
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opcoes': ['55', '25', '12', '10'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 5 elevado a 5?',
        'Opcoes': ['125', '150', '3125', '2550'],
        'Resposta': '3125',
    },
]

rightQuestions = 0
for pergunta in examQuestions:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    questionsOptions = pergunta['Opcoes']
    questions = ''
    for i, options in enumerate(questionsOptions, 1):
        questions += f'{i}) {options}\n'

    print(questions)
    userAnswer = input("Escolha: ")

    userAnswerInt = None
    while True:
        if userAnswer.isdigit():
            userAnswerInt = (int(userAnswer) - 1)

            verification = (userAnswerInt < len(
                questionsOptions)) and (not userAnswerInt < 0)

            if verification:
                if questionsOptions[userAnswerInt] == pergunta['Resposta']:
                    print('Acertou! 🤩')
                    rightQuestions += 1
                    break
                else:
                    print('Errou! 😞')
                    break

            else:
                clear()
                print('Digite uma opção válida!\n')
                print(questions)
                userAnswer = input("Escolha: ")
                continue

        else:
            clear()
            print('Digite uma opção válida!\n')
            print(questions)
            userAnswer = input("Escolha: ")

    print()

print('Você errou tudo! 😞' if rightQuestions == 0 else f'Você acertou {rightQuestions} de {len(examQuestions)}! 🤩')
