
from datetime import date
from models import Session, Duration


'''
Perioden är 1.1.2026–31.12.2035 = 10 år × 12 månader = 120 element
eg. måste skapa en lista med 120 separata MonthList-instanser
'''

from linked_list import MonthList

months = [MonthList() for _ in range(120)]

# function som räknar ut vilket index (0–119) en viss månad/år ska ha i months listan
def month_index(year, month):
    return (year - 2026) * 12 + (month - 1)


'''
Text-baserad meny:
- Visa alla pass för en viss dag
- Lägga till pass (ett i taget)
- Ta bort pass (ett i taget)

'''

def show_menu():
    print("\n","Vänligen välj en funktion nedan:")
    print("1. Visa pass för en dag")
    print("2. Lägg till pass")
    print("3. Ta bort pass")
    print("4. Avsluta")

# alternativ 2.
def add_session():
    # användar inputs
    description = input("Beskrivning: ")
    year = int(input("År: "))
    month = int(input("Månad: "))
    day = int(input("Dag: "))
    distance = float(input("Sträcka (km): "))
    hours = int(input("Timmar: "))
    minutes = int(input("Minuter: "))
    seconds = int(input("Sekunder: "))

    # dataclasser lagrade i variabler
    session_date = date(year, month, day)
    duration = Duration(hours, minutes, seconds)
    session = Session(description, session_date, distance, duration)

    # tar den nya sessionen och placerar den på rätt plats i months listan med 120 element
    idx = month_index(year, month)
    months[idx].insert(session)
    print("Pass tillagt!")

# alternativ 1.
def view_day():
    #använda inputs
    print("\n", "Välj ett pass att visa för perioden 1.1.2026–31.12.2035")
    year = int(input("År: "))
    month = int(input("Månad: "))
    day = int(input("Dag: "))

    idx = month_index(year, month)
    found = False # variablel som ändras endast när den är hittad
    for session in months[idx]:
        if session.date == date(year, month, day):
            print(session)
            found = True
    if not found:
        print("Inga pass den dagen.")

# alternativ 3. 
def remove_session():
    #användar inputs: 
    year = int(input("År: "))
    month = int(input("Månad: "))
    day = int(input("Dag: "))

    idx = month_index(year, month)
    target_date = date(year, month, day)

    matches = [s for s in months[idx] if s.date == target_date] # byggs en lista  med alla sessioner just den dagen

    if not matches:
        print("Inga pass den dagen.")
        return

    # Visar hittade passen numrerade, låter användaren välja vilket
    print("Pass den dagen:") 
    for i, s in enumerate(matches):
        print(f"{i}: {s.description} - {s.distance}km")

    choice = int(input("Vilket pass vill du ta bort (nummer)? "))
    if 0 <= choice < len(matches):
        months[idx].remove(matches[choice])
        print("Pass borttaget!")
    else:
        print("Ogiltigt val.")

# main funktionen, kallar på functionerna beroende på användar input alternativ
def main():
    while True:
        show_menu()
        choice = input("Val: ")
        if choice == "1":
            view_day()
        elif choice == "2":
            add_session()
        elif choice == "3":
            remove_session()
        elif choice == "4":
            break
        else:
            print("Ogiltigt val")

if __name__ == "__main__":
    main()