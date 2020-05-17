def eh_par(numero):
    if ( numero % 2 == 0):
        return True
    else:
        return False

controle = ''
a = 0
while controle != 'sim':
    a = int(input('digite um número e eu vou dizer se é par: '))
    if eh_par(a):
        print('é par')
    else:
        print('é impar')

    # considere dizer por exemplo "O número <numero> <é ou não é> par"
    # Fazer isso em uma linha só.

    controle = input('Deseja Sair?')



