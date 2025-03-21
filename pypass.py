#!/usr/bin/env python3

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(f"---------------------------------------------------------------------------------------------------------------------------\n\n")

print(r"""#  ____  _                                                                     _    ____                           _              
# / ___|| |_ _ __ ___  _ __   __ _   _ __   __ _ ___ _____      _____  _ __ __| |  / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __  
# \___ \| __| '__/ _ \| '_ \ / _` | | '_ \ / _` / __/ __\ \ /\ / / _ \| '__/ _` | | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__| 
#  ___) | |_| | | (_) | | | | (_| | | |_) | (_| \__ \__ \\ V  V / (_) | | | (_| | | |_| |  __/ | | |  __/ | | (_| | || (_) | |    
# |____/ \__|_|  \___/|_| |_|\__, | | .__/ \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|    
#                            |___/  |_|                                                                                           """)

print(f"\n\n---------------------------------------------------------------------------------------------------------------------------")

nr_letters = int(input("\t\tHow many letters would you like in your password?(a-z)(A-Z) , 52 letters -- \n\t\t"))
nr_symbols = int(input(f"\t\tHow many symbols would you like?\n\t\t"))
nr_numbers = int(input(f"\t\tHow many numbers would you like?(0-9)\n\t\t"))

password = ""
for i in range(0,nr_letters):
    password += random.choice(letters)
for i in range(0,nr_symbols):
    password += random.choice(symbols)
for i in range(0,nr_numbers):
    password += random.choice(numbers)

passlist = list(password)
random.shuffle(passlist)

jumbled = ''.join(passlist)
print(f"Your randomly generated password is -- {jumbled}")




