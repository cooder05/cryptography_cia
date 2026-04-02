from hill import clean_text,pad_text

def text_2_binblocks(text):
    blocks = []
    for i in range(0,len(text),2):
        bin1 = str(format(ord(text[i]), '08b'))     #8-bit binary
        bin2 = str(format(ord(text[i+1]),'08b'))    #8-bit binary
        block = bin1+bin2                           #16-bit binary
        blocks.append(block)
    return blocks
    

def xor16_hash(htext,ks):
    msg = clean_text(htext)
    msg += ks   #key in array form
    msg = pad_text(msg,2)
    blocks = text_2_binblocks(msg)
    result = 0

    for b in blocks:
        result ^= int(b, 2)   # convert binary string -> int and XOR

    xor_binary = format(result, '016b')
    return xor_binary
