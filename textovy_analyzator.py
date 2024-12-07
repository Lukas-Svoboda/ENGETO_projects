# Hlavička projektu
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lukáš Svoboda
email: lukas.svobo1@seznam.cz
discord: svoby_
"""

# Registrovaní uživatelé
users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Texty k analýze
TEXTS = [
'''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
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

# Funkce pro ověření přihlašovacích údajů
def login():
    username = input("username: ")
    password = input("password: ")

    if users.get(username) == password:
        print(f"Welcome to the app, {username}")
        print("We have 3 texts to be analyzed.")
        return True
    else:
        print("Unregistered user, terminating the program..")
        return False

# Funkce pro výběr textu
def choose_text():
    try:
        text_number = int(input("Enter a number btw. 1 and 3 to select: "))
        if text_number < 1 or text_number > 3:
            print("Invalid choice, terminating the program..")
            return None
        else:
            return TEXTS[text_number - 1]
    except ValueError:
        print("Invalid input, terminating the program..")
        return None

# Funkce pro analýzu textu
def analyze_text(text):
    words = text.split()
    num_words = len(words)
    titlecase_words = [word for word in words if word.istitle()]
    uppercase_words = [word for word in words if word.isupper() and word.isalpha()]
    lowercase_words = [word for word in words if word.islower()]
    numeric_strings = [word for word in words if word.isdigit()]
    sum_numbers = sum(int(num) for num in numeric_strings)

    print("----------------------------------------")
    print(f"There are {num_words} words in the selected text.")
    print(f"There are {len(titlecase_words)} titlecase words.")
    print(f"There are {len(uppercase_words)} uppercase words.")
    print(f"There are {len(lowercase_words)} lowercase words.")
    print(f"There are {len(numeric_strings)} numeric strings.")
    print(f"The sum of all the numbers is {sum_numbers}")
    print("----------------------------------------")

    # Statistika délek slov
    word_lengths = {}
    for word in words:
        word_len = len(word.strip(",.!?"))
        word_lengths[word_len] = word_lengths.get(word_len, 0) + 1

    # Graf
    print("LEN|  OCCURENCES  |NR.")
    print("----------------------------------------")
    for length, count in sorted(word_lengths.items()):
        print(f"{length:>3}| {'*' * count:<13} |{count}")

# Hlavní funkce programu
def main():
    if login():
        selected_text = choose_text()
        if selected_text:
            analyze_text(selected_text)

if __name__ == "__main__":
    main()
