import random
import string

def generate_password(length, uppercase=True, lowercase=True, numbers=True, special_characters=True):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special_characters:
        characters += string.punctuation

    if len(characters) == 0:
        return "Debes seleccionar al menos un tipo de caracteres."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Generador de Contraseñas Aleatorias")

    length = int(input("Introduce la longitud de la contraseña: "))
    uppercase = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
    lowercase = input("¿Incluir minúsculas? (s/n): ").lower() == 's'
    numbers = input("¿Incluir números? (s/n): ").lower() == 's'
    special_characters = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'

    password = generate_password(length, uppercase, lowercase, numbers, special_characters)

    print(f"\nContraseña generada: {password}")

if __name__ == "__main__":
    main()
