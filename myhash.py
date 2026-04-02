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
