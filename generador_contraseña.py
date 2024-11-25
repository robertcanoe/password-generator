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
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special_characters:
        characters += string.punctuation

    if not characters:
        return "Error: Debes seleccionar al menos un tipo de caracteres."

    return ''.join(random.choice(characters) for _ in range(length))

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

def main():
    """
    Función principal del programa.
    """
    print("=== Generador de Contraseñas Aleatorias ===")
    try:
        length = int(input("Introduce la longitud de la contraseña (número entero positivo): "))
        if length <= 0:
            raise ValueError("La longitud debe ser un número positivo.")
    except ValueError as e:
        print(f"Entrada inválida: {e}")
        return

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
