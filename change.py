def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    print("Ingresar gasto:")
    gasto= float(input())
    print(gasto)
    print("Dinero recibido")
    dinero = int(input())
    print(int(dinero))
    vuelto_pesos = dinero - gasto
    entero = int(vuelto_pesos // 1)
    centavos1 = vuelto_pesos - entero
    centavos = int(centavos1 * 100)
    print("\nVuelto\n")
    print(f"Pesos: \n{entero}")
    print(f"Centavos: \n{centavos}")
