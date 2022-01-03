def en(plaintext, key):
    encoded = []

    for i in range(len(plaintext)):
        xor = ord(plaintext[i]) ^ ord(key[i % len(key)])
        encoded.append(chr(xor))

    return ''.join(encoded)

def dek(chipertext, key):
    return en(chipertext, key)

def main():
    # fungsi enkripsi
    plaintext = str(input("Masukkan Plaintext: "))
    key = 'XYZ'

    print("Plaintext: ", plaintext)
    print("Enkripsi: ", en(plaintext, key))

    # fungsi dekripsi
    chipertext = str(input("Masukkan Chipertext: "))
    key = "XYZ"

    print("Chipertext: ", chipertext)
    print("Dekripsi: ", dek(chipertext, key))

main()
