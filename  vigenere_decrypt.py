def vigenere_decrypt(cipher, key):
    result = ""
    key = key.upper()
    j = 0
    for c in cipher:
        if c.isalpha():
            
            val = (ord(c.upper()) - ord(key[j % len(key)]) + 26) % 26
            result += chr(val + ord('A'))
            j += 1
        else:
            result += c
    return result

ciphertext_4 = "CAOWR SHVHE LOCAN AOUER RCNAS KVBOV OLNAW TSNKV WOIVG XIGWS GCCGB SGBIS FARGD ALORN MVPES EGSPS BCRLT KSRAF"


key = "JOY"

final_plaintext = vigenere_decrypt(ciphertext_4, key)

print(f"Recovered Key: {key}")
print("Final Plaintext:")
print(final_plaintext)