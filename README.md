# Hill Cipher + Custom 16-bit XOR Hash

This project implements:

- The **Hill cipher** (3×3 matrix, modulo 26) for encryption and decryption
- A **custom 16-bit XOR-based hash function** computed from the ciphertext and key

---

## Theory

### Hill Cipher

The Hill cipher is a classical polygraphic substitution cipher based on linear algebra.

Encryption is performed using:

\[
C = K \cdot P \pmod{26}
\]

Where:

- \(K\) is a 3×3 invertible key matrix modulo 26
- \(P\) is a vector of plaintext letters
- \(C\) is the resulting ciphertext vector

To decrypt, the modular inverse of the key matrix is computed and applied to the ciphertext.

---

### Custom 16-bit XOR Hash

The hashing function is intentionally simple for educational purposes.

The hash is computed **from the ciphertext**, not the plaintext.

#### Steps:

1. Append the key string (matrix written row-wise as letters) to the ciphertext
2. Pad the result to an even number of characters
3. Split into 2-character blocks
4. Convert each character to its ASCII 8-bit binary form
5. Combine into 16-bit blocks
6. XOR all 16-bit blocks together
7. Output the final 16-bit binary value

This design demonstrates why real cryptographic hashes require complex non-linear mixing.

---

## Files in This Repository

| File | Description |
|---|---|
| `hill.py` | Implementation of Hill encryption and decryption |
| `myhash.py` | Implementation of custom XOR 16-bit hash |
| `test_roundtrip.py` | Demonstrates encrypt → hash → decrypt process |
---

## How to Run

Ensure Python and NumPy are installed.

## How to Run

Make sure Python and NumPy are installed.

```bash
python test_roundtrip.py
