from hill import hill_encrypt, hill_decrypt
import myhash
import numpy as np

K = np.array([[6,24,1],
              [13,16,10],
              [20,17,15]])

key_string = "GYBNQKURP"

plaintext = "HELLOWORLD"

cipher = hill_encrypt(plaintext, K)
hashval = xor16_hash(cipher, key_string)
recovered = hill_decrypt(cipher, K)

print("Plaintext :", plaintext)
print("Ciphertext:", cipher)
print("Hash      :", hashval)
print("Decrypted :", recovered)
