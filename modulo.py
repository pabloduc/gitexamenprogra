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
            opcion = int(input("Ingrese opcion: "))
            if opcion >= 1 and opcion <= 7:
                return opcion
            print("Error, Debe seleccionar una opcion valida")
        except ValueError:
            print("Error, Debe seleccionar una opcion valida")

def buscar_codigo(codigo, productos):
    for cod in productos:
        if cod.lower() == codigo.lower():
            return True
    return False

def validar_codigo(codigo, productos):
    if len(codigo.strip()) == 0:
        return False
    if buscar_codigo(codigo, productos):
        return False
    return True

def validar_nombre(nombre):
    if len(nombre.strip()) == 0:
        return False
    return True

def validar_precio(precio):
    if precio>0:
        return True
    return False

def validar_disponible(disponible):
    if disponible.lower() == "si" or disponible.lower() == "no":
        return True
    return False

def validar_stock(stock):
    if stock >= 0:
        return True
    return False

def validar_vendidos(vendidos):
    if vendidos >= 0:
        return True
    return False

def agregar_producto(productos):
    codigo = input("Ingrese el codigo del producto: ")
    if not validar_codigo(codigo, productos):
        print("Error, el codigo ya existe o es invalido")
        return

    nombre = input("Ingrese el nombre del producto: ")
    if not validar_nombre(nombre):
        print("Error, el nombre es invalido")
        return

    try:
        precio = float(input("Ingrese el precio del producto: "))
        if not validar_precio(precio):
            print("Error, el precio debe ser mayor a 0")
            return
    except ValueError:
        print("Error, el precio debe ser un numero")
        return

    disponible = input("Ingrese si el producto esta disponible (si/no): ")
    if not validar_disponible(disponible):
        print("Error, debe ingresar 'si' o 'no'")
        return

    try:
        stock = int(input("Ingrese el stock del producto: "))
        if not validar_stock(stock):
            print("Error, el stock no puede ser negativo")
            return
    except ValueError:
        print("Error, el stock debe ser un numero entero")
        return

    try:
        vendidos = int(input("Ingrese la cantidad de productos vendidos: "))
        if not validar_vendidos(vendidos):
            print("Error, la cantidad de vendidos no puede ser negativa")
            return
    except ValueError:
        print("Error, la cantidad de vendidos debe ser un numero entero")
        return

    productos[codigo] = {
        "nombre": nombre,
        "precio": precio,
        "disponible": disponible.lower(),
        "stock": stock,
        "vendidos": vendidos
    }
    print(f"Producto {nombre} agregado exitosamente.")
    
def validar_categoria(categoria):
    if len(categoria.strip()) == 0:
        return False
    return True

def mostrar_productos(productos):
    if not productos:
        print("No hay productos para mostrar.")
        return
    for codigo, info in productos.items():
        print(f"Codigo: {codigo}, Nombre: {info['nombre']}, Precio: {info['precio']}, Disponible: {info['disponible']}, Stock: {info['stock']}, Vendidos: {info['vendidos']}")
        
def stock_categoria(categoria, productos):
    stock_total = 0
    for info in productos.values():
        if info['categoria'].lower() == categoria.lower():
            stock_total += info['stock']
    print(f"Stock total de la categoria {categoria}: {stock_total}")
    
def buscar_precio_rango(productos, precio_min, precio_max):
    encontrados = []
    for codigo, info in productos.items():
        if precio_min <= info['precio'] <= precio_max:
            encontrados.append((codigo, info))
    return encontrados

def actualizar_precio(codigo, nuevo_precio, productos):
    if codigo in productos:
        productos[codigo]['precio'] = nuevo_precio
        print(f"Precio del producto {codigo} actualizado a {nuevo_precio}.")
    else:
        print("Error, el codigo no existe.")

def eliminar_producto(codigo, productos):
    if codigo in productos:
        del productos[codigo]
        print(f"Producto {codigo} eliminado exitosamente.")
    else:
        print("Error, el codigo no existe.")