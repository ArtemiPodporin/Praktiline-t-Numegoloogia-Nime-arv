def calculate_name_number(name):

    # Определение алфавита по первой букве имени
    first_letter = name[0].upper()
    if first_letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif first_letter in ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']:
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    else:
        raise ValueError('tundmatu tähestik')

    # Расчет числа имени
    name_number = 0
    for letter in name.upper():
        if letter in alphabet:
            number = alphabet.index(letter) % 9 + 1
            name_number += number
    while name_number > 9:
        name_number = sum(map(int, str(name_number)))
    return name_number
