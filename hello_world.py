def hello_world():
    error = format_error(get_error(hello_world.__name__))
    try:
        raise Exception(error)
    except Exception as e:
        for character in str(e):
            print(character, end="")
        print()


def format_error(error):
    return ", ".join(map(str.capitalize, error.split("_"))) + "!"


def get_error(message):
    c = message[0]
    if message[1:]:
        c += get_exception(message[1:])
    return c


def get_exception(message):
    c = message[0]
    if message[1:]:
        c += get_issue(message[1:])
    return c


def get_issue(message):
    c = message[0]
    if message[1:]:
        c += get_error(message[1:])
    return c


hello_world()
