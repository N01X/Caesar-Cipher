from Mod_function import mod


plaintext = "Hello, w0Rld!! ` = - / \\"
shift = 3

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]


ciphertext = ""

for i in plaintext:

    if i.lower() in alpha:
        position = alpha.index(i.lower())
        newIndex = mod(position + shift, len(alpha))
        if i.isupper():

            ciphertext+= alpha[newIndex].upper()

        else:

            ciphertext+= alpha[newIndex]

    elif i.isascii():
        ciphertext+= i

       
    else:
        ciphertext+= ""

    
print(ciphertext)

plaintext2 = ""
for i in ciphertext:

    if i.lower() in alpha:
        position = alpha.index(i.lower())
        newIndex = mod(position - shift, len(alpha))
        if i.isupper():

            plaintext2+= alpha[newIndex].upper()

        else:

            plaintext2+= alpha[newIndex]

    elif i.isascii():
        plaintext2+= i

    
       
    else:
        plaintext2+= ""

print(plaintext2)