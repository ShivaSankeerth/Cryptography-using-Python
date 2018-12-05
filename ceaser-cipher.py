#ceaser-cipher

import pyperclip as pp

LETTERS ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
print("welcome to ceaser cipher,enter the following options to proceed!!\n")
key =int(input("Enter the key for the Algorithm >>"))
mode =input("Enter mode as M|m for encryption D|d for Decryption >>")
message =input("Enter message to be encrypted or decrypted >>")
translated =''

for symbol in message:
    if symbol in LETTERS:
        if mode == 'M' or mode =='m':
            num=LETTERS.index(symbol)
            num =(num+key)%26
            translated = translated+LETTERS[num]
        elif mode == 'D'or 'd':
            num=LETTERS.index(symbol)
            num =(num-key)%26
            translated = translated+LETTERS[num]
    elif symbol not in LETTERS :
        translated = translated+symbol

print(translated)
pp.copy(translated)
    
    
