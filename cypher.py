text = input("Text: ")
shift = int(input("Shift: "))
cypher = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in text.lower():
    index = alphabet.find(i)
    cypher = cypher + alphabet[index+shift]
print(cypher)
