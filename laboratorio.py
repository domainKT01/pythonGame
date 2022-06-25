'''Como ha sabes otras estructuras de datos en Python, se te ha pedido
que mejores el programa que desarrollaste para la tienda La seño.
'''
# solicita los nombres de productos para crear el inventario y retorna una tupla.
# No se sabe cuantos datos ingresara el usuario
def solicitarNombresProd():
    salida = True
    nProductos =[]
    while salida == True: 
       producto = input("ingrese el producto ")
       if producto == "salir":
         salida = False
       else:
         nProductos.append(producto)
    
    return tuple(nProductos)

#función que agrega la tupla de de productos al diccionario como keys
def insertarProductosDic(dicProductos,valores):
    diccionario= {}
    del(diccionario)[nProductos]

#actualiza una cantidad de un producto del diccionario 
def insertarCantidades(dicProductos, nombre, cantidad):
    pass

#elimina un producto del diccionario usando el nombre 
def eliminarProductos(dicProductos, nombre):
    pass

# agrega el nombre de un produto y su cantidad disponible
def agregarNuevoProductos(dicProductos, nombre, cantidad):
    pass

#inicio programa principal
inventarioProd= {}
while(True):
    #inicio programa principal
    print('''Menu
    (1) crear inventario con solo nombres de productos
    (2) actualizar cantidad a un producto
    (3) eliminar producto
    (4) agregar nuevo producto
    (5) salir
    ''')
    opcion=input()

    if opcion==1:
        if len(inventarioProd.keys()) == 0:
            nombreProductos=solicitarNombresProd()
            inventarioProd=insertarProductosDic(dict,nombreProductos)
            print(inventarioProd)
        else:
            print("ya existe")
    elif opcion==2:
        nombre=input("ingrese nombre")
        cant=int(input("ingrese cantidad"))
        inventarioProd=insertarCantidades(inventarioProd,nombre,cant)
        print(inventarioProd)
    elif opcion==3:
        nombre=input("ingrese nombre")
        inventarioProd=eliminarProductos(inventarioProd,nombre)
        print(inventarioProd)
    elif opcion==4:
        nombre = input("ingrese nombre")
        cant = int(input("ingrese cantidad"))
        inventarioProd=agregarNuevoProductos(inventarioProd,nombre,cant)
        print(inventarioProd)