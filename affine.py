def affine_decrypt(cipher, a, b):
    def modinv(a, m=26):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    a_inv = modinv(a)
    result = ""
    for c in cipher:
        if c.isalpha():
            result += chr((a_inv * (ord(c) - ord('A') - b)) % 26 + ord('A'))
        else:
            result += c
    return result
ciphertext_2 = "ZRCPC WUUAQ CZRWV MMAAX WVILL UCCQW VMHIW LEPCU YAEIP CVAZZ AUCCZ RIZVA OZWQC OWLLP CJCIL WZNCF IZWCV Z"


a = 5
b = 8


final_plaintext = affine_decrypt(ciphertext_2, a, b)

print(f"Recovered Keys: a = {a}, b = {b}")
print("Final Plaintext:")
print(final_plaintext)