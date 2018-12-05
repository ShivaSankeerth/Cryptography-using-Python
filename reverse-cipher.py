#reverse-cipher

message = input("enter message to encrypt >>")
#cipher = ''
#decipher = ''

#encryption-process

def rev_cipher_encryt(message):
    i = len(message)-1
    cipher = ''
    while i>=0:
        cipher = cipher+message[i]
        i=i-1
    print("CIPHERTEXT:",cipher)
    return cipher

#decryption-process

def rev_cipher_decryt(cipher):
    i = len(cipher)-1
    decipher = ''
    while i>=0:
        decipher = decipher+cipher[i]
        i=i-1
    print("DECIPHERTEXT",decipher)


#implementation
cipher = rev_cipher_encryt(message)
rev_cipher_decryt(cipher)

