import random
import string

heslo = "".join(random.choices("1324567890" + string.ascii_letters, k=8))

print(f"Vygenerovane heslo: {heslo}")

# pole_znakov = []
# for _ in range(10):
#     pole_znakov.append(chr(random.randint(33, 127)))

# heslo = "".join(pole_znakov)
# print(f"Heslo: {heslo}")
