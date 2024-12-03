import re


def day3function(file_content):
    """
    Funkcija pogleda vsebino datoteke in vrne dva rezultata:
    - part_1: Skupni seštevek vseh rezultatov mul(x, y).
    - part_2: Skupni seštevek rezultatov mul(x, y) samo, ko je omogočeno.

    :param file_content: Vsebina datoteke, ki vsebuje ukaze za obdelavo.
    :return: Vrednost (part_1, part_2)
    """

    # Inicializiramo spremenljivke
    part_1 = 0
    part_2 = 0

    # Spremenljivka za sledenje
    is_enabled = True

    # Zanka skozi vsebino datoteke
    for i in range(len(file_content)):

        # Preverimo, če se začne z 'do()'
        if file_content[i:].startswith('do()'):
            is_enabled = True

        # Preverimo, če se začne z 'don't()'
        elif file_content[i:].startswith("don't()"):
            is_enabled = False

        # Preverimo, ali je trenutni del besedila ukaz 'mul(x, y)'
        mul_instruction = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', file_content[i:])

        if mul_instruction:
            # Pridobimo vrednosti x in y iz ukaza 'mul(x, y)'
            x = int(mul_instruction.group(1))
            y = int(mul_instruction.group(2))

            # Izračunamo produkt x * y
            result = x * y

            # Dodamo rezultat k part_1
            part_1 += result

            # Če so naloge omogočene, dodamo tudi k part_2
            if is_enabled:
                part_2 += result

    return part_1, part_2


# Glavni del, ki prebere datoteko in pokliče funkcijo
if __name__ == "__main__":
    # Branje datoteke 'day3input.txt'
    with open('day3input.txt') as f:
        file_content = f.read().strip()  # Preberi vsebino datoteke

    # Obdelava vsebine datoteke
    part_1, part_2 = day3function(file_content)

    # Izpis rezultatov
    print(f"Rezultat za del 1 (part_1): {part_1}")
    print(f"Rezultat za del 2 (part_2): {part_2}")
