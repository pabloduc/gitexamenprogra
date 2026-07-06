import os

def mostrar_menu():

    print("""
========== MENU PRINCIPAL ==========
1. Stock por categoria
2. Buscar productos por rango de precio
3. Actualizar precio
4. Agregar producto
5. Eliminar producto
6. Mostrar productos
7. Salir
====================================
""")

def leer_opcion():

    while True:

        try:

            opcion=int(input("Ingrese opcion: "))

            if opcion>=1 and opcion<=7:
                return opcion

            print("Error, Debe seleccionar una opcion valida")

        except ValueError:

            print("Error, Debe seleccionar una opcion valida")

def buscar_codigo(codigo, productos):

    for cod in productos:

        if cod.lower()==codigo.lower():
            return True

    return False

def validar_codigo(codigo, productos):

    if len(codigo.strip())==0:
        return False

    if buscar_codigo(codigo, productos):
        return False

    return True

def validar_nombre(nombre):

    if len(nombre.strip())==0:
        return False

    return True

def validar_precio(precio):

    if precio>0:
        return True

    return False

def validar_disponible(opcion):

    if opcion.lower()=="s":
        return True

    if opcion.lower()=="n":
        return True

    return False

def validar_stock(stock):

    if stock>=0:
        return True

    return False

def validar_vendidos(vendidos):

    if vendidos>=0:
        return True

    return False

def agregar_producto(codigo,nombre,categoria,precio,disponible,stock,vendidos,productos,inventario):

    if buscar_codigo(codigo,productos):
        return False

    productos[codigo]=[nombre,categoria,precio,disponible]
    inventario[codigo]=[stock,vendidos]

    return True

def validar_categoria(categoria):

    if len(categoria.strip())==0:
        return False

    return True

def mostrar_productos(productos,inventario):

    if len(productos)==0:
        print("No hay productos registrados")
        return

    for codigo in productos:

        print("--------------------------")
        print(f"CODIGO: {codigo}")
        print(f"Nombre: {productos[codigo][0]}")
        print(f"Categoria: {productos[codigo][1]}")
        print(f"Precio: ${productos[codigo][2]}")
        print(f"Disponible: {productos[codigo][3]}")
        print(f"Stock: {inventario[codigo][0]}")
        print(f"Vendidos: {inventario[codigo][1]}")
        print("--------------------------")

def stock_categoria(categoria,productos,inventario):

    stock_total=0

    for codigo in productos:

        if productos[codigo][1].lower()==categoria.lower():

            stock_total+=inventario[codigo][0]

    print(f"Stock total de la categoria {categoria}: {stock_total}")
    
def buscar_precio(precio_min,precio_max,productos,inventario):

    lista=[]

    for codigo in productos:

        if productos[codigo][2]>=precio_min and productos[codigo][2]<=precio_max:

            if inventario[codigo][0]>0:

                lista.append(f"{productos[codigo][0]}--{codigo}")

    if len(lista)==0:

        print("No existen productos en ese rango")

    else:

        lista.sort()

        for producto in lista:

            print(producto)

def actualizar_precio(codigo,nuevo_precio,productos):

    if buscar_codigo(codigo,productos):

        productos[codigo][2]=nuevo_precio

        return True

    return False

def eliminar_producto(codigo,productos,inventario):

    if buscar_codigo(codigo,productos):

        del productos[codigo]
        del inventario[codigo]

        return True

    return False