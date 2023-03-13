import os

def test():
    # считываем вопросы и ответы из файла и сохраняем их в словарь
    kus_vas = {}
    with open('kusimused_vastused.txt', 'r', encoding='utf-8') as file:
        for line in file:
            kus, vas = line.strip().split(':')
            kus_vas[kus] = vas

    # создаем списки для записи данных о прошедших и не прошедших тестирование
    vastuvõetud = []
    eisoobi = []

    # опрашиваем 5 кандидатов и записываем результаты в соответствующие списки
    for i in range(5):
        print(f"Kandidaat nr {i+1}:")
        nimi = input("Mis on Teie nimi? ")
        punktid = 0
        for kus, vas in kus_vas.items():
            vastus = input(kus + " ")
            if vastus.lower() == vas.lower():
                punktid += 1
        if punktid >= 3:
            vastuvõetud.append((nimi, punktid))
        else:
            eisoobi.append(nimi)

    # сортируем список принятых по количеству верных ответов
    vastuvõetud.sort(key=lambda x: x[1], reverse=True)

    # записываем данные о прошедших тестирование в файл
    with open('vastuvõetud.txt', 'w', encoding='utf-8') as file:
        for nimi, punktid in vastuvõetud:
            file.write(f"{nimi}:{punktid}\n")

    # записываем данные о не прошедших тестирование в файл
    with open('eisoobi.txt', 'w', encoding='utf-8') as file:
        for nimi in sorted(eisoobi):
            file.write(nimi + "\n")

    # возвращаем списки принятых и не принятых
    return vastuvõetud, eisoobi
