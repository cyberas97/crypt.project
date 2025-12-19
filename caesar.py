def caesar_decrypt(cipher, k=3):
    result = ""
    for c in cipher:
        if c.isalpha():
            
            result += chr((ord(c) - ord('A') - k) % 26 + ord('A'))
        else:
           
            result += c
    return result


cipher_text = "WKHUH LVVRP HWKLQ JJRRG LQDOO VHHPL QJIDL OXUHV BRXDU HQRWW RVHHW KDWQR ZWLPH ZLOOU HYHDO LWEHS DWLHQ W"

plain_text = caesar_decrypt(cipher_text, k=3)

print(plain_text)