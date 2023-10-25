# criar um programa para gerar um numero aleatório e fazer com que o úsuario adivinhe o número

from random import randint
from time import sleep

n = randint(1, 30)
chances = 0
cont = 0

print('\033[31mAdivinhando um número\033[m')
sleep(1)

while cont < 3:
    print('\033[1;31mCARREGANDO...\033[m\n')
    cont += 1
    sleep(1.5)

print('\033[1mVocê tem 5 tentativas para adivinhar o número (DE 1 A 30) que o computador escolheu.')

while True:
    resp = int(input('Digite o número que você acha que o computador escolheu:\033[m '))
    if resp == n:
        print(f'\033[1;36mPARABÉNS!!! Você acertou! O valor que o computador escolheu foi: {n}\033[m')
        break
    chances += 1
    if chances < 5:
        if resp < n:
            sleep(0.3)
            print('\033[1mVocê errou!!! Dica: O número que o computador escolheu é maior...')
            sleep(0.3)
        if resp > n:
            sleep(0.3)
            print('Você errou!!! Dica: O número que o computador escolheu é menor...')
    if chances == 3:
        print(f'\033[1;31m2 TENTATIVAS RESTANTES \033[m')
    if chances == 5:
        sleep(1)
        print(f'\033[1;31mSuas tentativas expiraram. O número que o computador escolheu foi: \033[1m{n} ')
        break
