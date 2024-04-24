class Person:
    def __init__(self, namn, ålder, kön=None):
        self.namn = namn
        self.ålder = ålder
        self.kön = kön

# Lista för att hålla passagerare
passagerare_lista = []

def plocka_upp():
    if len(passagerare_lista) >= 25:
        print("Bussen är full. Kan inte lägga till fler passagerare.")
        return
    namn = input("Ange passagerarens namn: ")
    ålder = int(input("Ange passagerarens ålder: "))
    kön = input("Ange passagerarens kön: ")
    passager = Person(namn, ålder, kön)
    passagerare_lista.append(passager)
    print("Passagerare tillagd!")

def gå_av():
    if len(passagerare_lista) == 0:
        print("Det finns inga passagerare att ta bort.")
        return
    namn = input("Ange passagerarens namn som ska gå av: ")
    for passager in passagerare_lista:
        if passager.namn.lower() == namn.lower():
            passagerare_lista.remove(passager)
            print(f"{namn} har gått av.")
            return
    print(f"{namn} finns inte på bussen.")

def lista_passagerare():
    print("Passagerare på bussen:")
    for idx, passager in enumerate(passagerare_lista, start=1):
        print(f"{idx}. Namn: {passager.namn}, Ålder: {passager.ålder}, Kön: {passager.kön}")

def beräkna_sammanlagd_ålder():
    sammanlagd_ålder = sum(passager.ålder for passager in passagerare_lista)
    print(f"Den sammanlagda åldern av alla passagerare är: {sammanlagd_ålder}")

def beräkna_medelålder():
    medelålder = sum(passager.ålder for passager in passagerare_lista) / len(passagerare_lista)
    print(f"Medelåldern av passagerarna är: {medelålder:.2f}")

# Övriga funktioner kan implementeras på liknande sätt

def main():
    while True:
        print("\nVälj ett alternativ:")
        print("1. Plocka upp passagerare")
        print("2. Låt passagerare gå av")
        print("3. Lista alla passagerare")
        print("4. Beräkna sammanlagd ålder")
        print("5. Beräkna medelålder")
        print("6. Avsluta programmet")

        val = input("Ange ditt val: ")

        if val == "1":
            plocka_upp()
        elif val == "2":
            gå_av()
        elif val == "3":
            lista_passagerare()
        elif val == "4":
            beräkna_sammanlagd_ålder()
        elif val == "5":
            beräkna_medelålder()
        elif val == "6":
            print("Programmet avslutas.")
            break
        else:
            print("Ogiltigt val. Vänligen försök igen.")

if __name__ == "__main__":
    main()

