# Napisz funkcję (lub program), który wyświetli poprawnie zdanie "Ala ma x kotów" w zależności od ilości kotów. To jest: Ala ma 1 kota, Ala ma 2 koty, Ala ma 10 kotów

def koty(ilosc):
    while ilosc == int(ilosc):
        if ilosc < 0:
            print("Wpisz poprawną liczbę kotów")
        if ilosc == 0:
            print("Ala nie ma kota.")
        if ilosc == 1:
            print("Ala ma jednego kota")
        if 5 > ilosc >= 2:
            print(f"Ala ma {ilosc} koty.")
        if ilosc >=5:
            print(f"Ala ma {ilosc} kotów.")
        break
    else:
        print("Wpisz poprawną ilość kotów.")




koty(0)