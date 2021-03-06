#Máquina inteligente de fazer café e chá
#--coding:utf8;--
#python 3.6.5
from time import sleep
acucar = ' '
leite = ' '
cafe = ' '
print("""\nINSTRUÇÕES:
1. O número máximo de colheres de açúcar, leite e café é de 5 colheres.
'Se inserir mais 5 colheres o seu chá ou café estará exageradamente doce'
2. Quando não quiser acrescestar ingredientes digite 0.
""")
print('Bem vindo/a a Maquina de Café 3000')
while True:
    print("""\nFaça sua escolha!
[1] Para chá
[2] Para café
[0] Para 'PARAR' """)
    usuario = input('Sua escolha é: ')
    if usuario not in '012':
        print('Opção Invalida. Tente novamente...')
        continue
    usuario = int(usuario)
    if usuario == 1:
        print('\nVamos preparar o seu chá')
        print("""Como deseja o seu chá?
[1] Simples
[2] Com leite""")
        while True:
            cha = str(input('Sua escolha é: '))
            if cha not in '12':
                print('Opção Invalida. Tente novamente...')
                continue
            cha = int(cha)
            if cha == 1: 
                while not acucar.isdigit():
                    acucar = input('Quantas colheres de açúcar deseja? ')
                    continue
                print('Foram adicionadas {} colher/es de açúcar no seu chá.'.format(acucar))
                print('Aguarde 5 segundos e seu Chá estará pronto!')
                sleep(5)
                print('Chá pronto. Tenha um ótimo dia!')
            elif cha == 2:
                while not acucar.isdigit():
                    acucar = input('Quantas colheres de açúcar deseja? ')
                    continue
                while not leite.isdigit():
                    leite = input('Quantas colheres de leite deseja? ')
                    continue
                print('Foram adicionadas {} colher/es de açúcar no seu chá.'.format(acucar))
                print('Foram adicionadas {} colher/es de leite no seu chá.'.format(leite))
                print('Aguarde 5 segundos e seu Chá estará pronto!')
                sleep(5)
                print('Chá pronto. Tenha um ótimo dia!')
            break
    elif usuario == 2:
        print('\nVamos preparar o seu café')
        while not acucar.isdigit():
            acucar = input('Quantas colheres de açúcar deseja? ')
            continue
        while not cafe.isdigit():
            cafe = input('Quantas colheres de café deseja? ')
            continue
        print("""Deseja leite?
[1] Sim
[2] Não""")
        while True:
            usuario = input('Sua escolha é: ')
            if usuario not in '12':
                print('Opção Invalida. Tente novamente...')
                continue
            usuario = int(usuario)
            if usuario == 1:
                while not leite.isdigit():
                    leite = input('Quantas colheres de leite deseja? ')
                    continue
                print('Foram adicionadas {} colher/es de açúcar no seu café.'.format(acucar))
                print('Foram adicionadas {} colher/es de café no seu chá.'.format(cafe))
                print('Foram adicionadas {} colher/es de leite no seu chá.'.format(leite))
                print('Aguarde 5 segundos e seu Café estará pronto!')
                sleep(5)
                print('Café pronto. Tenha um ótimo dia!')
            elif usuario == 2:
                print('Foram adicionadas {} colher/es de açúcar no seu café.'.format(acucar))
                print('Foram adicionadas {} colher/es de café no seu chá.'.format(cafe))
                print('Aguarde 5 segundos e seu Café estará pronto!')
                sleep(5)
                print('Café pronto. Tenha um ótimo dia!')
            break
    elif usuario == 0:
        print('Tenha um ótimo dia!')
        break           
