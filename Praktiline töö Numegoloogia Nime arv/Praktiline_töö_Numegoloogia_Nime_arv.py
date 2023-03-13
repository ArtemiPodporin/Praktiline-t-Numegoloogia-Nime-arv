from name_number import calculate_name_number

name = input('Sisestage oma nimi: ')
name_number = calculate_name_number(name)
print(f'Nime "{name}" nimenumber on {name_number}.')