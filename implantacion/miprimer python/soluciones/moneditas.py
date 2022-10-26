#pedir monedas de 2,1,0.5,0.2,0.1
monedas2 = int(input("ingrese monedas de 2: "))
monedas1 = int(input("ingrese monedas de 1: "))
monedas50 = int(input("ingrese monedas de 0.5: "))
monedas20 = int(input("ingrese monedas de 0.2: "))
monedas10 = int(input("ingrese monedas de 0.1: "))
#calcular total
total = monedas2 * 2 + monedas1 * 1 + monedas50 * 0.5 + monedas20 * 0.2 + monedas10 * 0.1
#mostrar total
print("el total es: {:.2f}".format(total))