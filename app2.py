import os
import modulo as mo

productos = {
    "P101":["Cuaderno","Papeleria",2490,True],
    "P102":["Lapiz","Papeleria",590,True],
    "P103":["Botella","Accesorios",6990,False],
    "P104":["Mochila","Accesorios",24990,True]
}


inventario = {
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
            categoria=input("Ingrese categoria: ").strip()

            mo.stock_categoria(categoria,productos,inventario)
            
            os.system("pause")

        case 2:
            os.system("cls")
            while True:

                try:

                    precio_min=int(input("Ingrese precio minimo: "))

                    break

                except ValueError:

                    print("Debe ingresar un numero")

            while True:

                try:

                    precio_max=int(input("Ingrese precio maximo: "))

                    break

                except ValueError:

                    print("Debe ingresar un numero")

            mo.buscar_precio(precio_min,precio_max,productos,inventario)
            os.system("pause")

        case 3:
            
            os.system("cls")
            while True:

                codigo=input("Ingrese codigo del producto: ").strip().upper()

                if mo.buscar_codigo(codigo,productos):

                    while True:

                        try:

                            precio=int(input("Ingrese nuevo precio: "))

                            if mo.validar_precio(precio):
                                break

                            print("Precio invalido")

                        except ValueError:

                            print("Debe ingresar un numero")

                    mo.actualizar_precio(codigo,precio,productos)

                    print("Precio actualizado correctamente")

                else:

                    print("Codigo inexistente")

                continuar=input("Desea actualizar otro precio? (s/n): ").strip().lower()

                if continuar!="s":
                    break
            os.system("pause")

        case 4:
            
            os.system("cls")
            while True:
                codigo=input("Ingrese codigo: ").strip().upper()

                if mo.validar_codigo(codigo,productos):
                    break

                print("Codigo invalido")

            while True:
                nombre=input("Ingrese nombre: ").strip()

                if mo.validar_nombre(nombre):
                    break

                print("Nombre invalido")

            while True:
                categoria=input("Ingrese categoria: ").strip()

                if mo.validar_categoria(categoria):
                    break

                print("Categoria invalida")

            while True:

                try:

                    precio=int(input("Ingrese precio: "))

                    if mo.validar_precio(precio):
                        break

                    print("Precio invalido")

                except ValueError:

                    print("Debe ingresar un numero")

            while True:

                disponible=input("Disponible (s/n): ").strip().lower()

                if mo.validar_disponible(disponible):

                    if disponible=="s":
                        disponible=True
                    else:
                        disponible=False

                    break

                print("Debe ingresar s o n")

            while True:

                try:

                    stock=int(input("Ingrese stock: "))

                    if mo.validar_stock(stock):
                        break

                    print("Stock invalido")

                except ValueError:

                    print("Debe ingresar un numero")

            while True:

                try:

                    vendidos=int(input("Ingrese vendidos: "))

                    if mo.validar_vendidos(vendidos):
                        break

                    print("Cantidad invalida")

                except ValueError:

                    print("Debe ingresar un numero")

            if mo.agregar_producto(codigo,nombre,categoria,precio,disponible,stock,vendidos,productos,inventario):

                print("Producto agregado correctamente")

            else:

                print("No fue posible agregar el producto")

        
            os.system("pause")

        case 5:
            os.system("cls")
            codigo=input("Ingrese codigo del producto a eliminar: ").strip().upper()

            if mo.eliminar_producto(codigo,productos,inventario):

                print("Producto eliminado correctamente")

            else:

                print("Codigo inexistente")
            
            os.system("pause")

        case 6:
            os.system("cls")
                    

            mo.mostrar_productos(productos,inventario)

            
            os.system("pause")

        case 7:
            os.system("cls")
            
            break
        