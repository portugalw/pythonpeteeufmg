idade = 10
nome = input("Digite seu nome: ")

#argumentos
print("Sua idade é:" , idade, '\nO nome é ', nome, sep='---', end=';') #convert int para string, com +nao converte

#Tupla
print('Nome: %s, numero: %s' %(nome, idade))

#.format
print('Nome: {}, numero: {}'.format(nome, idade))

#concat
print('Sua idade é:' + str(idade) + '\nO nome é ' + nome) 