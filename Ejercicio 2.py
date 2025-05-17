#nos piden hacer una tiendita con un listado de productos, donde, dependiendo del monto final nos puede dar un descuento o no.
#adicional a esto se agrego la opción de poder sumar o restar productos con un menú.

#Se definen las variables a utilizar, en este caso los precios de los artículos.
Arroz = 450
Fideos = 330
Atún = 650
Galleta = 180
Jugo = 320
agregar_quitar = 0
articulo = 0
precio_final = 0

#Acá se hace una pequeña presentación y se muestran los precios.
print("\n--Bienvenido a nuestra tiendita familiar--\n")
print(f"Nuestros artículos son los siguienes:\n\n1.- 'Arroz' con un precio de     ${Arroz}\n2.- 'Fideos' con un precio de    ${Fideos}\n3.- 'Atún' con un precio de      ${Atún}")
print(f"4.- 'Galleta' con un precio de   ${Galleta}\n5.- 'Jugo' con un precio de      ${Jugo}\n")
print("¿Qué desea hacer?\n1.- Agregar artículos\n2.- Quitar artículos\n3.- Salir\n")


#Acá comenzamos a realizar el while para generar el bucle de suma y resta.
#Dentro de las opciones se limita la utilización de las opciones a solo las disponibles.

while agregar_quitar !=3:
    
    agregar_quitar = int(input("Ingrese Opción: "))

    if agregar_quitar >0 and agregar_quitar < 4:
      
        if agregar_quitar == 1: #Sumar o Agregar
                
            articulo = int(input("Ingrese el artículo que desea Agregar: "))
            if articulo == 1:
                precio_final = precio_final + Arroz
                print("")
                print(f"Sumando 'Arroz'\nSu compra tiene un Valor de ${precio_final}\n")
                
            elif articulo == 2:
                precio_final = precio_final + Fideos
                print("")
                print(f"Sumando 'Fideos'\nSu compra tiene un Valor de ${precio_final}\n")
                
            elif articulo == 3:
                precio_final = precio_final + Atún
                print("")
                print(f"Sumando 'Atún'\nSu compra tiene un Valor de ${precio_final}\n")
                
            elif articulo == 4:
                precio_final = precio_final + Galleta
                print("")
                print(f"Sumando 'Galleta'\nSu compra tiene un Valor de ${precio_final}\n")
                
            elif articulo == 5:
                precio_final = precio_final + Jugo
                print("")
                print(f"Sumando 'Jugo'\nSu compra tiene un Valor de ${precio_final}\n")
                
            elif articulo < 1:
                print("")
                print("Ingrese un artículo de la lista\n")
                
            elif articulo > 5:
                print("")
                print("Ingrese un artículo de la lista\n")
        

        if agregar_quitar == 2: #Restar o Quitar

            articulo = int(input("Ingrese el artículo que desea Quitar: "))
            
            if articulo == 1:
                comprobacion = precio_final-Arroz
                if comprobacion < 0:
                    precio_final = 0
                    print("")
                    print(f"Restando 'Arroz'\nSu compra tiene un Valor de ${precio_final}\n")
                else:
                    precio_final = precio_final - Arroz
                    print("")
                    print(f"Restando 'Arroz'\nSu compra tiene un Valor de ${precio_final}\n")
                    
            elif articulo == 2:
                comprobacion = precio_final-Fideos
                if comprobacion < 0:
                    precio_final = 0
                    print("")
                    print(f"Restando 'Fideos'\nSu compra tiene un Valor de ${precio_final}\n")
                    
                else:
                    precio_final = precio_final - Fideos
                    print("")
                    print(f"Restando 'Fideos'\nSu compra tiene un Valor de ${precio_final}\n")
                    
            elif articulo == 3:
                comprobacion = precio_final-Atún
                if comprobacion < 0:
                    precio_final = 0
                    print("")
                    print(f"Restando 'Atun'\nSu compra tiene un Valor de ${precio_final}\n")
                    
                else:
                    precio_final = precio_final - Atún
                    print("")
                    print(f"Restando 'Atún'\nSu compra tiene un Valor de ${precio_final}\n")
                    
            elif articulo == 4:
                comprobacion = precio_final-Galleta
                if comprobacion < 0:
                    precio_final = 0
                    print("")
                    print(f"Restando 'Galleta'\nSu compra tiene un Valor de ${precio_final}\n")
                    
                else:
                    precio_final = precio_final - Galleta
                    print("")
                    print(f"Restando 'Galleta'\nSu compra tiene un Valor de ${precio_final}\n")
                    
            elif articulo == 5:
                comprobacion = precio_final-Jugo
                if comprobacion < 0:
                    precio_final = 0
                    print("")
                    print(f"Restando 'Jugo'\nSu compra tiene un Valor de ${precio_final}\n")
                    
                else:
                    precio_final = precio_final - Jugo
                    print("")
                    print(f"Restando 'Jugo'\nSu compra tiene un Valor de ${precio_final}\n")
                    
            elif articulo < 0:
                print("")
                print("Ingrese un artículo de la lista\n")
                
            elif articulo > 6:
                print("")
                print("Ingrese un artículo de la lista\n")
                
    else:
        print("Por favor ingrese una opción válida")            



#aquí se determina el precio final aplicando el descuento.

#mayor a 5000 30% 
#menor a 5000 y mayor a 3000 20% 
#menor a 3000 y mayor a 1000 10%
#menor a 1000 nada


print("\nSaliendo y Calculando Precio Final de su Compra\n")

if precio_final >= 5000:
        precio_total = precio_final - precio_final*0.3
        print(f"Usted tiene un descuento del 30% y el Valor final de su compra es de: ${precio_total}\n")
elif precio_final < 5000 and precio_final >= 3000:
        precio_total = precio_final - precio_final*0.2
        print(f"Usted tiene un descuento del 20% y el Valor final de su compra es de: ${precio_total}\n")
elif precio_final < 3000 and precio_final >=1000:
        precio_total = precio_final - precio_final*0.1
        print(f"Usted tiene un descuento del 10% y el Valor final de su compra es de: ${precio_total}\n")
elif precio_final <1000:
        precio_total = precio_final
        print(f"Usted no tiene descuento y el Valor final de su compra es de: ${precio_total}\n")
    