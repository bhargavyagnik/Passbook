import random

def generate_random_passwords(length=10):
    if(length<7):
        print("Not a good password")
        length=10
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$']
    ALL=DIGITS+LOCASE_CHARACTERS+UPCASE_CHARACTERS+SYMBOLS
    d=int(length*0.3)
    l=int(length*0.3)
    u=int(length*0.1)
    s=length-(d+u+l)
    digits=random.sample(population=DIGITS,k=d)
    locase=random.sample(population=LOCASE_CHARACTERS,k=l)
    upcase=random.sample(population=UPCASE_CHARACTERS,k=u)
    symbols=random.sample(population=SYMBOLS,k=s)
    all=digits+locase+upcase+symbols
    random.shuffle(all)
    string=''
    for i in all:
        string=string+str(i)
    print(string)


def binary_char(char,length):
    b= bin(ord(char))[2:]
    if(len(b)<length):
        b=((length-len(b))*'0')+b
    return b

def sent_binary(sentence,length):
    b=''
    for ch in sentence:
        b=b+binary_char(ch,length)
    return b

def bin_char(char):
    return chr(int(char,2))

def binsent_char(binsentence,length):
    s=''
    for ch in range(0,len(binsentence),length):
        s=s+bin_char(binsentence[ch:ch+length])
    return s


if(__name__=='__main__'):
    #generate_random_passwords()
    sentence="Bhargav Yagnik"
    length=9
    binsent=sent_binary(sentence, length)
    print(binsent)
    sen=binsent_char(binsent,length)
    print(sen)

