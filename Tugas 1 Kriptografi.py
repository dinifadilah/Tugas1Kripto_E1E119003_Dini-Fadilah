def enkripsi(plaintext, key):
    encoded = []

    for i in range(len(plaintext)):
        xor = ord(plaintext[i]) ^ ord(key[i % len(key)])
        encoded.append(chr(xor))

    return ''.join(encoded)

def dekripsi(chipertext, key):
    return enkripsi(chipertext, key)

def main():
    # fungsi enkripsi
    plaintext = str(input("Masukkan Plaintext: "))
    key = 'XYZ'

    print("Plaintext: ", plaintext)
    print("Enkripsi: ", enkripsi(plaintext, key))

    # fungsi dekripsi
    chipertext = str(input("Masukkan Chipertext: "))
    key = "XYZ"

    print("Chipertext: ", chipertext)
    print("Dekripsi: ", dekripsi(chipertext, key))

main()
