import pycountry
import random


def Hangman(length):
    dict = {
        0: "H",
        1: "A",
        2: "N",
        3: "G",
        4: "M",
        5: "A",
        6: "N",
    }
    return dict[length]


def split(word):
    return [l for l in word]


empty_dash = []
letters_list=[]
hangman_check = ""
hangman_length = 0
countries_list = list(pycountry.countries)
countries_num = len(pycountry.countries)
secret_country = str(countries_list[random.randint(0, countries_num)].name)
country_length = len(secret_country)
exception = [" ", "(", ")", ".", ",", "'"]
tries = 7
print(f"You have {tries} tries ")
for sc in secret_country:
    if sc==" ":
        empty_dash.append(" ")
        country_length -= 1
    elif sc=="'":
        empty_dash.append("'")
        country_length -= 1
    elif sc=="-":
        empty_dash.append("-")
        country_length -= 1
    elif sc=="(":
        empty_dash.append("(")
        country_length -= 1
    elif sc==")":
        empty_dash.append(")")
        country_length -= 1
    elif sc==".":
        empty_dash.append(".")
        country_length -= 1
    elif sc==",":
        empty_dash.append(",")
        country_length -= 1
    else:
        empty_dash.append("_")
for e in empty_dash:
    print(e, end=" ")
print("\n")
secret_country_list = split(secret_country)
while tries > 0:
    guess = str(input("Enter a letter:"))
    if (guess.lower() in secret_country or guess.upper() in secret_country) and guess not in exception and guess not in letters_list :
        for i in range(len(secret_country_list)):
            if guess.lower() == secret_country_list[i] or guess.upper() == secret_country_list[i]:
                empty_dash[i] = secret_country_list[i]
                country_length -= 1
    else:
        tries -= 1
        hangman_check += Hangman(len(hangman_check))
    letters_list.append(guess)
    for e in empty_dash:
        print(e, end=" ")
    print(f"\n{hangman_check}")
    if country_length==0:
        print("You win!!!")
        print(f"The country was {secret_country}")
        break
    print(f"You have {tries} tries left")
else:
    print("Sorry! You lost!!")
    print(f"The country was {secret_country}")
