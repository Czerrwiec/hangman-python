import re

word = "hangman"
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
    
    found_indexes = find_indexes(letter)

    if len(found_indexes) == 0:
        print("Nie ma takiej litery w tym słowie.")
        print()
        tries -= 1
    
    for x in found_indexes:
        word_list[x] = letter

    if "".join(word_list) == word:
        print(f"Brawo! Słowo to {word.upper()}")

    if tries == 0:
        print(f"Liczba prób: {tries}")
        choice = input("Niestety przegrałeś, czy chcesz odkryć słowo? (t/n) ")
        if choice == "t" or choice == "T":
            print()
            print(f"Słowo to {word.upper()}")
            quit()
        else:
            quit()
            
    
