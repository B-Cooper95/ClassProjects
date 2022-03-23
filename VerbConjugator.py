
def conjug(pro, verb):
    stem, ending = verb[:-2], verb[-2:]
    if pro == "yo":
        word = stem + "o"
    elif pro == "tu":
        if ending == "ar":
            word = stem + "as"
        else:
            word = stem + "es"
    elif pro == "nosotros":
        word = verb[:-1] + "mos"
    elif pro == "el" or pro == "ella" or pro == "usted":
        if ending == "ar":
            word = stem + "a"
        else:
            word = stem + "e"
    elif pro == "ellos" or pro == "ellas" or pro == "ustedes":
        if ending == "er":
            word = stem + "an"
        else:
            word = stem + "en"
    print(pro + " " + word)



print()
conjug("el", "correr")
conjug("nosotros", "ayudar")
conjug("tu", "ayudar")

