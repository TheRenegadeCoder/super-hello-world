def hello_world():
    try:
        error = format_error(get_error(hello_world.__name__))
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


def get_exception(shout):
    i = shout[0]
    if shout[1:]:
        i += get_issue(shout[1:])
    return i


def get_issue(whisper):
    w = whisper[0]
    if whisper[1:]:
        w += get_error(whisper[1:])
    return w


hello_world()
