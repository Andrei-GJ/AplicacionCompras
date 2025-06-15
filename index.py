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
    cantidad = int(input("Cuantas productos escogio el cliente: "))
    for a in range (cantidad):
        nameProducto = input("como se llama el producto: ")
        valueProduct = int(input("Ingrese el valor del producto: "))
        amountProduct = int(input("Ingrese la cantidad del producto: "))
        valueTotal = valueProduct * amountProduct
        print("El valor total del producto es: ", valueTotal)
        listclient[i][nameProducto] = valueTotal  
        print("tu cuenta va por un valor de: " + str(sum(listclient[i].values())))
    print("--" * 20)
for a in listclient:
    # print("dsadjsa")
    valueFinal = sum(listclient[a].values())
    # print("dsadjsa")
# print("dsadjsa")
valueFinalTotal =+ valueFinal
# print("dsadjsa")
print(valueFinalTotal)