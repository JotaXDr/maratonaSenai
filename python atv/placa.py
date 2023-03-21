import os 
while True:
    X = int(input("Dgitie a altura: "))
    Y = int(input("\nDigite a largura: "))
    M = int(input("\nDigite quantas peças tem: "))

    for x in range (0, M) :
        Xi = int(input("\nQual a largura do cliente: "))
        Yi = int(input("\nQual a altura do cliente: "))
        if Xi > X:
            print("Não da para fazer")
        elif Yi > Y:
            print("Não da para fazer")
        else:
            print("Da para fazer")

    pedal = input("\nDeseja fazer outro pedal?\nR: ").lower

    if pedal == "s" or pedal == "sim" or pedal == "ss":
        break
    os.system("pause")
    os.system("cls")
os.system("cls")