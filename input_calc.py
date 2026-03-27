def rectangle():
     """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    
    base= int(input())
    altura= int(input())

    area= base * altura
    perimetro= base + base + altura + altura
    print(f"Base: {base}")
    print(f"Altura: {altura}")
    print(f"Area: {area}")
    print(f"Perimetro: {perimetro}")

