import os
import modulo as mo

productos={
    "P101":["Cuaderno","Papeleria",2490,True],
    "P102":["Lapiz","Papeleria",590,True],
    "P103":["Botella","Accesorios",6990,False],
    "P104":["Mochila","Accesorios",24990,True]
}

Inventario = {
    "P101":[30,15],
    "P102":[120,50],
    "P103":[0,10],
    "P104":[8,25]
}

while True:
    os.system("cls")
    mo.mostrar_menu()
    opcion = mo.leer_opcion()
    
    match opcion:
        case 1:
            os.system("cls")
            categoria = input("Ingrese categoria: ").strip()
            
            mo.stock_categoria(productos,Inventario)
            
            os.symlinkstem("pause")
        case 2:
            os.system("cls")
            while True:
                try:
                    precio_min = int(input("Ingrese precio minimo: "))
                    precio_max = int(input("Ingrese precio maximo: "))
                    if precio_min < 0 or precio_max < 0:
                        print("Error, Debe ingresar un valor mayor a 0")
                        continue
                    if precio_min > precio_max:
                        print("Error, El precio minimo no puede ser mayor al precio maximo")
                        continue
                    break
                except ValueError:
                    print("Error, Debe ingresar un valor numerico")
            mo.buscar_precio_rango(productos,precio_min,precio_max)
            os.system("pause")
        case 3:
            os.system("cls")
            while True:
                codigo = input("Ingrese codigo del producto: ").strip()
                if not mo.buscar_codigo(codigo, productos):
                    while True:
                        try:
                            nuevo_precio = int(input("Ingrese nuevo precio: "))
                            if not mo.validar_precio(nuevo_precio):
                                print("Error, Debe ingresar un valor mayor a 0")
                                continue
                            break
                        except ValueError:
                            print("Error, Debe ingresar un valor numerico")
                    mo.actualizar_precio(codigo, productos, nuevo_precio)
                    print("Precio actualizado correctamente")
                else:
                    print("Error, El codigo ingresado no existe")
                continue_input = input("Desea actualizar otro producto? (s/n): ").strip().lower()
                if continue_input != 's':
                    break
                os.system("pause")