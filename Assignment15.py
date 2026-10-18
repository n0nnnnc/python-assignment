plaintext = input("Enter your plaintext (Alphabet Only):")
secretkey = int(input("Enter your secret key (Number Only):"))

# ASCII
# A-Z => 65-90
# a-z => 97-122

"""
Encryption
    index a=0, b=1 , c=2, and so on
    shift == k mod 26
    index of new letter after shifted: [(index of old letter) + shift] mod 26
"""


def encrypt(P, k):
    ciphertext = ""
    shift = k % 26
    for i in P:
        min_ascii = 65 if i.isupper() else 97
        index = ((ord(i) - min_ascii) + shift) % 26
        cipherletter = chr(min_ascii + index)
        ciphertext += cipherletter
    return ciphertext


"""
Decryption
    index a=0, b=1 , c=2, and so on
    shift == k mod 26
    index of new letter after shifted: [(index of old letter) - shift] mod 26
"""


def decrypt(C, k):
    ciphertext = ""
    shift = k % 26
    for i in C:
        min_ascii = 65 if i.isupper() else 97
        index = ((ord(i) - min_ascii) - shift) % 26
        cipherletter = chr(min_ascii + index)
        ciphertext += cipherletter
    return ciphertext


ciphertext = encrypt(plaintext, secretkey)
print("The encrypted ciphertext:", ciphertext, sep="")
decryptedtext = decrypt(ciphertext, secretkey)
print("The decryption results:", decryptedtext, sep="")
print("")
