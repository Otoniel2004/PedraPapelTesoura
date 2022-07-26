import random
import time

print("-" * 45)
print("Vamos Jogar Pedra, Papel, Tesoura!!!")
print("-" * 45)
print("Digite o Número Correspondente a Sua Escolha\nPedra....[1]\nPapel....[2]"
      "\nTesoura..[3]")
print("-" * 45)
entrada = int(input("Faça Sua Escolha: "))
print("-" * 45)

roll = random.randint(1, 3)
def f():
    print("\033[32mJô\033[m")
    time.sleep(1)
    print("\033[33mKen\033[m")
    time.sleep(1)
    print("\033[31mPo\033[m")
    time.sleep(0.5)


while entrada != 4:
    if entrada == 1 and roll == 1:
        f()
        print("\033[33mEmpate!\033[m Você e o PC Escolheram Pedra")
    elif entrada == 1 and roll == 2:
        f()
        print("\033[31mPerdeu!\033[m Você Escolheu Pedra e o PC Papel")
    elif entrada == 1 and roll == 3:
        f()
        print("\033[32mVenceu!!!\033[m Você Escolheu Pedra e o PC Tesoura")
    elif entrada == 2 and roll == 1:
        f()
        print("\033[32mVenceu!!!\033[m Você Escolheu Papel e o PC Pedra")
    elif entrada == 2 and roll == 2:
        f()
        print("\033[33mEmpate!\033[m Você e o PC Escolheram Papel")
    elif entrada == 2 and roll == 3:
        f()
        print("\033[31mPerdeu!\033[m Você Escolheu Papel e o PC Tesoura")
    elif entrada == 3 and roll == 1:
        f()
        print("\033[31mPerdeu!\033[m Você Escolheu Tesoura e o PC Pedra")
    elif entrada == 3 and roll == 2:
        f()
        print("\033[32mVenceu!!!\033[m Você Escolheu Pedra e o PC Tesoura")
    elif entrada == 3 and roll == 3:
        f()
        print("\033[33mEmpate!\033[m Você e o PC Escolheram Tesoura")
    else:
        print("...")
        time.sleep(1)
        print("Insira Um Valor Válido")
        time.sleep(1)

    print("-" * 45)
    print("Vamos Tentar Novamente!!\nDigite o Número Correspondente a Sua "
          "Escolha\nPedra..........[1]\nPapel..........[2]\nTesoura........[3]"
          "\nSair do Jogo...[4]")
    print("-" * 45)
    entrada = int(input("Faça Sua Escolha: "))
    print("-" * 45)
    roll = random.randint(1, 3)

time.sleep(0.5)
print("Encerrando Jogo, Aguade...")
time.sleep(2)
print("Jogo Encerrado, \033[33mObrigado\033[m Por Jogar!!!\nVolte Sempre\n"
      "\033[32mCreated by\033[m\033[31m Otoniel\033[m")
