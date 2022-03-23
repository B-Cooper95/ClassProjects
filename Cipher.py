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

