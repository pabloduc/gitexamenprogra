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