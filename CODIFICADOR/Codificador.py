# ZURAN - Conversor secreto personalizado

# Definimos el alfabeto estándar (mayúsculas y espacio)
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

# Definimos un conjunto de símbolos especiales (mismo número que el alfabeto)
simbolos = "⌁♞★⚙⚡☣☯✦☢♻⚔⇄☄⇨✰✘☌☭⟁⌬⌇☈✎✂☍⏃ "

# Creamos un diccionario para codificar: cada letra se asocia con un símbolo
codificador = dict(zip(alfabeto, simbolos))

# Creamos el diccionario inverso para decodificar: de símbolo a letra
decodificador = dict(zip(simbolos, alfabeto))

# Función para codificar un mensaje en lenguaje secreto
def codificar(texto):
    resultado = ""
    for char in texto.upper():  # Convertimos a mayúsculas para que coincida con el alfabeto
        if char in codificador:
            resultado += codificador[char]  # Reemplaza por el símbolo correspondiente
        else:
            resultado += char  # Si el caracter no está (ej: números o símbolos), lo deja igual
    return resultado

# Función para decodificar un mensaje secreto
def decodificar(texto):
    resultado = ""
    for char in texto:
        if char in decodificador:
            resultado += decodificador[char]  # Reemplaza por la letra correspondiente
        else:
            # Si el símbolo no existe en el diccionario, lanza un error
            return f"❌ Error: símbolo desconocido '{char}' no está en el lenguaje secreto."
    return resultado

# Menú principal del programa
def main():
    print("1. Codificar mensaje")
    print("2. Decodificar mensaje")
    modo = input("Elige una opción (1 o 2): ")
    
    if modo == "1":
        mensaje = input("Escribe tu mensaje a codificar: ")
        resultado = codificar(mensaje)
        print("\n🔐 Mensaje codificado:\n", resultado)
    elif modo == "2":
        mensaje = input("Escribe tu mensaje codificado: ")
        resultado = decodificar(mensaje)
        print("\n📖 Mensaje decodificado:\n", resultado)
    else:
        print("Opción inválida")

# Ejecuta el programa solo si se corre directamente (no si se importa)
if __name__ == "__main__":
    main()
