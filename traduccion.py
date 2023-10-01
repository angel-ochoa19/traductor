def agregar_traduccion(palabra_origen, palabra_destino):
    """Agrega una nueva traducción al diccionario."""
    with open("EN-ES.txt", "a") as archivo:
        archivo.write(f"{palabra_origen}={palabra_destino}\n")

def traducir(palabra):
    """Traduce una palabra del idioma origen al idioma destino si está disponible."""
    with open("EN-ES.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            partes = linea.strip().split("=")
            if len(partes) == 2:
                palabra_dicc, palabra_destino = partes
                if palabra_dicc == palabra and palabra_destino != "":
                    return palabra_destino
    return None

while True:
    print("1. Agregar nueva traducción")
    print("2. Traducir")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        palabra_origen = input("Palabra en el idioma de origen: ")
        palabra_destino = input("Palabra en el idioma de destino: ")
        agregar_traduccion(palabra_origen, palabra_destino)
    elif opcion == "2":
        palabra = input("Palabra a traducir: ")
        traduccion = traducir(palabra)
        if traduccion is not None:
            print(f"Traducción: {traduccion}")
        else:
            print("No se encontró una traducción para esa palabra.")
    elif opcion == "3":
        break
    else:
        print("Opción no válida.")
