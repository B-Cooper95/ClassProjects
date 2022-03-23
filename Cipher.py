'''
This program gives students practice with functions and casting by using the Caesar Cipher as a background context.
Students are to build 2 functions: 
 • One takes in a string and a shift value and passes each character into the next function with the shift value.
 • The other function takes in a character, converts it to an integer value, shifts it by the shift value, and returns the result.
 • The result is appended to a new string, returning the final result when finished.
 • Students must also consider how casing effects the ascii value and make exception to spaces.
'''

def shift(letter, num):
    if letter == " ":
        return letter
    val = ord(letter)+num
    if val < 65:
        val += 26
    elif val > 122:
        val -= 26
    elif val > 90 and val < 97:
        if num < 0:
            val+=26
        else:
            val-=26

    return chr(val)

def cipher(word, num):
    newSent = ""
    for i in range(len(word)):
        newSent += shift(word[i], num)
    return newSent


print(cipher("the quick brown fox jumped over the lazy dog",2))
print(cipher("the quick brown fox jumped over the lazy dog",-2))
print(cipher("the quick brown fox jumped over the lazy dog".upper(),2))
print(cipher("the quick brown fox jumped over the lazy dog".upper(),-2))

