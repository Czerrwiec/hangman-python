import re
import random





# word = "hangman"
used_letters = []
word_list = []
tries = 5


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

while True:
    print()
    print("1. Imiona męskie")
    print("2. Imiona żeńskie")
    print("3. Imiona mieszane")
    print("4. Rzeczowniki")
    try:
        user_choice = int(input("Wybierz zestaw haseł: "))
        if user_choice == 1:
            word = random.choice(open("Python hangman\imiona meskie.txt", "r", encoding="utf8").readlines()).lower()
            word = word.rstrip('\n')
        if user_choice == 2:
            word = random.choice(open("Python hangman\imiona zenskie.txt", "r", encoding="utf8").readlines()).lower()
            word = word.rstrip('\n')      
        if user_choice == 3:
            word = random.choice(open("Python hangman\imiona mieszane.txt", "r", encoding="utf8").readlines()).lower()
            word = word.rstrip('\n')
        if user_choice == 4:
            word = random.choice(open("Python hangman\rzeczowniki.txt", "r", encoding="utf8").readlines()).lower()
            word = word.rstrip('\n')
    except:
        ValueError
        print()
        print("Wybierz od 1-4.")
        continue
    

    print(word)

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
            print()
            print(word_list)
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
                
    
