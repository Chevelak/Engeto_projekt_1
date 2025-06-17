#"""
#projekt_1.py: první projekt do Engeto Online Python Akademie

#author: Tomáš Vlach
#mail: vlacht@centrum.cz
#"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

#import
import sys
import re

from collections import Counter

#oddělovníky
lines = "_" * 40

#pozdrav
welcome = "Welcome in the text analyzer!".center(40)
print(welcome)
print("=" * len(welcome))
print("\n")

#uživatelé
users = {
    "user_a": {"name": 'bob', "pass": '123'},
    "user_b": {"name": 'ann', "pass": 'pass123'},
    "user_c": {"name": 'mike', "pass": 'password123'},
    "user_d": {"name": 'liz', "pass": 'pass123'}
}

print("Insert your login details:".center(40))
insert_name = input("Insert your username: ")


#kontrola přihlášení
user_found = False
valid_login = False

for user in users.values():
    if insert_name == user["name"]:
        user_found = True

        for attempt in range(3):
            insert_pass = input(f"Insert your password (Attempt {attempt + 1}/3): ")
            if insert_pass == user["pass"]:
                print(f"Welcome {user['name']} in the text analyzer!".center(40))
                valid_login = True
                break
            else:
                print("Password is not correct.".center(40))

        if not valid_login:
            print("All three attemps were used. Access denied!".center(40))
        break
        
if not user_found:
    print("Not a registered user.".center(40))

if not valid_login:
    sys.exit(1)
 

print(lines)
print("\n")

#výběr textu a podmínky
print(f"{insert_name} choose from three texts:".center(40))

while True:
    try:
        number = int(input("Enter a number from 1 to 3:"))

        if 1 <= number <= 3:
            num_text = number - 1
            print(f"Text {number} was choose!".center(40))
            break       
        else:
            print("Wrong input!".center(40))

    except ValueError:
        print("Invalid input! Please enter a whole number.".center(40))

print(lines)
print("\n")


#analýza textu

words_split = re.findall(r'\b\w+\b', TEXTS[num_text])

    # inicalizace počítání
num_words = len(words_split)
title_words = 0      
UP_words = 0         
lower_words = 0      
num_string = 0       
sum_numbers = 0      

for word in words_split:
    if word.isdigit():
        num_string += 1
        sum_numbers += int(word)

    if word.isupper() and len(word) > 1:
        UP_words += 1
   
    elif word.istitle():
        title_words += 1

    elif word.islower():
        lower_words += 1

    # výpis výsledků
print(f"Number of words    = {num_words}")
print(f"Titlecase words    = {title_words}")
print(f"Uppercase words    = {UP_words}")    
print(f"Lowercase words    = {lower_words}")  
print(f"Numeric strings    = {num_string}")
print(f"Sum of all numbers = {sum_numbers}")

#Graf

    # počítadlo délky slov
lengths = [len(word) for word in words_split]
counts = Counter(lengths)

    # pojmenovani sloupců grafu
print("LEN|\tOCCURENCES\t|NR.")
print("-" * 28)

    # hvězdičkový graf
for length in sorted(counts):
    stars = '*' * counts[length]
    print(f"{length:>3}|{stars:<16}\t|{counts[length]}")
