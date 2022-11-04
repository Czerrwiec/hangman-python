import re
import random

used_letters = []
word_list = []
number = 0


def find_indexes(letter):
    indexes = []
    for i, l in enumerate(word):
        if l == letter:
            indexes.append(i)
    return indexes


def score_table():
    print()
    if len(used_letters) != 0:
        print(f"Użyte litery: {used_letters}")
    print(f"Liczba prób: {tries}")
    print(word_list)
    print()


def userChoice(file):
    word = random.choice(open(file, "r", encoding="utf8").readlines()).lower()
    word = word.rstrip('\n')
    return word


def difficulty(number):
    while True:
        print("Jaki poziom trudności wybierasz?")
        try:
            number = int(input("Wybierz 1, 3 lub 5 (numery odpowiadają liczbom szans): "))
            if number == 1:
                return number
            if number == 3:
                return number
            if number == 5:
                return number
            else:
                print()
                print("Wybierz wartość 1, 3 lub 5.")
                print() 
                continue
        except:
            ValueError
            print()
            print("Wybierz wartość 1, 3 lub 5.")
            print()
            continue


tries = difficulty(number)

while True: 
    print()
    print("1. Imiona męskie")
    print("2. Imiona żeńskie")
    print("3. Imiona mieszane")
    print("4. Rzeczowniki")
    try:
        user_choice = int(input("Wybierz zestaw haseł: "))
        if user_choice == 1:
            word = userChoice("Python hangman\imiona meskie.txt")
            break
        if user_choice == 2:
            word = userChoice("Python hangman\imiona zenskie.txt")
            break      
        if user_choice == 3:
            word = userChoice("Python hangman\imiona mieszane.txt")
            break
        if user_choice == 4:
            word = userChoice("Python hangman\ki.txt")
            break
        else:
            continue
    except:
        ValueError
        print()
        print("Wybierz od 1-4.")
        continue 

for x in word:
    word_list.append("_")  

while True:        
    score_table()
    letter = input("Podaj literę: ").lower()
    if re.search(r"^[a-złżźąęśćóń]$", letter) and letter not in used_letters:
        used_letters.append(letter)
    else:
        if letter in used_letters:
            print("Podana litera została już użyta.")
            continue
        else:
            print()
            print("Podaj literę od a-z.")
            continue
                    
    found_indexes = find_indexes(letter)

    if len(found_indexes) == 0:
        print("Nie ma takiej litery w tym słowie.")
        print()
        tries -= 1
                    
    for x in found_indexes:
        word_list[x] = letter

    if "".join(word_list) == word:
        print(f"Brawo! Słowo to {word.upper()}")
        winList = []
        for i in word_list:
            winList.append(i.upper())
        print()
        print(winList)
        print()  
        quit()

    if tries == 0:
        print(f"Liczba prób: {tries}")
        choice = input("Niestety przegrałeś, czy chcesz odkryć słowo? (t/n) ")
        if choice == "t" or choice == "T":
            print()
            print(f"Słowo to {word.upper()}")
            quit()
        else:
            quit()

