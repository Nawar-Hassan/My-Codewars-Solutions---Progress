​
def encrypt(s, n):
    for _ in range(n):
        odd = ''.join(s[i] for i in range(len(s)) if i % 2)
        even = ''.join(s[i] for i in range(len(s)) if not i % 2)
        s = odd + even
    return s
​
def decrypt(s, n):
    for _ in range(n):
        half = len(s) // 2
        odd = s[:half]      
        even = s[half:]   
​
        decrypted = []
        for i in range(len(even)):
            decrypted.append(even[i])   
            if i < len(odd):
                decrypted.append(odd[i])
        s = ''.join(decrypted)
    return s
​
text = "012345"
enc = encrypt(text, 2)
print("Encrypted:", enc)
​
dec = decrypt(enc, 2)
print("Decrypted:", dec) 