alpha = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z"]
tempteststore = []
finaldecisionstore = []
lettersDone = 0
lettershift = int(input("How many letters would you like to shift?\n[If you would like to move up the text, input the numbers negative counterpart.]\n")) * 2

phrase = input("Enter the phrase to be shifted:\n")

# Ignore [doesnt need changing]
for letter in phrase:
    tempteststore.append(letter)

# Converter
for letter in tempteststore:
    i = 0
    found = False
    while not found and i < len(alpha) and lettersDone <= len(tempteststore):
        if letter == " ":
            finaldecisionstore.append(" ")
            found = True
        elif alpha[i] == letter:
            finaldecisionstore.append(alpha[i - lettershift])
            found = True
        elif letter.isdigit():
            finaldecisionstore.append(letter)
            found = True
        elif letter in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", '"', ",", ".", "<", ">", "/", "?", "\\", "|"]:
            finaldecisionstore.append(letter)
            found = True
        else:
            i += 1
    lettersDone += 1

print("".join(finaldecisionstore))
