#RECEBENDO UM NÚMERO

n = int(input('DIGITE UM NÚMERO: '))

#CALCULE O RESTO DA DIVISÃO POR 2

resto = n % 2

#VERIFICANDO SE É ÍMPAR OU PAR

if (resto == 0):

    print("\nO NÚMERO {} É PAR ".format(n))
else:
    print("\nO NÚMERO {} É ÍMPAR".format(n))
