from tarkvaraarendaja_vastuvõtt import test

# запускаем тестирование
vastuvõetud, eisoobi = test()

# выводим списки принятых и не принятых в консоль
print("Vastuvõetud:")
for nimi, punktid in vastuvõetud:
    print(f"{nimi} ({punktid} punkti)")
print("\nEi sobi:")
for nimi in eisoobi:
    print(nimi)