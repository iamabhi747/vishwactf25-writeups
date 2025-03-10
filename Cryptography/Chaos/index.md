---
title: "Chaos"
parent: "Cryptography"
---

# Chaos

> VishwaCTF{CrYpt0_cRyPT0_1g_It_1s_sOm3_7hiNg_t0_D0}

This simple cryptography challenge, we are given a encrypted text file and a python script which was used to encrypt the text file. It was using xor for the encryption. the encrypt function is as follows:

```python
def xor_encrypt(msg):
    transformed = bytearray(msg)
    for i in range(len(transformed)):
        transformed[i] ^= (i % 256)  
    return base64.b85encode(transformed).decode() 
```

and yes it is very simple to create `xor_decrypt` function for this. infact you can use the same function to decrypt the message just need to modify input-output encodings.

```python
def xor_decrypt(enc_msg):
    transformed = bytearray(base64.b85decode(enc_msg))
    for i in range(len(transformed)):
        transformed[i] ^= (i % 256)  
    return transformed
```

After description of text file, we got buch of english lines, 3 fake flags (i hate that) and the real flag.

```text
Perhaps the flag is encoded in Base64? Or maybe hex?Or maybe the real flag is just one character different from all these fakes?VishwaCTF{Fl4g_Or_N0t_Th4t_1s_Th3_QuesT10n}Maybe the flag is hidden elsewhere...VishwaCTF{T00_M4ny_F4k3_Fl4Gs_G00d_Luck}Or inside a comment in the source code?This is not the flag, keep looking!Or maybe there's a script generating multiple fake flags dynamically?VishwaCTF{CrYpt0_cRyPT0_1g_It_1s_sOm3_7hiNg_t0_D0}Maybe it's inside another challenge, cross-referencing flags?Or is it?But wait... isn't this too obvious?What if it's a hash of the real flag?VishwaCTF{NoT_ThE_ReaL_fLaG_K33P_tRy1Ng}Or hidden in an image using steganography?Happy hunting!VishwaCTF{Y0u_WiLl_N3v3r_F1nd_1t}Or maybe the real flag is hidden inside a hidden file?Find_the_real_flag_somewhere_in_this_messOh, did you think that was real? Keep digging!
```