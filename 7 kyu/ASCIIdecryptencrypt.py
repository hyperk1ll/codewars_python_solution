# ASCII Shift Encryption/Decryption 

def ascii_encrypt(plaintext):
    encrypted = ""
    for i in range (len(plaintext)):
        encrypted += chr(ord(plaintext[i]) + i)
    return encrypted

def ascii_decrypt(plaintext):
    decrypted = ""
    for i in range (len(plaintext)):
        decrypted += chr(ord(plaintext[i]) - i)
    return decrypted
