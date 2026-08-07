#loading
print("loading encryption machine...")

#importing library
import time
import shutil
import pyperclip
import random

#defining global varible

vencrypt = False
key = None
temp = ""
finish = []
text_list = []
counter = 0

from alphabet import alphabet

#defining function

def encrypt(letter) :
    counter = alphabet.index(letter)
    for x in range(0 ,key) :
        counter += 1
        if counter > len(alphabet) - 1 :
            counter = 0

    return alphabet[counter]

def decrypt(letter) :
    counter = alphabet.index(letter)
    for x in range(0 ,key) :
        counter -= 1
        if counter < 0 :
            counter = len(alphabet) - 1

    return alphabet[counter]

print("loading finished")
#finished loading

#getting key

key = input("key(int): ")
if len(key) == 0 :
    key = 3

elif "ra" in key :
    key = random.randint(3 ,100)
    print(f'key = "{key}"')

else :
    key = int(key)

#getting mode

while True :
    
    mode = input("please input mode: ")
    mode = mode.lower()

    if "en" in mode :
        mode = True
        vencrypt = True
        break

    elif "dec" in mode :
        mode = False
        vencrypt = True
        break

    elif "ex" in mode :
        break
    
    else :
        print(f'"{mode}" is an invalid mode')


#getting text

if vencrypt == True :
    text = input("input text: ")
    text_list = list(text)


#encryption mode

if mode and vencrypt :
    for x in range(0 ,len(text_list)) :
        if not text_list[x] == " " :
            finish.append(encrypt(text_list[x]))

        else :
            finish.append(" ")

    for i in range(0 ,len(finish)) :
        temp = temp + finish[i]


    print("")
    print(f"{text} = {temp}")

#decrypt mode

if not mode and vencrypt :
    for x in range(0 ,len(text_list)) :
        if not text_list[x] == " " :
                   finish.append(decrypt(text_list[x]))

        else :
            finish.append(" ")


    for i in range(0 ,len(finish)) :
        temp = temp + finish[i]

    print("")
    print(f"{text} = {temp}")

#copying to clipboard

if vencrypt == True :
    pyperclip.copy(temp)

    print("")
    print(f'"{temp}" have been copied to clipboard')



shutil.rmtree("__pycache__")
