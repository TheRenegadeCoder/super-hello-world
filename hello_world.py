import sys
import pathlib

error = ", ".join(map(str.capitalize, pathlib.Path(sys.argv[0]).stem.split("_"))) + "!"

try:
    raise Exception(error)
except Exception as e:
    for character in str(e):
        print(character, end="")
    print()
