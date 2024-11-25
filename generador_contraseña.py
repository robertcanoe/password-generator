"""
Generador de Contraseñas Aleatorias
-----------------------------------
Este programa genera contraseñas seguras y personalizables según las preferencias del usuario.
Permite seleccionar la longitud de la contraseña y el tipo de caracteres que incluir
(mayúsculas, minúsculas, números y caracteres especiales). Diseñado para reforzar
habilidades en Python y conceptos básicos de ciberseguridad.

Autor: Roberto Cano Estévez

Fecha: 23/11/2024
"""

import random
import string

def generate_password(length, uppercase=True, lowercase=True, numbers=True, special_characters=True):
    """
    Genera una contraseña aleatoria basada en los parámetros dados.
    
    :param length: Longitud de la contraseña.
    :param uppercase: Incluir letras mayúsculas.
    :param lowercase: Incluir letras minúsculas.
    :param numbers: Incluir números.
    :param special_characters: Incluir caracteres especiales.
    :return: Una contraseña generada o un mensaje de error.
    """
    # Garantizar al menos un carácter de cada tipo seleccionado
    characters = []
    if uppercase:
        characters.append(random.choice(string.ascii_uppercase))
    if lowercase:
        characters.append(random.choice(string.ascii_lowercase))
    if numbers:
        characters.append(random.choice(string.digits))
    if special_characters:
        characters.append(random.choice(string.punctuation))

    if not characters:
        return "Error: Debes seleccionar al menos un tipo de caracteres."

    # Generar el resto de la contraseña
    all_characters = ""
    if uppercase:
        all_characters += string.ascii_uppercase
    if lowercase:
        all_characters += string.ascii_lowercase
    if numbers:
        all_characters += string.digits
    if special_characters:
        all_characters += string.punctuation

    characters += random.choices(all_characters, k=length - len(characters))
    random.shuffle(characters)
    return ''.join(characters)

def get_user_input(prompt, valid_responses=("s", "n")):
    """
    Solicita una entrada al usuario y la valida.
    
    :param prompt: Mensaje mostrado al usuario.
    :param valid_responses: Respuestas válidas.
    :return: Verdadero si la respuesta es afirmativa, Falso en caso contrario.
    """
    while True:
        response = input(prompt).strip().lower()
        if response in valid_responses:
            return response == "s"
        print("Por favor, responde con 's' o 'n'.")

def get_password_length():
    """
    Solicita al usuario la longitud de la contraseña y la valida.
    
    :return: Longitud de la contraseña.
    """
    while True:
        try:
            length = int(input("Introduce la longitud de la contraseña (número entero positivo): "))
            if length > 0:
                return length
            else:
                print("La longitud debe ser un número positivo.")
        except ValueError:
            print("Por favor, introduce un número válido.")

def main():
    """
    Función principal del programa.
    """
    print("=== Generador de Contraseñas Aleatorias ===")
    
    # Solicitar longitud de la contraseña
    length = get_password_length()

    # Opciones del usuario
    uppercase = get_user_input("¿Incluir mayúsculas? (s/n): ")
    lowercase = get_user_input("¿Incluir minúsculas? (s/n): ")
    numbers = get_user_input("¿Incluir números? (s/n): ")
    special_characters = get_user_input("¿Incluir caracteres especiales? (s/n): ")

    # Generar contraseña
    password = generate_password(length, uppercase, lowercase, numbers, special_characters)
    print(f"\nContraseña generada: {password}")

if __name__ == "__main__":
    main()
