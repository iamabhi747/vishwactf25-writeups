---
title: "Leaky Stream"
parent: "Digital Forensics"
---

# Leaky Stream 
> VishwaCTF{this_is_first_part_this_second_part}

The challenge had a pcapng file. Just running the `findstr "Vishwa" chitty-chat.pcapng` command on it revealed the first part of the flag which was `VishwaCTF{this_is_first_part` .

![Screenshot (138)](https://github.com/user-attachments/assets/59c11e20-acff-4333-8a4b-0bfdbd314f7a)

Seeing this I ran `findstr "second" chitty-chat.pcapng` which revealed the second part of the flag `_this_second_part}`

![Screenshot (139)](https://github.com/user-attachments/assets/a174a6eb-c0ed-4ded-99c8-dcbd834cec3a)

