def hello_world():
    error = ", ".join(map(str.capitalize, hello_world.__name__.split("_"))) + "!"
    try:
        raise Exception(error)
    except Exception as e:
        for character in str(e):
            print(character, end="")
        print()
    
hello_world()
