from random import randint
from time import sleep

print("Vamos jogar PEDRA, PAPEL, TESOURA????? \nVAMOS LÁ")

n1 = randint(1, 3)

print("-=" * 10)

print("  [ 1 ] PEDRA \n  [ 2 ] PAPEL \n  [ 3 ] TESOURA")

print("-=" * 10)

opc = int(input("Escolha uma opção acima: "))

while opc != 5:

    if opc == 1 and n1 == 1:
        sleep(1)
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO")
        sleep(1)
        print("\033[33mEMPATE\033[m, os dois escolheram PEDRA")

    elif opc == 2 and n1 == 2:
        sleep(1)
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO")
        sleep(1)
        print("\033[33mEMPATE\033[m, os dois escolheram PAPEL")

    elif opc == 3 and n1 == 3:
        sleep(1)
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO")
        sleep(1)
        print("\033[33mEMPATE\033[m, os dois escolheram TESOURA")

    elif opc == 1 and n1 == 3:
        sleep(1)
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO")
        sleep(1)
        print("\033[32mVOCÊ GANHOU\033[m, o PC escolheu TESOURA e você PEDRA")

    elif opc == 2 and n1 == 1:
        sleep(1)
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO")
        sleep(1)
        print("\033[32mVOCÊ GANHOU\033[m, o PC escolheu PEDRA e você PAPEL")

    elif opc == 3 and n1 == 2:
        sleep(1)
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO")
        sleep(1)
        print("\033[32mVOCÊ GANHOU\033[m, o PC escolheu PAPEL e você TESOURA")

    elif opc == 2 and n1 == 3:
        sleep(1)
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO")
        sleep(1)
        print("\033[31mVOCÊ PERDEU\033[m, o PC escolheu TESOURA e você PAPEL")

    elif opc == 3 and n1 == 1:
        sleep(1)
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO")
        sleep(1)
        print("\033[31mVOCÊ PERDEU\033[m, o PC escolheu PEDRA e você TESOURA")

    elif opc == 1 and n1 == 2:
        sleep(1)
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO")
        sleep(1)
        print("\033[31mVOCÊ PERDEU\033[m, o PC escolheu PAPEL e você PEDRA")

    else:
        print("Escolha uma opção valida acima...")

    sleep(2.5)

    n1 = randint(1, 3)

    print("Vamos jogar de novo??")
    print("-=" * 15)
    print("  [ 1 ] PEDRA \n  [ 2 ] PAPEL \n  [ 3 ] TESOURA \n  [ 4 ] Sair do Programa")
    print("-=" * 15)

    opc = int(input("Escolha uma opção acima: "))

    if opc == 4:
        opc += 1

print("Processando...")
sleep(2)
print("Fim do Programa, Volte sempre!!")
