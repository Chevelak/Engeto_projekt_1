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
lines = "_" * 35

#pozdrav
welcome = "Welcome in the text analyzer!"
print(welcome)
duble_lines = "=" * len(welcome)
print(duble_lines)
print("\n")

#přihlášení
user_a = dict(name_a="bob", pass_a="123")
user_b = dict(name_b="ann", pass_b="pass123")
user_c = dict(name_c="mike", pass_c="password123")
user_d = dict(name_d="liz", pass_d="pass123")

print("Insert your login details:")
insert_name = input("Insert your username:")
insert_pass = input("Insert your password:")

#kontrola přihlášení
valid_login = False

if insert_name == user_a["name_a"]:
    if insert_pass == user_a["pass_a"]:
        print(f"Welcome {user_a["name_a"]} in the text analyzer!")
        valid_login = True
    else:
        print("Password is not correct")
        
elif insert_name == user_b["name_b"]:
    if insert_pass == user_b["pass_b"]:
        print(f"Welcome {user_b["name_b"]} in the text analyzer!")
        valid_login = True
    else:
        print("Password is not correct")
        
elif insert_name == user_c["name_c"]:
    if insert_pass == user_c["pass_c"]:
        print(f"Welcome {user_c["name_c"]} in the text analyzer!")
        valid_login = True
    else:
        print("Password is not correct")
        
elif insert_name == user_d["name_d"]:
    if insert_pass == user_d["pass_d"]:
        pozdrav_d = print(f"Welcome {user_d["name_d"]} in the text analyzer!")
        valid_login = True
    else:
        print("Password is not correct")
        
else:
    print("Not a registered user!")

if not valid_login:
    sys.exit(1)   

print(lines)
print("\n")

#výběr textu
print(f"{insert_name} choose from three texts:")
numer = int(input("Enter a number from 1 to 3:"))
num_text = numer - 1
print(lines)
print("\n")


#Analýza textu

    #počet slov
words_split = TEXTS[num_text].split()
num_words = print(f"Number of words = {len(words_split)}")

    #počet slov s velkým a malým začátečním písmenem a slov s velkými písmeny
upper_words = 0
lower_words = 0
UP_words = 0

for word in words_split:
    if word.isupper() and len(word) > 1:
        UP_words += 1
    elif word[0].isupper() and word[1:].islower():
        upper_words += 1
    elif word.islower():
        lower_words += 1

print(f"Uppercase words = {UP_words}")
print(f"Titlecase words = {upper_words}")
print(f"Lowercase words = {lower_words}")

    #počet číselných stringu v textu
n = re.findall(r"\d+", TEXTS[num_text])
n_num = len(n)
print(f"Numeric strings = {n_num}")

    #součet čísel v textu
all_n = sum(map(int, n))
print(f"Sum of all numbers = {all_n}")


#Graf

    # počítadlo délky slov
words = re.findall(r'\b\w+\b', TEXTS[num_text])
lengths = [len(word) for word in words]
counts = Counter(lengths)

    # pojmenovani sloupců grafu
print("LEN|\tOCCURENCES\t|NR.")
print("-" * 28)

    # hvězdičkový graf
for length in sorted(counts):
    stars = '*' * counts[length]
    print(f"{length:>3}|{stars:<16}\t|{counts[length]}")
