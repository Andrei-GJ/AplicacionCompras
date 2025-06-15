nombresclientes = []
listclient = {}
print("Compras")
cantidad_clientes = int(input("Ingrese la cantidad de clientes: "))


for i in range(cantidad_clientes):
    listclient[i] = {}
    print("Cliente", i + 1)
    
    nombre = input("Ingrese el nombre del cliente: ")
    print("Un gusto atenderlo ", nombre)
    nombresclientes.append(nombre)
    
    cantidad = int(input("Cuantas productos escogio el cliente: "))
    for a in range (cantidad):
        nameProducto = input("como se llama el producto: ")
        valueProduct = int(input("Ingrese el valor del producto: "))
        listclient[i][nameProducto] = valueProduct
    print(listclient[i])
    print(listclient)