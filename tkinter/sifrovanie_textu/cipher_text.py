text = input("Zadaj text: ")

ord_text = []
for char in text:
    ord_text.append(ord(char))

for i in range(len(ord_text)):
    ord_text[i] = ord_text[i] + 1

characters = []
for number in ord_text:
    characters.append(chr(number))

print("".join(characters))

