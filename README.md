# cryptography_cia

# Toy XOR Hash (16-bit) — Explanation

This module implements a **very simple educational hash function** based on XORing
16-bit binary blocks derived from text.

---

## Overview

The hash works in five stages:

The hash is computed **from the ciphertext**, not the original plaintext.

---

## Step 1 — Input Is the Ciphertext

After Hill encryption, the text:

- Contains only uppercase letters A–Z
- Is padded to a multiple of 3
- Has been transformed using matrix multiplication mod 26

The hash operates on this encrypted output.

---

## Step 2 — Append Key String

This string represents the Hill cipher key matrix written row-wise as letters.

Appending it ensures the hash depends on both:

- The ciphertext
- The encryption key

---

## Step 3 — Pad to Even Length

The hash processes **2 characters at a time**, so the message is padded with `'X'` if needed to make the length even.

---

## Step 4 — Convert Text to 16-bit Binary Blocks

Each pair of characters becomes one 16-bit block:

1. Convert each character to ASCII
2. Represent ASCII as 8-bit binary
3. Concatenate to form a 16-bit block

Example:

| Char | ASCII | 8-bit Binary |
|------|-------|---------------|
| H    | 72    | 01001000      |
| E    | 69    | 01000101      |

16-bit block:

0100100001000101
---

## Step 5 — XOR All 16-bit Blocks

Each block is:

1. Converted from binary string to integer (base 2)
2. XORed with an accumulator

The final value is formatted back into 16-bit binary:

---
