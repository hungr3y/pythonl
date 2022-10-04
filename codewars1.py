

def alphabet_position(text):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in text.lower():
        if type(i) != str:
            continue

        if i in alphabet:
            a = alphabet.index(i)+1
            print(str(a), end=" ")

alphabet_position("aaa1a")

alphabet_position("The sunset sets at twelve o' clock.")







#alphabet_position("The sunset sets at twelve o' clock.")