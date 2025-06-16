nombresclientes = []
listclient = {}
valueFinalTotal = 0
cantidad_clientes = int(input("Ingrese la cantidad de clientes: "))
print("--" * 20)
for i in range(cantidad_clientes):
    listclient[i] = {}
    nombre = input("Ingrese el nombre del cliente: ")
    print("Un gusto atenderlo ", nombre)
    nombresclientes.append(nombre)
    print("--" * 20)
    cantidad = int(input("cuantos productos escogio el cliente: "))
    for a in range (cantidad):
        print(" " )
        nameProducto = input("como se llama el producto: ")
        print(" " )
        valueProduct = int(input("Ingrese el valor del producto: "))
        print(" " )
        amountProduct = int(input("Ingrese la cantidad del producto: "))
        print(" " )
        valueTotal = valueProduct * amountProduct
        print("El valor total del producto es: ", valueTotal)
        print(" " )
        listclient[i][nameProducto] = valueTotal  
        print("*" * 10)
        if(a + 1 == cantidad):
            print(" " )
            print("tu cuenta total es de: " + str(sum(listclient[i].values())))
            print(" " )
        else:
            print(" " )
            print("tu cuenta va por un valor de: " + str(sum(listclient[i].values())))
            print(" " )
        print("*" * 10)
    print("--" * 20)

for b in range(len(listclient)):
    valueFinal = sum(listclient[b].values())
    valueFinalTotal += valueFinal
    if b + 1 == len(listclient):
        print("Total de compra de todos los clientes " + str(valueFinalTotal))
        print(" " )

if len(listclient) == 1:
    print("El cliente con la mayor compra es " + nombresclientes[0])
else:
    MaxValue = 0
    for e in range(len(listclient)):
        Valueclient = sum(listclient[e].values())
        if MaxValue < Valueclient:
            MaxValue = Valueclient
            positioncliente = e
    print("El cliente " + nombresclientes[positioncliente] + " con la mayor compra es de: " + str(MaxValue))
