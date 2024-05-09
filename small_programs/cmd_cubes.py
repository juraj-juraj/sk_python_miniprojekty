# Prva iteracia, velkost strany sa zadava po spusteni programu

# velkost_strany = int(input("Zadaj velkost strany stvorca: "))

# print(f"Obsah stvorca je {velkost_strany ** 2}")

# print("*" * velkost_strany)
# for _ in range(velkost_strany - 2):
#     print("*" + " " * (velkost_strany - 2) + "*")
# print("*" * velkost_strany)


# Druha iteracia velkost strany sa zadava ako argument v prikazovom riadku

# import argparse

# parser = argparse.ArgumentParser(description="Program na vypocet obsahu stvorca")

# parser.add_argument("side", type=int, help="size of a side of a square")
# parser.add_argument(
#     "-o",
#     "--output",
#     default="-",
#     type=argparse.FileType(mode="w"),
#     help="size of a side of a square",
# )
# args = parser.parse_args()

# args.output.write(f"Obsah stvorca je {args.side ** 2}\n")
# args.output.write("*" * args.side + "\n")
# args.output.write(("*" + " " * (args.side - 2) + "*\n") * (args.side - 2))
# args.output.write("*" * args.side + "\n")

# Tretia iteracia zadavame velkosti stran obdlznika

import argparse

parser = argparse.ArgumentParser(
    description="Program na kreslenie obdlznika na prikazovy riadok"
)

parser.add_argument("--height", type=int, help="Height of a rectangle")
parser.add_argument("--width", type=int, help="Width of a rectangle")

args = parser.parse_args()

print(f"Obsah obdlznik: {args.height * args.width}")
print("*" * args.width)
for _ in range(args.height - 2):
    print("*" + " " * (args.width - 2) + "*")
print("*" * args.width)
