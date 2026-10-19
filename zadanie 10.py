ilosc_studentow = int(input("Podaj ilość studentów: "))
for x in range(0, ilosc_studentow):
    nazwisko = input("Podaj nazwisko: ")
    punkty = int(input('Podaj liczbę punktów: '))
    if punkty < 0:
        ocena = 0
    elif punkty < 50:
        ocena = 2
    elif punkty < 60:
        ocena = 3
    elif punkty < 70:
        ocena = 3.5
    elif punkty < 80:
        ocena = 4
    elif punkty < 90:
        ocena = 4.5
    elif punkty <= 100:
        ocena = 5
    else:
        ocena = 0

    if ocena > 0:
        print(nazwisko + 'posiada ' + str(punkty) + ' punktów i ma ocenę: ' + str(ocena))
    else:
        print('Nieprawidłowa liczba punktów')


    
print('liczba studentów którzy zdali: ' + str(len([x for x in range(1, ilosc_studentow) if ocena > 3])))
    


