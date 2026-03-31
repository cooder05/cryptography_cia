# cryptography_cia

# Toy XOR Hash (16-bit) — Explanation

This module implements a **very simple educational hash function** based on XORing
16-bit binary blocks derived from text.

> ⚠️ This is **not cryptographically secure**. It is for learning purposes only.

---

## Overview

The hash works in five stages:

1. Clean the text (A–Z only, uppercase)
2. Append a fixed key string: `"GYBNQKURP"`
3. Pad the text to even length
4. Convert every 2 characters → one 16-bit binary block
5. XOR all 16-bit blocks together to produce a final 16-bit hash

---

## Step 1 — Clean Text

```python
def clean_text(s):
    return ''.join([c for c in s.upper() if c in string.ascii_uppercase])
