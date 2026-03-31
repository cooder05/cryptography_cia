import numpy as np
import string
from math import gcd

MOD = 26

text = "helloworld"
K =np.array([[6,24,1],[13,16,10],[20,17,15]])
             #G,Y ,B,  N ,Q ,K ,  U ,R ,P

def clean_text(s):
    return ''.join([c for c in s.upper() if c in string.ascii_uppercase])

def pad_text(s, n):
    while len(s) % n != 0:
        s += 'X'
    return s

def text_to_vec(block):
    return np.array([ord(c) - ord('A') for c in block])

def vec_to_text(v):
    return ''.join(chr(int(x) % 26 + ord('A')) for x in v)

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No modular inverse")

def matrix_modinv(matrix, modulus):
    det = int(round(np.linalg.det(matrix)))
    det_mod = det % modulus

    if gcd(det_mod, modulus) != 1:
        raise ValueError("Matrix not invertible mod 26")

    det_inv = modinv(det_mod, modulus)

    # Adjugate matrix
    adj = np.round(det * np.linalg.inv(matrix)).astype(int)
    return (det_inv * adj) % modulus


def hill_encrypt(ptext):
    msg = clean_text(ptext)
    msg = pad_text(msg,3)
    cipher_text = ""

    for i in range(0, len(msg), 3):
        block = text_to_vec(msg[i:i+3])
        encrypted = np.dot(K, block) % MOD
        cipher_text += vec_to_text(encrypted)
    
    return cipher_text

def hill_decrypt(ciphertext):
    K_inv = matrix_modinv(K, MOD)
    plaintext = ""

    for i in range(0, len(ciphertext), 3):
        block = text_to_vec(ciphertext[i:i+3])
        decrypted = np.dot(K_inv, block) % MOD
        plaintext += vec_to_text(decrypted)

    return plaintext

encrypt = hill_encrypt(text)
print("cyphertext: ",encrypt)
fin = hill_decrypt(encrypt,)
print("plaintext: ",fin)

def text_2_binblocks(text):
    blocks = []
    for i in range(0,len(text),2):
        bin1 = str(format(ord(text[i]), '08b'))     #8-bit binary
        bin2 = str(format(ord(text[i+1]),'08b'))    #8-bit binary
        block = bin1+bin2                           #16-bit binary
        blocks.append(block)
    return blocks
    


def myhash(htext):
    msg = clean_text(htext)
    msg += "GYBNQKURP"   #key in array form
    msg = pad_text(msg,2)
    blocks = text_2_binblocks(msg)
    result = 0

    for b in blocks:
        result ^= int(b, 2)   # convert binary string -> int and XOR

    xor_binary = format(result, '016b')
    print("hash: ",xor_binary)

myhash(text)