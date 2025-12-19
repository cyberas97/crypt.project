def hill_decrypt(cipher, K):
    K_inv = np.linalg.inv(K)
    K_inv = np.round(K_inv * np.linalg.det(K)).astype(int) % 26
    result = ""
    for i in range(0, len(cipher), 3):
        block = [ord(c) - ord('A') for c in cipher[i:i+3]]
        plain = np.dot(K_inv, block) % 26
        result += ''.join(chr(int(x) + ord('A')) for x in plain)
    return result
