try:
    raise Exception("Hello, World!")
except Exception as e:
    for character in str(e):
        print(character, end="")
    print()
