def generowanie_poziomej_piramidy():
    while True:
        # Pobranie wysokości piramidy od użytkownika lub opcji zakończenia
        dane_podstawowe = input("Napisz jaka wysoka ma być Twoja piramida lub jeśli masz dość piramid - wybierz 'q': ")
        if dane_podstawowe.lower() == 'q':
            print("Nie zostaniesz Tutanchamonem.")
            break

        try:
            wysokosc = int(dane_podstawowe)
            if wysokosc <= 0:
                raise ValueError("Wysokość piramidy nie może być ujemna.")
        except ValueError as e:
            print("Błąd:", e)
            continue
        
        for i in range(1, wysokosc + 1):
            print('#' * i)
        
        for i in range(wysokosc - 1, 0, -1):
            print('#' * i)

generowanie_poziomej_piramidy()

