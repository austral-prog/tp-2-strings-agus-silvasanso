def slice_simple():
    """Dado el texto 'Awesome', imprime distintos substrings
    usando slicing y lower().
    """
    texto = "Awesome"
    texto_minusculas = texto.lower()
    print(texto_minusculas[:3])
    print(texto[2:5])
    print(texto_minusculas)
