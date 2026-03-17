def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    print("Ingresar gasto:")
    gasto= float(input(""))
    print(gasto)
    print("Dinero_recibido")
    dinero = int(input(""))
    print(int(dinero))
    print()
    print("Vuelto")
    print()
    print("Pesos:")
    vuelto_pesos = dinero - gasto
    entero= (int(vuelto_pesos))
    print(entero)
    print("Centavos:")
    centavos= gasto - int(gasto)
    print(100 - (centavos * 100))
