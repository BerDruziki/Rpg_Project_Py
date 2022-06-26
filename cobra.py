nome = input('Digite o nome do seu personagem: ')
print('É muito bom conhecer você, {}!' .format(nome))

input('Por favor, nos diga o nível do seu personagem: ')
print('Certo,vamos lá!')



print('Indique a sua raça: ')
print(''' 
[ 1 ] Tiefling
[ 2 ] Anão
[ 3 ] Elfo
''')
opção = int(input('Qual a opção desejada?'))
if opção == 1:
    print('Sabia escolha')
elif opção == 2:
    print('Cresça em seu estado de espirito, melhore')
elif opção == 3:
    print('Serio?')
else:
    print('Opção inválida, digite um valor válido!')
   

print('Opções: ')
print(''' 
[ 1 ] Habilidades
[ 2 ] Stats
[ 3 ] Sobre
[ 4 ] Nenhuma, apenas encerre o programa!
''')

opção2 = int(input('Qual a opção desejada?'))

if opção2 == 1:
    print('hahaha')
elif opção2 == 2:
    print('huhuhu')
elif opção2 == 3:
    print('hihihi')
elif opção2 == 4:
    print('O programa foi encerrado')
    exit()
else:
    print('Opção inválida, digite um valor válido!')
