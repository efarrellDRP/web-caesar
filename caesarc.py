alphabet='abcdefghijklmnopqrstuvwxyz'
key_index=[]
j=0
def alphabet_position(key):
    j=0
    for i in key:
        for j in range(len(alphabet)):
            if i.lower()==alphabet[j]:
                key_index.append(j)
    return key_index



def rotate_character(char, rot):
    cipher=0
    if char.isalpha()==True:
        for i in range(len(alphabet)):
            if char.istitle()==False:
                if char.lower()==alphabet[i]:
                    cipher=i+rot
                    if cipher<26:

                        return alphabet[cipher]

                    else:
                        cipher=cipher%26

                        return alphabet[cipher]
            elif char.istitle()==True:
                if char.lower()==alphabet[i]:
                    cipher=i+rot
                    if cipher<26:

                        return alphabet[cipher].upper()

                    else:
                        cipher=cipher%26

                        return alphabet[cipher].upper()
    else:
        return(char)

def encrypt(text, rot):
    caesar=''
    for i in text:
        caesar+=rotate_character(i,rot)
    return caesar
